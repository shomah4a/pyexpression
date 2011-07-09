#-*- coding:utf-8 -*-

import setuptools
from pyexpression import __version__, __author__, __doc__, __license__

version = '0.1.0'

setuptools.setup(
    name='pyexpression',
    version=__version__,
    packages=['pyexpression'],
    install_requires=[
        ],
    author=__author__,
    author_email='shoma.h4a+pypi@gmail.com',
    license=__license__,
    url='https://github.com/shomah4a/pyexpression',
    description='boost.lambda like function generator',
    long_description=__doc__,
    classifiers='''
Programming Language :: Python
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Utilities
'''.strip().splitlines())
