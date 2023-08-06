# Copyright 2016 to 2021, Cisco Systems, Inc., all rights reserved.
# Discover and run doctests, report results alongside other unittest results.

from doctest import DocTestSuite
from unittest import TestSuite


def yangsuite_module(name):
    """Construct a module name relative to __name__."""
    return '.'.join(__name__.split('.')[:-2] +
                    [name])


storage = None


def clear_registered_paths(doctest):
    """Cache the paths registered in yangsuite.paths and clear the registry."""
    global storage
    storage = doctest.globs['_paths'].copy()
    doctest.globs['_paths'].clear()


def restore_registered_paths(doctest):
    """Restore the cached paths registry."""
    global storage
    doctest.globs['_paths'].update(storage)


def load_tests(*args):
    """Wrap module doctests into a unittest TestSuite.

    Called automatically by unittest.
    """
    suite = TestSuite()
    suite.addTests(DocTestSuite(yangsuite_module('paths'),
                                setUp=clear_registered_paths,
                                tearDown=restore_registered_paths))
    suite.addTests(DocTestSuite(yangsuite_module('logs')))
    return suite
