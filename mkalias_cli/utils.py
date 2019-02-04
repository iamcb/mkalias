import os

import osascript


def check_path(source, destination):
    """
    Check if source directory/file and destination directory exists
    :param source: Source directory or file
    :param destination: Destination directory
    :return: False if directory/file is not found, otherwise returns true
    """
    path_exists = True
    source = os.path.abspath(source)
    destination_head, destination_tail = os.path.split(destination)

    def print_not_found_error(location):
        print("Error '{}' not found!".format(location))

    if not os.path.isdir(source):
        print_not_found_error(source)
        path_exists = False
    elif not os.path.isdir(destination_head):
        print_not_found_error(destination_head)
        path_exists = False
    elif not os.path.isfile(source):
        print_not_found_error(source)
        path_exists = False

    if path_exists:
        print("Source Dir - '{}'".format(source))
        print("Destination Dir - '{}'".format(destination))

    return path_exists


def create_alias(source, destination):
    command_string = 'tell application "Finder" to make alias file to POSIX file "{}" at POSIX file "{}"' \
        .format(source, destination)

    code, out, error = osascript.run(command_string)

    print(command_string)
    print(code)
    print(out)
    print(error)


def rename_alias(source, destination, name):
    """
    Rename the new alias to a custom name instead of "example alias"

    :param name: custom name of new alias
    :param source: Name of the source file/dir for the alias
    :param destination: destination for the alias
    :return: none
    """

    source_head, source_tail = os.path.split(source)

    alias_name = source_tail + " alias"
    alias_path = destination + "/" + alias_name
    new_name_path = destination + "/" + name

    os.rename(alias_path, new_name_path)
    print(new_name_path)
