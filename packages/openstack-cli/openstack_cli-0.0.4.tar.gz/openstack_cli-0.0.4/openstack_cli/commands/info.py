import click


@click.command(help="show doc about openstack")
def cli():
    click.echo_via_pager(
        """
=========
openstack
=========

openstack is a poilerplate Python that encourages rapid development
and clean, pragmatic design. and we're support templates to your field
what ever you want. Thanks for checking it out.

All documentation is in the "``docs``" directory and online at
https://openstack_cli.sh/docs/en/. If you're just getting started,
here's how we recommend you read the docs:

* First, read ``https://openstack_cli.sh/docs/en/install.txt`` for instructions on installing openstack_cli.

* Next, work through the tutorials in order (``https://openstack_cli.sh/docs/en/intro/tutorial01.txt``,
  ``https://openstack_cli.sh/docs/en/intro/tutorial02.txt``, etc.).


Docs are updated rigorously. If you find any problems in the docs, or think
they should be clarified in any way, please take 30 seconds to fill out a
ticket here: https://openstack_cli.sh/code/newticket

        """
    )
