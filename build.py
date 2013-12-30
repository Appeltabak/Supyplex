#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pynt import task
from subprocess import call


def _run(command):
    """ Run command.

    :param command:     A string with 1 or more commands.

    """
    return call(command.split(' '))


@task()
def tests(coverage=False):
    """ Run unit tests. """
    if coverage:
        _run('coverage run --source app -m py.test test/ -vv')
        _run('coverage report -m')
    else:
        _run('py.test test/ -vv')


@task()
def build_doc():
    """ Build documentation with Sphinx. """
    os.chdir('docs/')
    _run('make html')


@task()
def run(env='prod'):
    """ Run Supyplex. """
    os.environ['SUPYPLEX_ENV'] = env
    _run('./supyplex.py')


__DEFAULT__ = run
""" Default action when pynt is run without parameter. """
