from argparse import ArgumentParser, Namespace
from typing import List, Union

from ..utils.exceptions import (CommandLineArgumentsException,
                                CustomTypeErrorException)
from ..utils.functions import print_report


def main() -> Union[List[int], int]:
    """
    Function for parsing command line arguments
    """
    parser = ArgumentParser(description="Function for parsing command line strings")
    parser.add_argument("--driver", help="string value rider name as args")
    parser.add_argument("--folder", help="folder_path as args")
    parser.add_argument("--desc", help="sort by desc as args")
    namespace_args = parser.parse_args()
    return execution_func_with_arguments(namespace_args)


def execution_func_with_arguments(namespace_args: Namespace):
    """
    Argument "--folder" is required
    If "--driver" and "--desc" arguments was passed - only "--driver" will be executed
    """
    if not isinstance(namespace_args, Namespace):
        raise CustomTypeErrorException(
            f"Wrong data type {type(namespace_args)}, must be a {Namespace}"
        )
    folder, driver, desc = namespace_args.folder, namespace_args.driver, namespace_args.desc
    if not folder:
        raise CommandLineArgumentsException(
            f"Required argument '--folder' is missing"
        )
    if driver or (driver and desc):
        return print_report(folder, rider_name=driver)
    elif desc:
        return print_report(folder, desc=desc)
    return print_report(folder)
