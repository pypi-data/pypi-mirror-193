# -*- encoding: utf-8 -*-

"""
@文件名称:    random_util.py 
@版   权:    (C)Copyright 山西博维创 2023
@创建时间:    2023/2/21 21:03 
@作   者:    rongweifeng     	
@版   本:    1.0   	            	
@说   明:
  随机数生成器
"""

import random

def generate_vcode(length=6):
    """
    生成随机验证码
    :param length: 验证码长度,默认6位
    :return:
    """
    return ''.join(random.choices('0123456789',k=length))


