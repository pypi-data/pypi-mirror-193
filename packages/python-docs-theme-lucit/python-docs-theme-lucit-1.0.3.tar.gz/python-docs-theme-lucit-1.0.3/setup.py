#!/usr/bin/env python3

import io
from setuptools import setup

with io.open('README.md', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='python-docs-theme-lucit',
    version='1.0.3',
    description='A responsive sphinx theme for github pages based on python-docs-theme for LUCIT docs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Oliver Zehentleitner',
    url='https://www.lucit.tech',
    packages=['python_docs_theme_lucit'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'python_docs_theme_lucit = python_docs_theme_lucit',
        ]
    },
    project_urls={
        'Source': 'https://github.com/LUCIT-Systems-and-Development/python-docs-theme-lucit',
        'Author': 'https://www.lucit.tech',
    },

    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python :: 3',
    ],
)
