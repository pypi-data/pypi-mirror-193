#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "testpyd",      #这里是pip项目发布的名称
    version = "0.0.1",  #版本号，数值大的会优先被pip
    keywords = ["pip", "testpyd"],			# 关键字
    description = "Ferelegan's test.",	# 描述
    long_description = "Ferelegan's test.",
    license = "MIT",		# 许可证
    zip_safe=False,

    url = "https://github.com/Adenialzz/SongUtils",     #项目相关文件地址，一般是github项目地址即可
    author = "Adenialzz",			# 作者
    author_email = "ferelegan111@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],          #这个项目依赖的第三方库
    python_requires='>=3'
)
