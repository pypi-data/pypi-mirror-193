import click

from .config import dump_json, make_client
from .entrypoint import cli
from .utils import is_uuid


@cli.group
def job():
    pass


@job.command
@click.argument("job_id", type=str, default=None)
@click.option("--show-json", "-J", type=bool, is_flag=True, default=False)
@click.option("--output", "-o", type=bool, is_flag=True, default=False)
def get(job_id: str, show_json: bool, output: bool):
    client = make_client()

    if not is_uuid(job_id):
        raise ValueError

    job_obj = client.get_job(job_id)

    if output:
        click.echo(job_obj.output)
    elif show_json:
        dump_json(job_obj)
    else:
        click.echo(
            f"{job_obj.repository.host.name}: "
            f"{job_obj.repository.owner.name}/{job_obj.repository.name} #{job_obj.number}\n"
        )
        click.echo(f"{job_obj.status}\n")
        click.echo(job_obj.output)
