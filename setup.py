# coding=utf-8
#!/usr/bin/env python

from setuptools import setup, find_packages
import wbteq
import os

def read(*names):
    values = dict()
    extensions = ['.md', '.txt']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values

long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

setup(
    name='wbteq',
    version=wbteq.__version__,
    description='Run Teradata BTEQ on Windows with parameters',
    long_description=long_description,
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Documentation",
    ],
    keywords='teradata bteq database command console wrapper',
    author='Zhong Dai',
    author_email='zhongdai2017@gmail.com',
    maintainer='Zhong Dai',
    maintainer_email='zhongdai2017@gmail.com',
    url='https://github.com/zhongdai/wbteq',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'wbteq = wbteq.wbteq:command_line_runner',
        ]
    },
    install_requires=[
        'pyodbc'
    ],
)
