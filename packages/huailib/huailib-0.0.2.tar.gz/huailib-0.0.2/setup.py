#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File     : setup
# @Author   : LiuYan
# @Time     : 2021/4/16 10:07

import setuptools

with open('./huailib/README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='huailib',
    version='0.0.2',
    author='huai guo',
    author_email='guohuai@csu.edu.cn',
    description='a helpful python library',
    long_description=long_description,
    url='https://github.com/wsmgh/hpl.git',
    packages=setuptools.find_packages(),

)

