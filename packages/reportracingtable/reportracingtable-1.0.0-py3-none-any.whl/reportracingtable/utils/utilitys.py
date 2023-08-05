import os
from typing import Dict, List

from .exceptions import CustomFileNotFoundException


def import_folder(folder_path: str) -> Dict[str, str]:
    """Reading folder and make full path to the files"""
    if not os.path.exists(folder_path):
        raise CustomFileNotFoundException(
            f"No such file or directory: '{folder_path}'"
        )
    files_full_path = {}
    for _, __, log_files in os.walk(folder_path):
        for file in log_files:
            full_path = folder_path + '/' + file
            files_full_path[file[:-4]] = full_path
    return files_full_path


def read_file(file_path: str) -> List[str]:
    """Reading and preparing file before well be used by function"""
    if not os.path.exists(file_path):
        raise CustomFileNotFoundException(
            f"No such file or directory: '{file_path}'"
        )
    with open(file_path) as file:
        return [line.strip("\n") for line in file.readlines()]
