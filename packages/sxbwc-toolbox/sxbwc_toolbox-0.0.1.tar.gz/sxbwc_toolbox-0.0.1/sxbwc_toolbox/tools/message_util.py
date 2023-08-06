# -*- encoding: utf-8 -*-

"""
@文件名称:    message_util.py 
@版   权:    (C)Copyright 山西博维创 2023
@创建时间:    2023/2/20 22:44 
@作   者:    rongweifeng     	
@版   本:    1.0   	            	
@说   明:
  消息工具类
"""
import json
import logging

import requests
from dingtalkchatbot.chatbot import DingtalkChatbot
import settings.dev
from utils.tools import weixin_template_util

logger=logging.getLogger(__name__)

def send_dingtalk_message(message, mobiles=[]):
    """
    发送钉钉文本消息
    :param message:
    :param mobiles:
    :return:
    """
    webhook=settings.base.DING_TALK_WEBHOOK
    secret=settings.base.DING_TALK_SECRET

    # 机器人初始化
    # :param webhook: 钉钉群自定义机器人webhook地址
    #  :param secret: 机器人安全设置页面勾选“加签”时需要传入的密钥
    #  :param pc_slide: 消息链接打开方式，默认False为浏览器打开，设置为True时为PC端侧边栏打开
    #  :param fail_notice: 消息发送失败提醒，默认为False不提醒，开发者可以根据返回的消息发送结果自行判断和处理
    xiaoding = DingtalkChatbot(webhook=webhook, secret=secret)

    # 发送消息
    # :param msg: 消息内容
    #  :param is_at_all: @所有人时：true，否则为false（可选）
    #  :param at_mobiles: 被@人的手机号（注意：可以在msg内容里自定义@手机号的位置，也支持同时@多个手机号，可选）
    # :param at_dingtalk_ids: 被@人的dingtalkId（可选）
    # :param is_auto_at: 是否自动在msg内容末尾添加@手机号，默认自动添加，可设置为False取消（可选）

    if isinstance(mobiles,str):
        mobiles=[mobiles]
    try:
        if mobiles is None or len(mobiles)==0:
            xiaoding.send_text(msg=message, is_at_all=True, at_mobiles=[])
            logger.info('发送钉钉消息成功,消息内容:{},通知所有人'.format(message))
        else:
            xiaoding.send_text(msg=message,at_mobiles=mobiles)
            logger.info('发送钉钉消息成功,消息内容:{},通知人员:{}'.format(message,';'.join(mobiles)))
    except Exception as e :
        logger.error('发送钉钉消息失败,消息内容:{},通知人员:{},错误信息:{}'.format(message,';'.join(mobiles),e))


def send_weixin_message(message,mobiles,picture=None):
    """
    发送企业微信消息
    :param message:
    :param mobiles:
    :param picture:  图片对象
        {
            "url": "点击图片的跳转地址",
            "image":"图片的地址"
        }
    :return:
    """
    webhook = settings.base.WEIXIN_TALK_WEB_HOOK
    data={}
    if picture: # 图文消息
        data = {
            "msgtype": "news",  # news格式消息
            "news": {
                "articles": [
                    {
                        "title": message,  # 主标题
                        "description": message,  # 副标题
                        "url": picture.get('url'),  # 这段是图文消息点进去后转到的地址
                        "picurl": picture.get('image') # 图片地址
                    }
                ]
            }
        }
    else: # 文本消息
        data = {
            "msgtype": "text",
            "text": {
                "content": message,
                "mentioned_list": [],
            }
    }
    try:
        res = requests.post(url=webhook, json=data)
        ret= json.loads(res.text)
        if ret.get('errcode')==0:
            logger.info('发送企业微信消息成功,消息内容:{}'.format(message))
        else:
            logger.error('发送企业微信消息失败,消息内容:{},错误信息:{}'.format(message,ret.text.get('errmsg')))
    except Exception as e :
        logger.error('发送企业微信消息失败,消息内容:{},错误信息:{}'.format(message,e))



def send_weixin_template_message(openids,template,params,link=''):
    """
    发送微信模板消息
    :param openids: openid集合
        1个:字符串
        多个:列表
    :param template:
        模板消息id
    :param params:
        模板参数,格式:
            "参数名1:
            {
                "value":"参数值",
                "color": "#173177"
            },
            "参数名2:
            {
                "value":"参数值"
            }
    :param link: 链接地址
    :return:
    """
    if isinstance(openids,str) :
        openids =[openids]
    if len(openids)==0:
        return
    for openid in openids:
        try:
            message={
                'openid':openid,
                'template':template,
                'params':params
            }
            ret =weixin_template_util.send_msg(openid,template,params,link)
            if ret:
                logger.info('发送微信模板消息成功,消息内容:{}'.format(message))
            else:
                logger.error('发送微信模板消息失败,消息内容:{}'.format(message))

        except Exception as e :
            logger.error('发送微信模板消息失败,消息内容:{},错误信息{}'.format(message,e))


"""  测试数据  =====================================
    openids="o6tb45oT_lVwYo0ryqNUPGbGqNIQ"
    template="xMOLkofOdeJmpEhbXXWK1TxUym5JEACOkxw6hzf-ex4"
    params={
        "first":{
            "value":"访问申请"
        },
        "keyword1":{
            "value":"戎伟峰",
        },
        "keyword2":{
            "value":"找周晓旭签合同"
        },
        "keyword3": {
            "value":"2023-2-22 16:00"
        },

        "keyword4": {
            "value":"13835165255",
        },
        "remark":{
            "value":"已经电话预约"
        }
    }
"""

if __name__ == '__main__':
    message="明天准备下井"
    # picture={
    #     "url":'https://www.baidu.com',
    #     "image":"https://t7.baidu.com/it/u=1819248061,230866778&fm=193&f=GIF"
    # }
    # send_weixin_message(message,'13835165255',picture)
    send_dingtalk_message(message,'13835165255')