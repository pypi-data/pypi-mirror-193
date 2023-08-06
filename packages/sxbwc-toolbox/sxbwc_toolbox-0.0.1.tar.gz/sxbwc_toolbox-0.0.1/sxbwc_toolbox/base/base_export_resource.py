# -*- encoding: utf-8 -*-
"""
@文件名:   base_export_resource.py
@版权:     (C)Copyright 山西博维创 2022-2024

@创建时间              @作者       @版本        @说明
---------------      -------    --------    -----------
2022/10/6 17:23      戎伟峰       1.0         import_export 资源基类
"""
import tablib
from import_export.resources import ModelResource

from utils.base.base_model import BaseModel


class BaseExportResource(ModelResource):
    class Meta:
        model = BaseModel
        fields = '__all__'  # 指定导出的字段
        export_order = ()  # 指定导出的顺序
        exclude = ('creator', 'create_time', 'modifier', 'modify_time', 'order_no', 'state', 'order_no')  # 不用导出的内容
        import_id_fields = ('id',)  # 指定ID字段名称

    def __init__(self):
        """
        初始化数据
        生成verbose_name数据集
        """
        super().__init__()
        field_list = self.fields
        self.vname_dict = {}
        for item in field_list.keys():
            self.vname_dict[item] = getattr(self.Meta.model, item).field.verbose_name  # field_list[item].verbose_name

    def get_export_fields(self):
        """
        重写方法
        转换导出字段
        处理表头,显示verbose_name(中文)
        :return:
        """
        fields = self.get_fields()
        for i, field in enumerate(fields):
            field_name = self.get_field_name(field)
            if field_name.find("__") > 0:
                _field_name = field_name.split("__")[0]
                if _field_name in self.vname_dict.keys():
                    field.column_name = self.vname_dict[_field_name]
            elif field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    def get_sheet_name(self):
        """
        获取sheet页的中文名称
        修改sheet页名称为模型的verbose_name
        ??? 未实现,调用方法未知
        :return:
        """
        name = '导出数据'
        try:
            name = self.Meta.model._meta.verbose_name
            # data = tablib.Dataset(headers=headers, title="Sheet")
        except:
            pass

        return name
