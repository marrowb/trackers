import click
from utils.json_utils import load_json, save_json

@click.group()
@click.pass_context
def json_cli():
    pass

@json_cli.command()
@click.pass_context
@click.option("--name", prompt='Enter the name of the dataset', type=str)
@click.option('--url', prompt='Enter the URL')
@click.option('--selector', prompt='Enter the HTML selector (tag, id, or class)')
def add(name, url, selector):
    """Add a new link and its HTML selector to the JSON file."""
    config = ctx.obj['config']
    data = load_json(config['JSON_FILE_PATH'])
    data['links'].append({"name":name, 'url': url, 'selector': selector})
    save_json(JSON_FILE_PATH, data)
    click.echo(f'Added URL: {url} with selector: {selector}')
