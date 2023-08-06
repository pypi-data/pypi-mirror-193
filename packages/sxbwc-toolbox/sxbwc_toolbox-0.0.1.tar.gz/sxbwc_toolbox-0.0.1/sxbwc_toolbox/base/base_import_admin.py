# -*- encoding: utf-8 -*-
"""
@文件名:   base_import_admin.py   
@版权:     (C)Copyright 山西博维创 2022-2024

@创建时间              @作者            @版本           @说明
---------------      -----------    --------       -----------
2022/11/24 11:26      rongweifeng       1.0           导入导出基类-基于import-export
"""
from import_export.admin import ImportExportMixin
from import_export.formats import base_formats

from utils.base.base_admin import BaseAdmin
from utils.base.base_export_resource import BaseExportResource
from utils.tools import export_util


class BaseImportAdmin(ImportExportMixin,BaseAdmin):
    """
    导入导出基类
    包含导入和导出
    基于import-export组件
    """
    resource_class = BaseExportResource


    def get_export_filename(self, request, queryset, file_format):
        return export_util.export_filename(self)

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]


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

    def has_import_permission(self, request):
        """
        导入按钮控制
        :param request:
        :return:
        """
        if request.user.is_superuser:
            return True
        elif '{0}_import'.format(self.get_app_class_name(request)) in request.user.get_all_permissions():
            return True
        return False

    def has_export_permission(self, request):
        """
        导出按钮控制
        :param request:
        :return:
        """
        if request.user.is_superuser:
            return True
        elif '{0}_export'.format(self.get_app_class_name(request)) in request.user.get_all_permissions():
            return True
        return False


    def get_app_class_name(self,request):
        """
        获取包含app_labe的类名称
        :param request:
        :return:
        """
        name= '{0}.{1}'.format(self.model._meta.app_label,self.model._meta.model_name)
        return name