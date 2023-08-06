# -*- encoding: utf-8 -*-
"""
@文件名:   base_export_admin.py
@版权:     (C)Copyright 山西博维创 2022-2024

@创建时间              @作者       @版本        @说明
---------------      -------    --------    -----------
2022/10/6 17:15      戎伟峰       1.0         导出基类-基于import-export
"""
from import_export.admin import ExportMixin
from import_export.formats import base_formats

from utils.base.base_admin import BaseAdmin
from utils.tools import export_util


class BaseExportAdmin(ExportMixin,BaseAdmin):
    """
    导出基类
    只有导出
    基于import-export组件
    """
    def get_export_filename(self, request, queryset, file_format):
        """
         impot-export方法重写
        :param request:
        :param queryset:
        :param file_format:
        :return:
        """
        return export_util.export_filename(self)

    def get_export_formats(self):
        """
        重写方法
        限制导出文件格式
        :return:
        """
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]

    def has_export_permission(self, request):
        return True

    def has_import_permission(self, request):
        """
        重写方法
        允许导出按钮
        禁止导入按钮
        :param request:
        :return:
        """
        return False



