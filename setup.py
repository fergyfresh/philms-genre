#!/usr/bin/env python
import os
import re

from setuptools import setup

with open('requirements.txt') as f:
    requirements = [i for i in f.read().splitlines()]

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, '__init__.py'), 'rb') as init_py:
        src = init_py.read().decode('utf-8')
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", src).group(1)


def read(*paths):
    """
    Build a file path from paths and return the contents.
    """
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]
    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


name = 'philms-genre'
version = get_version('philms_genre')
package = 'philms_genre'
description = 'Multi purpose movie genre scraper in python'
url = 'https://github.com/fergyfresh/philms-genre'
author = 'Billy Ferguson'
author_email = 'william.d.ferg@gmail.com'
license = 'MIT'


setup(
    name=name,
    version=version,
    url=url,
    license=license,
    description=description,
    long_description=read('README.md'),
    author=author,
    author_email=author_email,
    packages=get_packages(package),
    package_data=get_package_data(package),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: WTFPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
