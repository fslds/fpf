"""Extensible File Path Filtering."""


from .filters import (  # noqa: F401
    ExtensionFileFilter,
    IgnoreFileFilter,
    PathSpecWildcardFileFilter,
    YamlIgnoreFileFilter,
    YamlPathSpecFilter,
    UnixHiddenFileFilter,
    DummyFilter)
from .fpf import fpf, file_path_filter, filter_file_paths  # noqa: F401

__VERSION__ = '0.1.3'
__all__ = [
    'fpf',
    'file_path_filter',
    'filter_file_paths',
    'ExtensionFileFilter',
    'IgnoreFileFilter',
    'PathSpecWildcardFileFilter',
    'YamlIgnoreFileFilter',
    'YamlPathSpecFilter',
    'UnixHiddenFileFilter',
    'DummyFilter'
]
