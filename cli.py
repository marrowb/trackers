import click
from cmd.config import config_cli
from cmd.json import json_cli
from cmd.scrape import scrape_cli
from config.settings import load_config

@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['config'] = load_config()

cli.add_command(config_cli)
cli.add_command(json_cli)
cli.add_command(scrape_cli)

if __name__ == '__main__':
    cli(obj={})
