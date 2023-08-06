import click

from merph.app import make_dashboard


@click.command()
def run_app():
    make_dashboard()
