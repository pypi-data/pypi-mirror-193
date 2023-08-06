import click


@click.group()
@click.version_option()
def cli():
    "Use AI to automatically fix bugs"


@cli.command(name="command")
@click.argument(
    "example"
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
