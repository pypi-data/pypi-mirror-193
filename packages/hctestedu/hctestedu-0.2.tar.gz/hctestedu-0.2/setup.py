# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：setup.py
from setuptools import setup,find_packages

setup(
    name="hctestedu",
    version="0.2",
    description="支持yaml文件里面的数据内容转化为常用的python数据",
    author="cf",
    author_email="dingjun_baby@yeah.net",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'chardet'
    ],
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    python_requires='>=3.6',

)