from __future__ import absolute_import, unicode_literals

import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-Webtouch',
    version=get_version('mopidy_webtouch/__init__.py'),
    url='https://github.com/roosnic1/mopidy-webtouch',
    license='Apache License, Version 2.0',
    author='Nicolas Koki Roos',
    author_email='nicolas.k.roos@gmail.com',
    description='Webclient for small touchscreens',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 2.0.0',
        'Pykka >= 1.2.1',
    ],
    entry_points={
        'mopidy.ext': [
            'webtouch = mopidy_webtouch:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)