# -*- encoding: utf-8 -*-
"""
@文件名:   base_model.py   
@版权:     (C)Copyright 山西博维创 2022-2024

@创建时间              @作者       @版本        @说明
---------------      -------    --------    -----------
2022/10/5 12:39      戎伟峰       1.0         None
"""
import uuid

import mptt.models
from django.contrib.auth.models import User
from django.db import models



class BaseModel(models.Model):
    """
    普通模型基类
    定义系统字段:
        id: id
        name:名称
        note:备注
        create_time:创建时间
        modify_time:修改时间
        state: 状态
    基类中不能使用引用字段
    """
    id = models.BigAutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name='名称', max_length=200, )  # unique=True
    code = models.CharField(verbose_name='编码', max_length=200, null=True,blank=True)
    note = models.TextField(verbose_name='备注', max_length=500, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    creator=models.ForeignKey(User,db_column='creator',verbose_name='创建人',related_name='%(app_label)s_%(class)s_creator_user',on_delete=models.CASCADE,null=True)
    modifier=models.ForeignKey(User,db_column='modifier',verbose_name='修改人',related_name='%(app_label)s_%(class)s_modify_user',on_delete=models.CASCADE,null=True)
    STATE=(
        (0,'禁用'),
        (1,'启用')
    )
    state=models.SmallIntegerField(verbose_name='状态',choices=STATE,default=1)
    order_no =models.BigIntegerField(verbose_name='序号',default=1)

    class Meta:
        abstract=True  #  抽象类

    def __str__(self):
        return self.name



class BaseTreeModel(mptt.models.MPTTModel,BaseModel):
    """
    树形模型基类
    """

    parent = models.ForeignKey('self', verbose_name='上级', null=True, blank=True, on_delete=models.SET_NULL,related_name='parent_'+ '%(app_label)s_%(class)s') # relate_name_prefix()

    class Meta:
        abstract = True

    class MPTTMeat:
        parent_attr = 'parent'




