import subprocess

import click


@click.command()
@click.option('--name', default=False, help='enter a name, dummy')
@click.argument('path', default='snakeeyes')
def cli(name, path):
    """
    Say hello to someone

    :param name: name placeholder
    :param path: Test coverage path
    :return: Subprocess call result
    """
    hello_flag_exclude = ''

    if name:
      hello_flag_exclude = name

    cmd = 'echo hello {1}'.format(path, name)
    return subprocess.call(cmd, shell=True)
