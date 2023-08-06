# -*- encoding: utf-8 -*-

"""
@文件名称:    permission_util.py 
@版   权:    (C)Copyright 山西博维创 2023
@创建时间:    2023/2/20 15:18 
@作   者:    rongweifeng     	
@版   本:    1.0   	            	
@说   明:
  django权限
"""
import logging

logger =logging.getLogger(__name__)

def get_groups(request):
    """
    获取用户隶属的组名
    :param request:
    :return:
    """
    group_names=[]
    try:
        for group in request.user.groups.all():
            group_names.append(group.name)
    except:
        logger.log('用户未登录')

    return group_names