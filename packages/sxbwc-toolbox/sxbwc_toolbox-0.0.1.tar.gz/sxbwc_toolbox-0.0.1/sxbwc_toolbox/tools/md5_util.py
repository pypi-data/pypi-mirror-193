# -*- encoding: utf-8 -*-
"""
@文件名:   md5.py
@版权:     (C)Copyright 山西校安通 2022-2024

@创建时间              @作者       @版本        @说明
---------------      -------    --------    -----------
2022/8/26 17:28      戎伟峰       1.0        md5-加解密
"""
import hashlib

def md5_password(password):
    """
    md5加密密码
    :param password:  密码明文
    :return: 加密后的值
    """
    try:
        md5_password = hashlib.md5(bytes(password, encoding='utf-8')).hexdigest()
    except:
        md5_password = ''
    return md5_password