# -*- encoding: utf-8 -*-
"""
@文件名:   export_util.py   
@版权:     (C)Copyright 山西校安通 2022-2024

@创建时间              @作者       @版本        @说明
---------------      -------    --------    -----------
2022/10/6 18:14      戎伟峰       1.0         None
"""

import logging
from datetime import datetime


logger = logging.getLogger(__name__)

# 导出excel名称
def export_filename(self):
    """
    导出文件名称定义
    模型verbose_name + 导出日期
    基于 import_export 组件
    :param self:
    :param request:
    :return:
    """
    import urllib.parse
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename_diy = urllib.parse.quote(self.model._meta.verbose_name)
    filename = "%s_%s.%s" % (filename_diy, date_str, 'xls') # file_format.get_extension()
    return filename
