# -*- encoding: utf-8 -*-
"""
@文件名:   pinyin_util.py   
@版权:     (C)Copyright 山西校安通 2022-2024

@创建时间              @作者       @版本        @说明
---------------      -------    --------    -----------
2022/10/6 11:33      戎伟峰       1.0         拼音工具类
"""
from xpinyin import Pinyin

def hanzi_to_pinyin_first(self,str):
    """
    汉字转拼音首字母
    :param self:
    :param str:
    :return:
    """
    p = Pinyin()
    return p.get_initial(str,'')


def hanzi_to_pinyin(self,str):
    """
    汉字转拼音全拼
    :param self:
    :param str:
    :return:
    """
    p = Pinyin()
    return p.get_pinyin(str, '')

