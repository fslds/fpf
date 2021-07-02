"""Simple FPF implementations

Example usage with a simple function filter:

.. code-block:: python

    from fpf import filter_file_paths

    def filter1(file_path):
    '''Filter out all files not ending with `.yml`'''
        return file_path.endswith('.yml')


    list(filter_file_paths(root_dir='.', path_filter=filter1))

Example usage with an `fpf` filter:

.. code-block:: python

    from fpf import filter_file_paths, YamlIgnoreFilter

    # Read pathspec from `.myproject-yaml-ignore-file` and only include yml files.
    filter2 = YamlIgnoreFilter('.myproject-yaml-ignore-file')
    list(filter_file_paths(root_dir='.', path_filter=filter2))

"""

import os
from typing import Callable, Generator
from .filters import DummyFilter


def file_path_filter(
        root_dir: str,
        path_filter: Callable[[str], bool] = DummyFilter(),
        relative_paths=True) -> Generator[str, None, None]:
    """Filter file paths/names relative to the root based on a filter.

    :param root_dir: root directory to filter through.
    :type root_dir: str
    :param path_filter: A filter function. Returns false for files/paths that should be excluded.
    :type path_filter: Callable[[str], bool]
    :param relative_paths: return relative paths to the root dir,
        alternative is full absolute paths on the file system, defaults to True.
    :type relative_paths: bool, optional
    :yield: file path/name that passes the filter.
    :rtype: Generator[str, None, None]
    """
    for root, subdirs, files in os.walk(root_dir):
        for file in files:
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, start=root_dir)
            if path_filter(rel_path):
                if relative_paths:
                    yield rel_path
                else:
                    yield abs_path


# Add some aliases for the function
filter_file_paths = file_path_filter
fpf = file_path_filter  # shortcut for the function

__all__ = ['file_path_filter', 'filter_file_paths', 'fpf']
