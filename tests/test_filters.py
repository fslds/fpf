#!/usr/bin/env python

"""Tests for `fpf` filters."""
from fpf import (ExtensionFileFilter, PathSpecWildcardFileFilter,
                 YamlIgnoreFileFilter, YamlPathSpecFilter, UnixHiddenFileFilter, DummyFilter)


def test_simple_extension_filter():
    file_filter = ExtensionFileFilter(['.txt', '.sql'])
    assert not file_filter('test.yml')
    assert not file_filter('test.yaml')
    assert file_filter('test.txt')
    assert file_filter('test.TXT')


def test_simple_extension_filter_with_case():
    file_filter = ExtensionFileFilter(['.txt', '.sql'], ignore_case=False)
    assert not file_filter('test.yml')
    assert not file_filter('bar/test.yaml')
    assert file_filter('test.txt')
    assert not file_filter('test.SQL')


def test_blank_pathspecfile_filter():
    file_filter = PathSpecWildcardFileFilter()
    assert file_filter('test.txt')
    assert file_filter('foo/test2.txt')
    assert file_filter('blah.obj')


def test_simple_pathspecfile_filter():
    file_filter = PathSpecWildcardFileFilter('.*')
    assert file_filter('test.txt')
    assert file_filter('foo/test2.txt')
    assert not file_filter('blah/some/.obj')
    assert not file_filter('.travis.yml')


def test_blank_yaml_pathspec_filter():
    yamlignore_filter = YamlPathSpecFilter()
    assert yamlignore_filter('test.yml')
    assert yamlignore_filter('test.yaml')
    assert not yamlignore_filter('test.txt')


def test_minimal_yaml_pathspec_filter():
    yamlignore_filter = YamlPathSpecFilter('forbidden.yml')
    assert yamlignore_filter('test.yml')
    assert yamlignore_filter('test.yaml')
    assert not yamlignore_filter('test.txt')
    assert not yamlignore_filter('forbidden.yml')


def test_minimal_yamlignore_filter():
    yamlignore_filter = YamlIgnoreFileFilter('tests/.yamlignore')
    assert yamlignore_filter('test.yml')
    assert yamlignore_filter('bar/test.yaml')
    assert yamlignore_filter('bar/foo.YML')
    assert not yamlignore_filter('.travis.yml')
    assert not yamlignore_filter('templates/forbidden.rx.yml')


def test_unix_hidden_file_filter():
    hidden_file_filter = UnixHiddenFileFilter()
    assert not hidden_file_filter('.hidden')
    assert not hidden_file_filter('visible/.hidden.yml')
    assert hidden_file_filter('visible/visible.txt')


def test_dummy_filter():
    dummy_filter = DummyFilter()
    assert dummy_filter('whatever')
