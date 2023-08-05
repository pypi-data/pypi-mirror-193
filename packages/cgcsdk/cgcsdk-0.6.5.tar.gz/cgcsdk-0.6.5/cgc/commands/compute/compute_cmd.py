import json
import click

from cgc.commands.compute.compute_models import EntityList, GPUsList
from cgc.commands.compute.compute_responses import (
    compute_create_filebrowser_response,
    compute_create_response,
    compute_delete_response,
    compute_restart_response,
    compute_list_response,
    template_list_response,
    template_get_start_path_response,
)
from cgc.commands.compute.compute_utills import (
    compute_create_payload,
    compute_delete_payload,
)
from cgc.utils.prepare_headers import get_api_url_and_prepare_headers
from cgc.utils.response_utils import retrieve_and_validate_response_send_metric
from cgc.utils.click_group import CustomGroup, CustomCommand
from cgc.utils.requests_helper import call_api, EndpointTypes


@click.group(name="compute", cls=CustomGroup)
@click.option("--debug", "debug", is_flag=True, default=False, hidden=True)
@click.pass_context
def compute_group(ctx, debug):
    """
    Management of compute resources.
    """
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug


@click.group(name="template", cls=CustomGroup)
def template_group():
    """
    Management of templates.
    """


@template_group.command("list", cls=CustomCommand)
def template_list():
    """Lists all available templates"""
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/list_available_templates"
    metric = "compute.template.list"
    __res = call_api(request=EndpointTypes.get, url=url, headers=headers)
    click.echo(
        template_list_response(
            retrieve_and_validate_response_send_metric(__res, metric)
        )
    )


@template_group.command("get_start_path", cls=CustomCommand)
@click.argument("template", type=click.Choice(EntityList.get_list()))
def template_get_start_path(template: str):
    """Displays start path of specified template"""
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/get_template_start_path?template_name={template}"
    metric = "compute.template.get_start_path"
    __res = call_api(request=EndpointTypes.get, url=url, headers=headers)
    click.echo(
        template_get_start_path_response(
            retrieve_and_validate_response_send_metric(__res, metric)
        )
    )


@click.group(name="filebrowser", cls=CustomGroup)
def filebrowser_group():
    """
    Management of filebrowser.
    """


@filebrowser_group.command("create", cls=CustomCommand)
def compute_filebrowser_create():
    """Create a filebrowser service"""
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/filebrowser_create"
    metric = "compute.create_filebrowser"
    __payload = {"puid": 0, "pgid": 0}
    __res = call_api(
        request=EndpointTypes.post,
        url=url,
        headers=headers,
        data=json.dumps(__payload),
    )
    click.echo(
        compute_create_filebrowser_response(
            retrieve_and_validate_response_send_metric(__res, metric)
        )
    )


@filebrowser_group.command("delete", cls=CustomCommand)
def compute_filebrowser_delete():
    """Delete a filebrowser service"""
    compute_delete("filebrowser")


@compute_group.command("create", cls=CustomCommand)
@click.argument("entity", type=click.Choice(EntityList.get_list()))
@click.option("-n", "--name", "name", type=click.STRING, required=True)
@click.option("-g", "--gpu", "gpu", type=click.INT, default=0)
@click.option(
    "-gt",
    "--gpu-type",
    "gpu_type",
    type=click.Choice(GPUsList.get_list(), case_sensitive=False),
    default="A5000",
)
@click.option("-c", "--cpu", "cpu", type=click.INT, default=1)
@click.option("-m", "--memory", "memory", type=click.INT, default=2)
@click.option("-v", "--volume", "volumes", multiple=True)
def compute_create(
    entity: str,
    gpu: int,
    gpu_type: str,
    cpu: int,
    memory: int,
    volumes: list[str],
    name: str,
):
    """
    Create an app in user namespace.
    \f
    :param entity: name of entity to create
    :type entity: str
    :param gpu: number of gpus to be used by app
    :type gpu: int
    :param cpu: number of cores to be used by app
    :type cpu: int
    :param memory: GB of memory to be used by app
    :type memory: int
    :param volumes: list of volumes to mount
    :type volumes: list[str]
    :param name: name of app
    :type name: str
    """
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/create"
    metric = "compute.create"
    __payload = compute_create_payload(
        name=name,
        entity=entity,
        cpu=cpu,
        memory=memory,
        gpu=gpu,
        volumes=volumes,
        gpu_type=gpu_type,
    )
    __res = call_api(
        request=EndpointTypes.post,
        url=url,
        headers=headers,
        data=json.dumps(__payload),
    )
    click.echo(
        compute_create_response(
            retrieve_and_validate_response_send_metric(__res, metric)
        )
    )


@compute_group.command("delete", cls=CustomCommand)
@click.argument("name", type=click.STRING)
def compute_delete_cmd(name: str):
    """
    Delete an app from user namespace.
    \f
    :param name: name of app to delete
    :type name: str
    """
    compute_delete(name)


def compute_delete(name: str):
    """
    Delete an app using backend endpoint.
    \f
    :param name: name of app to delete
    :type name: str
    """
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/delete"
    metric = "compute.delete"
    __payload = compute_delete_payload(name=name)
    __res = call_api(
        request=EndpointTypes.delete,
        url=url,
        headers=headers,
        data=json.dumps(__payload),
    )
    click.echo(
        compute_delete_response(
            retrieve_and_validate_response_send_metric(__res, metric)
        )
    )


@compute_group.command("list", cls=CustomCommand)
@click.option(
    "-d", "--detailed", "detailed", type=click.BOOL, is_flag=True, default=False
)
@click.pass_context
def compute_list(ctx, detailed):
    """
    List all apps for user namespace.
    """
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/list"
    metric = "compute.list"
    __res = call_api(
        request=EndpointTypes.get,
        url=url,
        headers=headers,
    )
    table = compute_list_response(
        detailed,
        retrieve_and_validate_response_send_metric(__res, metric),
    )

    click.echo(table)


@compute_group.command("restart", cls=CustomCommand)
@click.argument("name", type=click.STRING)
def compute_restart(name: str):
    """Restarts the specified app"""
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/restart"
    metric = "compute.restart"
    __payload = {"name": name}
    __res = call_api(
        request=EndpointTypes.post,
        url=url,
        headers=headers,
        data=json.dumps(__payload),
    )
    click.echo(
        compute_restart_response(
            retrieve_and_validate_response_send_metric(__res, metric)
        )
    )


compute_group.add_command(filebrowser_group)
compute_group.add_command(template_group)
