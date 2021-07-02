"""Extensible File Path Filters."""
import ntpath
from typing import Set

import pathspec

from .mixins import FilePathMatchCallableMixin, ReadFileMixin


class PathSpecWildcardFileFilter(FilePathMatchCallableMixin):
    """Filter files based on PathSpec WildMatch (`.gitignore`)."""

    def __init__(self, path_spec_str: str = ''):
        """Create a new path spec wildcard file filter.

        :param path_spec_str: pathspec wildcard paterns. One per line, defaults to ''.
            If you want to ignore all hidden files, a valid pattern would be `.*`
        :type path_spec_str: str, optional
        """
        self._spec = pathspec.PathSpec.from_lines(
            pattern_factory=pathspec.patterns.GitWildMatchPattern,
            lines=path_spec_str.splitlines())

    def _match(self, file_path: str) -> bool:
        """Filter paths based on the pathspec filter.

        :param file_path: a file path or filename.
        :type file_path: str
        :return: True if the filename/path passes the filter, false if not.
        :rtype: bool
        """
        result = not self._spec.match_file(file_path)
        return result


class ExtensionFileFilter(FilePathMatchCallableMixin):
    """Filter files based on a match of the file extensions.

    You can set it to ignore cases. Make sure to start each extension with the dot (`.`)."""

    def __init__(self, extensions: Set[str] = set(), ignore_case: bool = True):
        """Create a new filter based on file extensions.

        :param extensions: File extensions to *whitelist*, defaults to an empty set.
            The extension should start with ``.``.
        :type extensions: Set[str], optional
        :param ignore_case: Ignore extension case (``.exe`` vs ``.EXE``), defaults to True
        :type ignore_case: bool, optional
        """
        if ignore_case:
            extensions = {extension.lower() for extension in extensions}
        self.extensions = extensions
        self.ignore_case = ignore_case

    def _match(self, file_path: str) -> bool:
        basename = ntpath.basename(file_path)
        _, extension = ntpath.splitext(basename)
        if self.ignore_case:
            extension = extension.lower()
        return extension in self.extensions


class YamlPathSpecFilter(ExtensionFileFilter, PathSpecWildcardFileFilter):
    """Filter YAML files (.yml, .yaml) based on pathspec wildcards (gitignore style)."""

    def __init__(self, path_spec_str: str = '', extensions=['.yml', '.yaml'], ignore_extension_case=True):
        """Create a PathSpec Wildcard filter.

        :param path_spec_str: pathsspec multiline string, defaults to ``''`` (no spec)
        :type path_spec_str: str, optional
        :param extensions: YAML file extensions, defaults to ``['.yml', '.yaml']``.
        :type extensions: list, optional
        :param ignore_extension_case: ignore extension cases, defaults to ``True``
        :type ignore_extension_case: bool, optional
        """
        PathSpecWildcardFileFilter.__init__(self, path_spec_str=path_spec_str)
        ExtensionFileFilter.__init__(self, extensions=extensions, ignore_case=ignore_extension_case)

    def _match(self, file_path: str):
        return PathSpecWildcardFileFilter._match(self, file_path) and ExtensionFileFilter._match(self, file_path)


class IgnoreFileFilter(PathSpecWildcardFileFilter, ReadFileMixin):
    """Filter files based on an ignore file like `.gitignore`."""

    def __init__(self, ignore_file_path: str):
        """Create a filter based on an ignore file.

        :param ignore_file_path: path to the ignore file.
        :type ignore_file_path: str
        """
        ignore_file_content = self._read_file(ignore_file_path)
        PathSpecWildcardFileFilter.__init__(
            self,
            path_spec_str=ignore_file_content,
        )


class YamlIgnoreFileFilter(YamlPathSpecFilter, ReadFileMixin):
    """Filter YAML files(`.yml, .yaml`) based on pathspec wildcard file(gitignore style)."""

    def __init__(self, ignore_file_path: str = '.yamlignore', extensions=['.yml', '.yaml'], ignore_extension_case=True):
        """Create a filepath filter based on a ``.yamlignore`` file (similar to a ``.gitignore``).

        :param ignore_file_path: path to the yamlignore file, defaults to ``.yamlignore``
        :type ignore_file_path: str, optional
        :param extensions: Extensions to allow, defaults to ``['.yml', '.yaml']``.
        :type extensions: list, optional
        :param ignore_extension_case: ignore cases of extensions(yml vs YML), defaults to True.
        :type ignore_extension_case: bool, optional
        """
        yaml_ignore_contents = self._read_file(ignore_file_path)
        YamlPathSpecFilter.__init__(
            self,
            path_spec_str=yaml_ignore_contents,
            extensions=extensions,
            ignore_extension_case=ignore_extension_case
        )


class UnixHiddenFileFilter(FilePathMatchCallableMixin):
    """Filter out any hidden files (starting with a .)."""

    def _match(self, file_path: str):
        basename = ntpath.basename(file_path)
        return not basename.startswith('.')


class DummyFilter(FilePathMatchCallableMixin):
    """Do not filter out anything."""

    def _match(self, file_path: str):
        return True


__all__ = [
    'ExtensionFileFilter',
    'IgnoreFileFilter',
    'PathSpecWildcardFileFilter',
    'YamlIgnoreFileFilter',
    'YamlPathSpecFilter',
    'UnixHiddenFileFilter',
    'DummyFilter',
]
