import sys

import click

from .config import default_host, dump_json, make_client
from .entrypoint import cli
from .utils import is_uuid


@cli.group
def repo():
    pass


@repo.command
@click.option(
    "--host",
    "-h",
    type=str,
    default=None,
    help=f"Which GitHost to use - see the output from `weevil host ls`. Will default to using {default_host()}",
)
@click.option(
    "--owner", "-o", type=str, default=None, help="The name of the user or organisation owning the repository"
)
@click.option(
    "--repo",
    "-r",
    "repo",
    type=str,
    default=None,
    help="The name of the repository, or the ID of the repository on Weevils",
)
@click.option(
    "--show-json",
    "-J",
    type=bool,
    is_flag=True,
    default=False,
    help="Show the JSON representation of the repository object",
)
@click.option("--only-id", "-I", type=bool, is_flag=True, default=False, help="Only show the ID of the repository")
def get(host: str, owner: str, repo_name: str, show_json: bool, only_id: bool):
    client = make_client()

    if host is None:
        host = default_host()

    host = client.get_host(host)

    if owner is None and not is_uuid(repo_name):
        click.echo("Must specify either an owner name and repository name as strings, or a repository ID")

    if owner and repo_name:
        repo_obj = host.repository(owner, repo_name)
    else:
        repo_obj = host.repository_by_id(repo_name)

    if only_id:
        click.echo(repo_obj.id)
        sys.exit(0)

    if show_json:
        dump_json(repo_obj)
        sys.exit(0)

    click.echo("hello")
