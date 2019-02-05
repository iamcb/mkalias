import os

import osascript


def check_path(path):
    """
    Check if file or directory path is valid
    :param path: path to check
    :return: true if path exists otherwise returns false
    """

    not_found_msg = "Error '{}' not found!"

    if os.path.exists(path):
        return True
    else:
        print(not_found_msg.format(path))
        return False


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
