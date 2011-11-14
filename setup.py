#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from cmsplugin_disqus import __version__


INSTALL_REQUIRES = [
    'django-cms>=2.2',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='cmsplugin-disqus',
    version=__version__,
    description='Disqus plugin for django CMS',
    author='Djeese Factory GmbH',
    author_email='say@djee.se',
    url='https://github.com/djeese/cmsplugin-disqus',
    packages=['cmsplugin_disqus', 'cmsplugin_disqus.migrations'],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False
)
