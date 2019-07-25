#!/usr/bin/env python3
"""
    mkalias.py - CLI app to create finder aliases.
"""
import logging
import os
import sys

import click

from .alias import Alias
from .version import version


def init_logging(verbose, logger=logging.getLogger(__name__)):
    # Setup logger
    logger.setLevel(logging.DEBUG)

    # setup Logging Handlers
    log_console_handler = logging.StreamHandler()
    if verbose:
        log_console_handler.setLevel(logging.DEBUG)  # Verbose/Debug output
    else:
        log_console_handler.setLevel(logging.INFO)  # Normal Output

    # setup Logging Formatters
    log_console_format = logging.Formatter('%(levelname)s: \n %(message)s')
    log_console_handler.setFormatter(log_console_format)
    # add handler to the logger
    logger.addHandler(log_console_handler)

    return logger


@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('destination', type=click.Path(exists=True))
@click.option('--name', '-n', help='Set the name of the new alias')
@click.option('--verbose', '-v', is_flag=True, help='Output all app info for testing/troubleshooting')
@click.version_option(version=version)
def main(source, destination, verbose, name=None, ):
    log = init_logging(verbose)

    log.debug('Source: "{}" \n'
              ' Destination: "{}"'.format(source, destination))

    source_path = os.path.abspath(source)
    destination_path = os.path.abspath(destination)

    log.info('Source Path: "{}" \n'
             ' Destination Path: "{}"'.format(source_path, destination_path))

    # Create the Alias
    alias_output = Alias.create(source_path, destination_path, name)

    log.info('Command String: "' + str(alias_output[Alias.CMD_STRING]) + '"')
    log.debug('osascript Exit Code: "' + str(alias_output[Alias.CODE]) + '"')
    log.debug('osascript Output: "' + str(alias_output[Alias.OUT]) + '"')
    log.debug('osascript Error: "' + str(alias_output[Alias.ERROR]) + '"')

    logging.shutdown()
    sys.exit(0)  # exit gracefully


if __name__ == "__main__":
    main()
