#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-02-09
"""

from setuptools import setup

setup(
    name='docsetviz',
    version='1.1',
    description='Docset Visualization Tool',
    author='yanaenen',
    install_requires=[
        'docset',
        'numpy',
        'opencv-python',
        'paramiko',
        'PyQt5',
    ],
    package_dir={'docsetviz': '.'},
    entry_points={
        'console_scripts': [
            'docsetviz = docsetviz.main:main'
        ]
    },
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    zip_safe=False,
)
