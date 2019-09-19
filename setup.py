#!/usr/bin/env python
import os
import re
import sys

from setuptools import setup, find_packages

classes = """
    Development Status :: 4 - Beta
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Topic :: System :: Distributed Computing
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Operating System :: OS Independent
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

setup(
    name='ceph-info',
    version="0.1",
    description='ds starsan',
    author='Mher',
    author_email='mher.movsisyan@gmail.com',
    url='https://github.com/',
    license='BSD',
    classifiers=classifiers,
    keywords='ceph_info',
    packages=find_packages(exclude=[]),

)