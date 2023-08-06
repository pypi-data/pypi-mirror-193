# -*- encoding: utf-8 -*-

"""
@文件名称:    weixin_template_util.py
@版   权:    (C)Copyright 山西博维创 2023
@创建时间:    2023/2/22 01:13 
@作   者:    rongweifeng     	
@版   本:    1.0   	            	
@说   明:
  微信公众号工具箱
"""
import json
import time
import requests
import settings.base

exp_time = 0
access_token = ''

def get_access_token():
    """
    获取access_token
    :return: 返回token
    """
    global exp_time, access_token
    appid = settings.base.WEIXIN_TEMPLATE_APPID
    appkey = settings.base.WEIXIN_TEMPLATE_APPKEY
    if time.time() > exp_time:
        try:
            res= requests.get(
                'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(appid,appkey))
            data = json.loads(res.text)
            access_token = data['access_token']
            exp_time = time.time() + data['expires_in'] - 10  # 减一点防止快到时间的时候已经失效了
        except Exception as e:
            raise e
    return access_token


def send_msg(openid,template,params,link=''):
    """
    发送单条模板消息
    :param openid: openid
    :param template: 模板消息id
    :param params: 模板参数
    :link: 点击链接地址
    :return:
    """

    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + get_access_token()
    data = {
        "touser": openid,
        "template_id": template,
        "url": link,
        "data": params,

    }

    try:
        res = requests.post(url, json.dumps(data))
        ret=json.loads(res.text)
        if ret.get('errcode')==0:
            return True
    except Exception as e:
        raise e
    return False


