#!/usr/bin/env python

"""Tests for `fpf` filter function."""

from fpf import fpf, file_path_filter, filter_file_paths


def test_fpf_import_simple():
    test_fnc = fpf
    assert test_fnc
    assert hasattr(fpf, '__call__')


def test_file_path_filter_import_simple():
    test_fnc = file_path_filter
    assert test_fnc
    assert hasattr(fpf, '__call__')


def test_filter_file_paths_import_simple():
    test_fnc = filter_file_paths
    assert test_fnc
    assert hasattr(fpf, '__call__')
