"""Simple implementations  """

import os

from typing import Generator, Callable


def get_filename_list_from_directory(
        folder: str,
        filename_filter: Callable[[str], bool],
        relative_paths=True) -> Generator[str, None, None]:
    """Yield yml filenames in a directory.

    :param folder: folder path
    :type folder: str
    :return: list of YAML file names
    :rtype: list
    """
    for root, subdirs, files in os.walk(folder):
        for file in files:
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, start=folder)
            if filename_filter(rel_path):
                if relative_paths:
                    yield rel_path
                else:
                    yield abs_path
            else:
                # print('NOPE', rel_path)
                pass
