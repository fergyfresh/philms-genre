#!/usr/bin/env python
from setuptools import setup

with open('requirements.txt') as f:
    requirements = [i for i in f.read().splitlines()

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, '__init__.py'), 'rb') as init_py:
        src = init_py.read().decode('utf-8')
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", src).group(1)


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
    long_description=read('README.rst'),
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
