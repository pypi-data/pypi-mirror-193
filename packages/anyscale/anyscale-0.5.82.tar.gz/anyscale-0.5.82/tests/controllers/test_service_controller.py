import json
import os
from typing import Optional
from unittest.mock import Mock, mock_open, patch

import click
import pytest

from anyscale.client.openapi_client.models.apply_production_service_v2_api_model import (
    ApplyProductionServiceV2APIModel,
)
from anyscale.client.openapi_client.models.create_production_service import (
    CreateProductionService,
)
from anyscale.client.openapi_client.models.production_job_config import (
    ProductionJobConfig,
)
from anyscale.controllers.service_controller import ServiceConfig, ServiceController


def test_service_config_model_with_entrypoint():
    config_dict = {
        "entrypoint": "python test.py",
        "project_id": "test_project_id",
        "build_id": "test_build_id",
        "compute_config_id": "test_compute_config_id",
        "healthcheck_url": "test.url",
    }
    mock_validate_successful_build = Mock()
    with patch.multiple(
        "anyscale.controllers.job_controller",
        validate_successful_build=mock_validate_successful_build,
    ):
        service_config = ServiceConfig.parse_obj(config_dict)
        assert service_config.ray_serve_config is None


def test_service_config_model_with_ray_serve_config():
    config_dict = {
        "ray_serve_config": {"runtime_env": {"pip": ["requests"]}},
        "project_id": "test_project_id",
        "build_id": "test_build_id",
        "compute_config_id": "test_compute_config_id",
    }
    mock_validate_successful_build = Mock()
    with patch.multiple(
        "anyscale.controllers.job_controller",
        validate_successful_build=mock_validate_successful_build,
    ):
        service_config = ServiceConfig.parse_obj(config_dict)
        assert service_config.entrypoint is None


@pytest.mark.parametrize("use_default_project", [True, False])
@pytest.mark.parametrize("access", ["public", "private"])
@pytest.mark.parametrize("maximum_uptime_minutes", [60, None])
def test_update_service(
    mock_auth_api_client,
    use_default_project: bool,
    access: str,
    maximum_uptime_minutes: Optional[int],
) -> None:
    config_dict = {
        "entrypoint": "mock_entrypoint",
        "build_id": "mock_build_id",
        "compute_config_id": "mock_compute_config_id",
        "healthcheck_url": "mock_healthcheck_url",
        "access": access,
    }
    mock_logger = Mock()
    service_controller = ServiceController(log=mock_logger)
    if use_default_project:
        mock_infer_project_id = Mock(return_value="mock_default_project_id")
    else:
        mock_infer_project_id = Mock(return_value="mock_project_id")

    mock_validate_successful_build = Mock()

    with patch(
        "builtins.open", mock_open(read_data=json.dumps(config_dict))
    ), patch.multiple(
        "anyscale.controllers.service_controller",
        infer_project_id=mock_infer_project_id,
    ), patch.object(
        ServiceController,
        "_get_maximum_uptime_minutes",
        return_value=maximum_uptime_minutes,
    ), patch.multiple(
        "anyscale.controllers.job_controller",
        validate_successful_build=mock_validate_successful_build,
    ), patch.multiple(
        "os.path", exists=Mock(return_value=True)
    ):
        service_controller.deploy(
            "mock_config_file", name="mock_name", description="mock_description",
        )

    service_controller.api_client.apply_service_api_v2_decorated_ha_jobs_apply_service_put.assert_called_once_with(
        CreateProductionService(
            name="mock_name",
            description="mock_description",
            project_id="mock_default_project_id"
            if use_default_project
            else "mock_project_id",
            config=ProductionJobConfig(  # noqa: PIE804
                **{
                    "entrypoint": "mock_entrypoint",
                    "build_id": "mock_build_id",
                    "compute_config_id": "mock_compute_config_id",
                }
            ),
            healthcheck_url="mock_healthcheck_url",
            access=access,
        )
    )
    assert mock_logger.info.call_count == 4


