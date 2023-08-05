#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["pydantic"]

test_requirements = ['pytest>=3', ]

setup(
    author="contracts",
    author_email='contracts@test.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='orders_pr_contracts',
    name='orders_pr_contracts',
    packages=find_packages(
        include=['orders_pr_contracts', 'orders_pr_contracts.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/example/orders_pr_contracts',
    version='0.1.0',
    zip_safe=False,
)
