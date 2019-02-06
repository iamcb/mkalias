#!/usr/bin/env python3
"""
    mkalias.py - CLI app to create finder aliases.

"""

import argparse
import os
import sys
import logging

from setuptools_scm import get_version

import utils
import strings

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

version = get_version()


def parse_args():
    """
    Function to setup and hold argument parser
    :return: parser.parse_args() object -
    """
    parser = argparse.ArgumentParser(prog='mkalias',
                                     description='Application to create Finder aliases from the command line')

    parser.add_argument('source', help='Source to create alias from')
    parser.add_argument('destination', help='Destination directory of alias')
    parser.add_argument('-n', dest='alias_name', metavar="Name", help='Set the name of the new alias')
    parser.add_argument('--version', action='version', version='%(prog)s v{}'.format(version),
                        help='Display version info')

    return parser.parse_args()


def main():
    args = parse_args()

    source = os.path.abspath(args.source)
    destination = os.path.abspath(args.destination)

    if not utils.Path.check_path(source):
        logger.error(strings.PATH_NOT_FOUND.format(source))
        sys.exit(1)
    elif not utils.Path.check_path(destination):
        logger.error(strings.PATH_NOT_FOUND.format(destination))
        sys.exit(1)

    create_alias_output = utils.Alias.create_alias(source, destination)

    print(create_alias_output[utils.Alias.CMD_STRING])
    print(create_alias_output[utils.Alias.CODE])
    print(create_alias_output[utils.Alias.OUT])
    print(create_alias_output[utils.Alias.ERROR])

    if args.alias_name:
        utils.Alias.rename_alias(source, destination, args.alias_name)

    logging.shutdown()
    sys.exit(0)  # exit gracefully


if __name__ == "__main__":
    main()
