#!/usr/bin/env python3
"""
    mkalias.py - CLI app to create finder aliases.

"""

import argparse
import os

import utils
from setuptools_scm import get_version

version = get_version()


def parse_args():
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

    utils.check_path(source, destination)

    utils.create_alias(source, destination)

    if args.alias_name:
        utils.rename_alias(source, destination, args.alias_name)


if __name__ == "__main__":
    main()
