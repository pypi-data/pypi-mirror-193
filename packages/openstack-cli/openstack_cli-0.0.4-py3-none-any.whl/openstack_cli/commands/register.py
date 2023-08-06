import click


@click.command(help="Register to openstack_cli.sh website")
def cli():
    click.launch("https://openstack_cli.sh/register/")
