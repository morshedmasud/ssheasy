import click
from ssh_easy import ssheasy


@click.group()
def cli():
    """ Main CLI Function """


@cli.command(help="To see current SSH kay with 'ssheasy current'")
def current():
    return ssheasy.get_current()


@cli.command('list', help="To see all SSH kay list with 'ssheasy list'")
def key_list():
    """ All SSH Key """
    return ssheasy.get_list()


@cli.command(help="SSH key backup 'ssheasy backup {current_key_name}'")
@click.argument('name')
def backup(name):
    """ Backup a Key """
    return ssheasy.backup_key(name)


@cli.command(help="Create new SSH key pair with 'ssheasy new {new_ssh_name}'")
@click.argument('name')
def new(name):
    """ Create a New SSH Key """
    return ssheasy.new_key(name)


@cli.command(help="To Rename a ssh key pair with 'ssheasy rename {old_key} {new_key}'")
@click.argument('old_key_name')
@click.argument('new_key_name')
def rename(old_key_name, new_key_name):
    """ Rename a Key """
    return ssheasy.rename_key(old_key_name, new_key_name)


@cli.command(help="To delete specific kay with 'ssheasy delete {name}'")
@click.argument('name')
def delete(name):
    """ Delete a Key """
    return ssheasy.delete_key(name)


@cli.command(help="To switch RSH pair key 'ssheasy delete {name}'")
@click.argument('name')
def switch(name):
    """ Delete a Key """
    return ssheasy.switch_key(name)


def start():
    cli(obj={})


if __name__ == '__main__':
    start()
