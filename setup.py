# -*- coding: utf-8 -*-
"""
Python TestRail PyTest
----------------------

TestRail Report Generator for pytest.
"""

from setuptools import setup, find_packages

install_requires = [
    'future',
    'pytest>=3.2.5',
    'pytest-env',
    'selenium',
    'pillow',
    'pyobjc',
    'pyobjc-core',
    'pyautogui',
    'pillow'
]

dependency_links = ["http://user:password@pypi-cabestan/packages/"]

setup(
    name='iris_selenium_tests',
    version='0.0.1',
    description='Librar that handles squash operations',
    long_description=__doc__,
    url='https://bitbucket.org/cabestan-dev/testsuite-pytest-selenium',
    keywords='testuite python selenium util',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    include_package_data=True,
    dependency_links=dependency_links
)
