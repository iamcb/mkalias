#!/usr/bin/env python3
"""
    mkalias.py - CLI app to create finder aliases.
"""
import click
import logging
import os
import sys

from .version import version
from .alias import Alias

# Setup Logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

log.addHandler(ch)


@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('destination', type=click.Path(exists=True))
@click.option('--name', '-n', help='Set the name of the new alias')
@click.version_option(version=version)
def main(source, destination, name=None):
    log.debug('Source: {} \n'
              'Destination: {}'.format(source, destination))

    source_path = os.path.abspath(source)
    destination_path = os.path.abspath(destination)

    log.debug('Source Path: {} \n'
              'Destination Path: {}'.format(source_path, destination_path))

    # Create the Alias
    alias_output = Alias.create(source_path, destination_path, name)

    log.info(alias_output[Alias.CMD_STRING])
    # log.debug(alias_output[Alias.CODE])
    log.debug(alias_output[Alias.OUT])
    log.error(alias_output[Alias.ERROR])

    logging.shutdown()
    sys.exit(0)  # exit gracefully


if __name__ == "__main__":
    main()
