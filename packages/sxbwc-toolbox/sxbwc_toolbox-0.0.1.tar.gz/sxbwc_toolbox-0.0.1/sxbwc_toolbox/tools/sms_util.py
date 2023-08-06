# -*- encoding: utf-8 -*-

"""
@文件名称:    sms_util.py 
@版   权:    (C)Copyright 山西博维创 2023
@创建时间:    2023/2/21 20:42 
@作   者:    rongweifeng     	
@版   本:    1.0   	            	
@说   明:
  短信服务类
"""
import json
import logging

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

import settings.base
from utils.tools import random_util

logger=logging.getLogger(__name__)

def send_phone_code(phone):
    """
    发送手机验证码
    :param phone: 接收手机号码,多个号码用逗号分隔
    :return: 返回验证码
    """
    vcode=random_util.generate_vcode(6)
    template=settings.base.SMS_TEMPLATE_VCODE
    params={
        "code":vcode,
    }
    if send_phone(phone,template,params):
        return vcode
    return ''


def send_phone(phone,template,params):
    """
    发送手机短信
    :param phone: 接收手机号码,多个号码用逗号分隔
    :param message: 短信内容
    :return: 返回true/false
    """

    # 创建客户端对象
    client = AcsClient(settings.base.SMS_APP_ID, settings.base.SMS_APP_KEY)
    # 设置发送请求
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com') # 阿里云短信网关
    request.set_method('POST')
    request.set_protocol_type('https')  # http协议
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')
    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', settings.base.SMS_SIGN)   # 短信签名
    request.add_query_param('TemplateCode', template)      # 短信模板
    request.add_query_param('TemplateParam', params)    # 模板参数
    message ={
        "template":template,
        "params":params,
        "phone":phone,
    }
    try:
        response = client.do_action_with_exception(request)
        ret = json.loads(response.decode())
        if ret.get('Code') == "OK":
            logger.info('短信发送成功,发送内容:{}'.format(message))
            return True
        else:
            logger.error('短信发送失败,发送内容:{}'.format(message))
    except Exception as e:
        logger.error('短信发送失败,发送内容:{},错误原因:{}'.format(message,e))

    return False


