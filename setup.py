#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    description = f.read()

setup(
    name='cinch',
    version='0.3.0',
    description='Cinch continuous integration setup',
    long_description=description,
    url='https://github.com/RedHatQE/cinch',
    author='RedHatQE',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='continuous integration, ci, jenkins',
    packages=find_packages(exclude=('library', 'bin')),
    include_package_data=True,
    install_requires=[
        'ansible>=2.1',
        'plumbum>=1.6.0',
        'linchpin>=0.8.2',
        'sphinx_rtd_theme'
    ],
    entry_points={
        'console_scripts': [
            'cinch=cinch.bin.entry_point:cinch',
            'cinchpin=cinch.bin.entry_point:cinchpin'
        ]
    },
    extras_require={
        'lint': [
            'flake8'
        ]
    }
)
