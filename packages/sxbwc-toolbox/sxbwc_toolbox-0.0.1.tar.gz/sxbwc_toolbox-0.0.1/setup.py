# -*- encoding: utf-8 -*-

"""
@文件名称:    setup.py 
@版   权:    (C)Copyright 山西博维创 2023
@创建时间:    2023/2/22 02:46 
@作   者:    rongweifeng     	
@版   本:    1.0   	            	
@说   明:
  
"""
from setuptools import setup, find_packages

setup(
    name='sxbwc_toolbox',
    version='0.0.1',
    author='sxbwc',
    author_email='65489942@qq.com',
    description='山西博维创python工具包',
    url='http://www.sxbwc.cn',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=[
        'sxbwc_toolbox.base.base_admin',
        'sxbwc_toolbox.base.base_export_admin',
        'sxbwc_toolbox.base.base_import_admin',
        'sxbwc_toolbox.base.base_export_resource',
        'sxbwc_toolbox.base.base_model',
        'sxbwc_toolbox.tools.datetime_util',
        'sxbwc_toolbox.tools.export_util',
        'sxbwc_toolbox.tools.jsonresponse_util',
        'sxbwc_toolbox.tools.mail_util',
        'sxbwc_toolbox.tools.md5_util',
        'sxbwc_toolbox.tools.message_util',
        'sxbwc_toolbox.tools.permission_util',
        'sxbwc_toolbox.tools.pinyin_util',
        'sxbwc_toolbox.tools.pycharts_util',
        'sxbwc_toolbox.tools.random_util',
        'sxbwc_toolbox.tools.datetime_util',
        'sxbwc_toolbox.tools.sms_util',
        'sxbwc_toolbox.tools.weixin_template_util',

    ]
)
