"""Additional mixins for File Path Filters."""

from abc import ABC, abstractmethod

from .logger import logger


class FilePathMatchCallableMixin(ABC):
    """Make a class callable if the implement a match function with the same signature."""

    def match(self, file_path: str) -> bool:
        """Match filenames with the filter.

        :param file_path: A file path
        :type file_path: str
        :return: True if the file passes all filters, False if it is set to be filtered.
        :rtype: bool
        """
        return self._match(file_path)

    @abstractmethod
    def _match(self, file_path: str) -> bool:
        pass

    def __call__(self, file_path: str) -> bool:
        """Make the object Callable, in this case the object will behave like the `match` function.

        Refer to the  `match` abstract function that needs to be implemented by inherinting classes.
        """
        return self.match(file_path)


class ReadFileMixin:
    """Add pathspec File reading capabilities to a class."""

    def _read_file(self, file_path: str):
        ignore_file_content: str = ''
        try:
            with open(file_path) as yaml_ignore_file:
                ignore_file_content = yaml_ignore_file.read()
        except FileNotFoundError as fnf:
            logger.warning(f'No file found at {file_path} - {type(fnf)}: {fnf}')
        finally:
            return ignore_file_content
