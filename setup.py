#!/usr/bin/env python

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ttt-lib',
    version='0.1.0',
    description='Tic Tac Toe Library',
    long_description=long_description,
    url='https://github.com/c17r/ttt-lib',
    author='Christian Sauer',
    author_email='sauerc@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    py_modules=[
        'ttt',
    ],
    tests_require=[
        'pytest',
        'pytest-conv'
    ]
)
