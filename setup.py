# coding: utf-8
from setuptools import setup, find_packages
from dbf2csv import __version__

setup(
    name='dbf2csv',
    version=__version__,
    url='https://github.com/akadan47/dbf2csv',
    description='Small utility to convert simple *.DBF files to *.CSV',
    packages=find_packages(),
    platforms='any',
    entry_points={
        'console_scripts': [
            'dbf2csv = dbf2csv.main:main',
        ],
    },
    install_requires=[
        'dbfread==2.0.6'
    ]
)
