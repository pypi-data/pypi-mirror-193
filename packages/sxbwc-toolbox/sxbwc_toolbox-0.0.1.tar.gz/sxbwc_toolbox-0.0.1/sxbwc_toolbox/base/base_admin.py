# -*- encoding: utf-8 -*-
"""
@文件名:   base_admin.py
@版权:     (C)Copyright 山西博维创 2022-2024

@创建时间              @作者       @版本        @说明
---------------      -------    --------    -----------
2022/10/5 13:28      戎伟峰       1.0         管理类-基类
"""
from django.contrib import admin

from utils.tools import md5_util
from utils.tools.pinyin_util import hanzi_to_pinyin_first


class BaseAdmin(admin.ModelAdmin):
    list_display = ['name','note','state','creator','create_time','modifier','modify_time']
    exclude = ['id',  'code','create_time', 'creator', 'modify_time', 'modifier', ]  # 编辑页-系统项
    ordering = ['id',] # 排序
    list_per_page = 30  # 每页显示条数
    list_max_show_all = 500  # 显示全部

    def save_model(self, request, obj, form, change):
        """
        重写保存方法
        给系统字段赋值
        :param request:
        :param obj:
        :param form:
        :param change: 对象编辑状态
        :return:
        """
        # 检查系统字段是否存在
        if hasattr(obj,'creator') and hasattr(obj,'create_time') and hasattr(obj,'modify_time') and hasattr(obj,'modifier'):
            if change: # 修改状态
                if not obj.creator:
                    obj.creator = request.user
                obj.modifier = request.user
            else: # 添加状态
                obj.creator = request.user
                obj.modifier = request.user
        # 生成编码
        if not obj.code:
            obj.code=self.generate_code(obj)
        # 自动生成序号
        if hasattr(obj,'order_no'):
            if not change:
                obj.order_no=self.generate_order_no(obj)

        # 密码加密存储
        if hasattr(obj,'password') and not change:
           obj.password=self.password_md5(obj)
        return super().save_model(self, obj, form, change)


    def generate_code(self,obj):
        """
        自动生成编码
        根据名称生成拼音首字母
        :param obj:
        :return:
        """
        if not obj:
            return ''
        if not obj.name or obj.name=='':
            return ''
        code=''
        try:
            code=hanzi_to_pinyin_first(self,obj.name)
        except:
            pass
        return code

    def generate_order_no(self,obj):
        """
        生成序号
        :param obj:
        :return:
        """
        if not obj:
            return 1
        order_no = 1
        if hasattr(obj, 'parent'):  # 根据父级计算
            try:
                order_no = self.model.objects.filter(parent=obj.parent).order_by('-order_no').first().order_no + 1
            except:
                pass
        else: # 根据同级计算
            try:
                order_no = self.model.objects.all().order_by('-order_no').first().order_no + 1
            except:
                pass
        return order_no


    def password_md5(self,obj):
        """
        密码使用md5保存
        只针对新建数据
        编辑状态保存由子类自己实现
        :param self:
        :param obj:
        :return:
        """

        if not obj:
            return ''
        password = obj.password
        try:
            password = md5_util.md5_password(obj.password)
        except:
            pass
        return password