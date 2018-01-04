import subprocess

import click


@click.command()
@click.argument('name', default='nick')
@click.argument('path', default='snakeeyes')
def cli(name, path):
    """
    Say hello to someone

    :param name: name placeholder
    :param path: Test coverage path
    :return: Subprocess call result
    """
    cmd = 'echo hello {1}'.format(path, name)
    return subprocess.call(cmd, shell=True)
