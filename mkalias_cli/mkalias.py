#!/usr/bin/env python3
"""
    mkalias.py - CLI app to create finder aliases.

"""

import argparse
import logging
import os
import sys

from setuptools_scm import get_version

<<<<<<< HEAD
import strings
import utils

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

=======
from mkalias_cli import strings

#  Get version info
>>>>>>> develop
version = get_version()

# Setup Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger.addHandler(ch)


def parse_args():
    """
<<<<<<< HEAD
    Function to setup and hold argument parser
=======
    Function to setup argument parser
>>>>>>> develop
    :return: parser.parse_args() object
    """
    parser = argparse.ArgumentParser(prog='mkalias',
                                     description='Application to create Finder aliases from the command line')

    parser.add_argument('source', help='Source to create alias from')
    parser.add_argument('destination', help='Destination directory of alias')
    parser.add_argument('-n', dest='alias_name', metavar="Name", help='Set the name of the new alias')
    parser.add_argument('--version', action='version', version='%(prog)s v{}'.format(version),
                        help='Display version info')

    return parser.parse_args()


<<<<<<< HEAD
=======
class Alias:
    #  Constants used for this Class
    CMD_STRING = 0
    CODE = 1
    OUT = 2
    ERROR = 3

    @staticmethod
    def create_alias(source, destination, name=None) -> tuple:
        """
        Creates and runs the AppleScript required to create the alias
        :param source: File or Directory to create an alias of
        :param destination: Destination directory of the new alias
        :param name: Name of new alias - OPTIONAL
        :return: tuple containing the AppleScript Created, Code, Output of AppleScript, and Errors - in that order
        """

        if name is None:
            cmd_string = 'tell application "Finder" to make alias file to POSIX file "{}" at POSIX file "{}"' \
                .format(source, destination)
        else:
            cmd_string = 'tell application "Finder" to make alias file to POSIX file "{}" at POSIX file "{}"' \
                         ' with properties {{name:"{}"}}'.format(source, destination, name)

        code, out, error = osascript.run(cmd_string)

        return cmd_string, code, out, error


>>>>>>> develop
def main():
    args = parse_args()

    source = os.path.abspath(args.source)
    destination = os.path.abspath(args.destination)

<<<<<<< HEAD
    #  TODO: Check for symbolic / hard links
    if not utils.Path.check_path(source):
        logger.error(strings.PATH_NOT_FOUND.format(source))
        sys.exit(1)
    elif not utils.Path.check_path(destination):
        logger.error(strings.PATH_NOT_FOUND.format(destination))
        sys.exit(1)

    #  TODO: Make this better?
    create_alias_output = utils.Alias.create_alias(source, destination)

    logger.log("INFO", create_alias_output[utils.Alias.CMD_STRING])
    logger.log("DEBUG", create_alias_output[utils.Alias.CODE])
    logger.log("DEBUG", create_alias_output[utils.Alias.OUT])
    logger.log("ERROR", create_alias_output[utils.Alias.ERROR])
=======
    #  TODO: Check for symbolic / hard links if necessary
    if not os.path.exists(source):
        logger.error(strings.PATH_NOT_FOUND.format(source))
        sys.exit(1)
    elif not os.path.exists(destination):
        logger.error(strings.PATH_NOT_FOUND.format(destination))
        sys.exit(1)
>>>>>>> develop

    #  TODO: Is there a better way to rename the alias?
    if args.alias_name:
<<<<<<< HEAD
        utils.Alias.rename_alias(source, destination, args.alias_name)
=======
        create_alias_output = Alias.create_alias(source, destination, args.alias_name)
    else:
        create_alias_output = Alias.create_alias(source, destination)

    logger.info(create_alias_output[Alias.CMD_STRING])
    logger.debug(create_alias_output[Alias.CODE])
    logger.debug(create_alias_output[Alias.OUT])
    logger.error(create_alias_output[Alias.ERROR])
>>>>>>> develop

    logging.shutdown()
    sys.exit(0)  # exit gracefully


if __name__ == "__main__":
    main()
