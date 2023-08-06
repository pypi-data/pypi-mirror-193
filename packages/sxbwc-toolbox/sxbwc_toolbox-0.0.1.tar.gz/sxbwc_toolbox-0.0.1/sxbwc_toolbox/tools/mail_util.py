# -*- encoding: utf-8 -*-

"""
@文件名称:    mail_util.py 
@版   权:    (C)Copyright 山西博维创 2023
@创建时间:    2023/2/21 20:41 
@作   者:    rongweifeng     	
@版   本:    1.0   	            	
@说   明:
  email工具类
  1.发送附件暂时没有实现
"""
import logging
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import settings
from utils.tools import random_util

logger=logging.getLogger(__name__)



def send_mail_vcode(to_address):
    """
    发送验证码到邮箱
    :param to_address: 接收邮箱
    :return: 返回验证码
    """
    vcode=random_util.generate_vcode(6)
    message = "您好,欢迎注册,您的验证码:{},有效期60分钟,请立即验证".format(vcode)
    if send_mail(message,to_address):
        return vcode
    return ''

def send_mail(message,to_addr):
    """
    发送邮件
    :param to_addr:     接收方邮箱,支持多个, 用;进行连接
    :return:            返回true和false
    """
    # 构建smtp对象
    server =smtplib.SMTP(settings.base.MAIL_SMTP_SERVER,25)
    # 设置调试级别
    server.set_debuglevel(1)
    try:
        # 登录邮箱
        server.login(settings.base.MAIL_SEND_EMAIL_ADDR, settings.base.MAIL_SEND_EMAIL_PASSWORD)
        # 生成邮件内容
        msg = generate_mail_message(message, settings.base.MAIL_SEND_EMAIL_ADDR, to_addr)
        # 发送邮件
        server.sendmail(settings.base.MAIL_SEND_EMAIL_ADDR, to_addr.split(';'), msg.as_string())
        # 退出邮件服务器
        server.quit()
    except Exception as e:
        logger.error('邮件发送失败:{},错误原因:{}'.format(msg.as_string(),e))
        return False
    logger.info('邮件发送成功'.format(msg.as_string()))
    return True




def generate_mail_message(message,from_addr,to_addr):
    """
    生成邮件内容
    :param vcode:验证码
    :param from_addr:发送邮箱
    :param to_addr:接收邮箱
    :return:包含验证码的邮件内容
    """
    msg=MIMEText(message,'plain','utf-8')
    msg['From']=_format_addr('山西博维创<{}>'.format(from_addr))
    msg['To']=_format_addr('验证码<{}>'.format(to_addr))
    msg['Subject']=Header('邮箱验证码').encode()
    return msg



def _format_addr(s):
    """
    格式化邮件头
    :param s: 原始内容
    :return: 格式化后的内容
    """
    name,addr =parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))



