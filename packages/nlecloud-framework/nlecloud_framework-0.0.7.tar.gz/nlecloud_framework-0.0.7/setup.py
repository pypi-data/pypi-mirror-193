# _*_ coding:utf-8 _*_
"""
@File: setup.py
@Author: cfp
@Date: 2020-08-21 14:07:08
@LastEditTime: 2023/2/22 15:43
@LastEditors: cfp
@LastModifyTime @Version  @Desciption
@Description: 
"""

from distutils.core import setup
from setuptools import find_packages


# 获取readme文档
with open("README.md","rb") as f :
    data = f.read().decode("utf8")
    long_description = data

# 需要按住的第三方库
install_requires = [
    "cffi==1.15.1",
    "cryptography==39.0.1",
    "pycparser==2.21"
]

setup(
    name="nlecloud_framework",      # python包的名字
    version="0.0.7",                # 版本号
    description='nlecloud_framework框架',           # 描述
    long_description=long_description,                  # 详细描述，这里将readme的内容放置于此
    long_description_content_type='text/markdown',  #文件格式
    author='redrose2100',                                      # 作者
    author_email='954742660@qq.com',              # 作者邮箱
    maintainer='dalyer',                               # 维护人
    maintainer_email='954742660@qq.com',       # 维护人邮箱
    license='BSD License',                                    # 遵守协议
    packages=find_packages(),
    install_requires=[],                                            # lamb-common依赖的第三方库,
    platforms=["all"],                                                # 支持的平台
    url='https://github.com/redrose2100/lamb-common',          # github代码仓地址
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries'
    ],
)
