"""
The installation module of the package.

-----

:authors: notjik
:license: MIT License
:copyright: (c) 2023 notjik
"""
import os

from setuptools import setup, find_packages

version = '0.1.2'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scratches-algorithms',
    version=version,

    author='notjik',
    author_email='notjik@yandex.ru',

    description=(
        u'Python package with classical algorithms and simple utilities'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/notjik/scratches-algorithms',
    download_url='https://github.com/notjik/scratches-algorithms/dist/scratches-algorithms-{}.tar.gz'.format(version),

    license='MIT License',

    package_dir={'': 'src'},
    packages=find_packages('src', include=[
        'scratches_algorithms*'
    ]),

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)
