#!/usr/bin/env python
#coding: utf-8
from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

import sys

try:
    from importlib import reload
except ImportError:
    pass
reload(sys)

try:
    sys.setdefaultencoding('utf8')
except AttributeError:
    # data that is already encoded in Python 3
    pass

setup(
    name='django-robokassa',
    version='1.2.3',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['robokassa'],

    url='https://bitbucket.org/kmike/django-robokassa/',
    license = 'MIT license',
    description = 'Приложение для интеграции платежной системы ROBOKASSA в проекты на Django.'.encode('utf8'),
    long_description = '',

    requires=['django (>= 1.3)'],

    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