def test_service_submit_parse_logic(mock_auth_api_client) -> None:
    service_controller = ServiceController()
    service_controller.generate_config_from_entrypoint = Mock()  # type: ignore
    service_controller.generate_config_from_file = Mock()  # type: ignore
    service_controller.deploy_from_config = Mock()  # type: ignore

    # We are not in a workspace, so entrypoint should not be allowed
    with pytest.raises(click.ClickException):
        service_controller.deploy(
            "file", None, None, entrypoint=["entrypoint"], is_entrypoint_cmd=False
        )

    with pytest.raises(click.ClickException):
        service_controller.deploy(
            "file", None, None, entrypoint=["entrypoint"], is_entrypoint_cmd=True
        )

    with pytest.raises(click.ClickException):
        service_controller.deploy(
            "file",
            None,
            None,
            entrypoint=["entrypoint", "commands"],
            is_entrypoint_cmd=True,
        )

    # Simulate a workspace
    with patch.dict(
        os.environ, {"ANYSCALE_EXPERIMENTAL_WORKSPACE_ID": "fake_workspace_id"}
    ), patch.multiple(
        "anyscale.controllers.service_controller",
        override_runtime_env_for_local_working_dir=Mock(
            return_value={"rewritten": True}
        ),
    ):
        # Fails due to is_entrypoint_cmd being False
        with pytest.raises(click.ClickException):
            service_controller.deploy(
                "file", None, None, entrypoint=["entrypoint"], is_entrypoint_cmd=False
            )

        mock_config = Mock()
        service_controller.generate_config_from_file.return_value = mock_config
        service_controller.deploy(
            "file", None, None, entrypoint=[], is_entrypoint_cmd=False
        )
        service_controller.generate_config_from_file.assert_called_once_with(
            "file", None, None, healthcheck_url=None
        )
        service_controller.deploy_from_config.assert_called_once_with(mock_config)
        service_controller.generate_config_from_file.reset_mock()
        service_controller.deploy_from_config.reset_mock()

        mock_config = Mock()
        service_controller.generate_config_from_entrypoint.return_value = mock_config
        service_controller.deploy(
            "file", None, None, entrypoint=["entrypoint"], is_entrypoint_cmd=True
        )
        service_controller.generate_config_from_entrypoint.assert_called_once_with(
            ["file", "entrypoint"], None, None, healthcheck_url=None
        )
        service_controller.deploy_from_config.assert_called_once_with(mock_config)


@pytest.mark.parametrize("override_name", [None, "override_service_name"])
@pytest.mark.parametrize("override_version", [None, "override_version"])
@pytest.mark.parametrize("override_canary_weight", [None, 40])
def test_service_rollout(
    mock_auth_api_client,
    override_name: Optional[str],
    override_version: Optional[str],
    override_canary_weight: Optional[int],
) -> None:
    """
    This tests that when we submit a Service config with ray_serve_config,
    we submit both the Service v1 and Service v2 configs.
    Please reference services_internal_api_models.py for more details.
    """
    service_controller = ServiceController()

    name = "test_service_name"
    description = "mock_description"
    ray_serve_config = {"runtime_env": {"pip": ["requests"]}}
    build_id = "test_build_id"
    compute_config_id = "test_compute_config_id"
    project_id = "test_project_id"

    config_dict = {
        "name": name,
        "description": description,
        "ray_serve_config": ray_serve_config,
        "project_id": project_id,
        "build_id": build_id,
        "compute_config_id": compute_config_id,
        "version": "test_abc",
        "canary_weight": 100,
    }
    mock_validate_successful_build = Mock()
    with patch(
        "builtins.open", mock_open(read_data=json.dumps(config_dict))
    ), patch.multiple("os.path", exists=Mock(return_value=True)), patch.multiple(
        "anyscale.controllers.job_controller",
        validate_successful_build=mock_validate_successful_build,
    ):
        service_controller.rollout(
            "test_ser8vice_config_file",
            name=override_name,
            version=override_version,
            canary_percent=override_canary_weight,
        )

    service_v2_config = ApplyProductionServiceV2APIModel(
        name=override_name if override_name else name,
        description=description,
        build_id=build_id,
        compute_config_id=compute_config_id,
        project_id=project_id,
        ray_serve_config=ray_serve_config,
        version=override_version if override_version else "test_abc",
        canary_weight=override_canary_weight if override_canary_weight else 100,
    )

    service_controller.api_client.apply_service_v2_api_v2_services_v2_apply_put.assert_called_once_with(
        service_v2_config
    )
