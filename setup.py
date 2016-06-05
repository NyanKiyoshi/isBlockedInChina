# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='isBlockedInChina',
    version='0.0.1',
    author='KOÇAK Mikail',
    author_email='wibberry@gmail.com',
    url='https://github.com/NyanKiyoshi/isBlockedInChina',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    data_files=[('', ['README.md', 'LICENSE'])],
    keywords=['Internet', 'China', 'censure'],
    packages=['isBlockedInChina'],
    install_requires=[
        'lxml',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
