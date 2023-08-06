import sys
from typing import List, Optional

import click

from anyscale.cli_logger import BlockLogger
from anyscale.controllers.service_controller import ServiceController
from anyscale.util import validate_non_negative_arg


log = BlockLogger()  # CLI Logger


@click.group(
    "service", help="Interact with production services running on Anyscale.",
)
def service_cli() -> None:
    pass


@service_cli.command(name="deploy", help="Deploy a service to Anyscale.")
@click.argument("service-config-file", required=True)
@click.option("--name", "-n", required=False, default=None, help="Name of service.")
@click.option(
    "--description", required=False, default=None, help="Description of service."
)
@click.option(
    "--healthcheck-url", required=False, help="Healthcheck URL for Service.",
)
@click.argument(
    "entrypoint", required=False, nargs=-1,
)
def deploy(
    service_config_file: str,
    entrypoint: List[str],
    name: Optional[str],
    description: Optional[str],
    healthcheck_url: Optional[str],
) -> None:
    # TODO[Bruce]: Remove update flag once fully test apply function.
    service_controller = ServiceController()
    service_controller.deploy(
        service_config_file,
        name=name,
        description=description,
        healthcheck_url=healthcheck_url,
        entrypoint=entrypoint,
        is_entrypoint_cmd="--" in sys.argv,
    )


@service_cli.command(
    name="rollout",
    help="Rollout a Service v2 to Anyscale. Please contact support for details.",
)
@click.option(
    "-f",
    "--service_config_file",
    required=True,
    help="The path of the service configuration file.",
)
@click.option("--name", "-n", required=False, default=None, help="Name of service.")
@click.option("--version", required=False, default=None, help="Version of service.")
@click.option(
    "--canary-percent",
    required=False,
    default=None,
    type=int,
    help="The percentage of traffic going to the new version of Service that you are deploying",
)
def rollout(
    service_config_file: str,
    name: Optional[str],
    version: Optional[str],
    canary_percent: Optional[int],
) -> None:
    service_controller = ServiceController()
    service_controller.rollout(
        service_config_file, name=name, version=version, canary_percent=canary_percent
    )


@service_cli.command(name="list", help="Display information about existing services.")
@click.option(
    "--name", "-n", required=False, default=None, help="Filter by service name."
)
@click.option(
    "--service-id", "--id", required=False, default=None, help="Filter by service id."
)
@click.option(
    "--project-id", required=False, default=None, help="Filter by project id."
)
@click.option(
    "--include-all-users",
    is_flag=True,
    default=False,
    help="Include services not created by current user.",
)
@click.option(
    "--include-archived",
    is_flag=True,
    default=False,
    help=(
        "List archived services as well as unarchived services."
        "If not provided, defaults to listing only unarchived services."
    ),
)
@click.option(
    "--max-items",
    required=False,
    default=10,
    type=int,
    help="Max items to show in list.",
    callback=validate_non_negative_arg,
)
def list(  # noqa: A001, PLR0913
    name: Optional[str],
    service_id: Optional[str],
    project_id: Optional[str],
    include_all_users: bool,
    include_archived: bool,
    max_items: int,
) -> None:
    service_controller = ServiceController()
    service_controller.list(
        name=name,
        service_id=service_id,
        project_id=project_id,
        include_all_users=include_all_users,
        include_archived=include_archived,
        max_items=max_items,
    )


@service_cli.command(name="archive", help="Archive a service.")
@click.option("--service-id", "--id", required=False, help="Id of service.")
@click.option("--name", "-n", required=False, help="Name of service.")
def archive(service_id: Optional[str], name: Optional[str]) -> None:
    service_controller = ServiceController()
    service_controller.archive(service_id=service_id, service_name=name)


@service_cli.command(
    name="rollback", help="Attempt to rollback a service asynchronously."
)
@click.option("--service-id", "--id", required=True, help="Id of service.")
def rollback(service_id: str) -> None:
    # TODO (kamenshah)
    # Add service_name and service_config_file as arguments
    # If service_id is None then derive id from service_name or service_config_file
    service_controller = ServiceController()
    service_controller.rollback(service_id=service_id,)


@service_cli.command(
    name="terminate", help="Attempt to terminate a service asynchronously."
)
@click.option("--service-id", "--id", required=False, help="Id of service.")
@click.option("--name", "-n", required=False, help="Name of service.")
def service(service_id: Optional[str], name: Optional[str]) -> None:
    service_controller = ServiceController()
    service_controller.terminate(service_id=service_id, service_name=name)
