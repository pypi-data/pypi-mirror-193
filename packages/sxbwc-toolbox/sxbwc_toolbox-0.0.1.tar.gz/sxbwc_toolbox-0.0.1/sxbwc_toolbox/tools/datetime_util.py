from datetime import datetime
from django.utils.html import format_html


# 自定义日期格式: 年-月-日 时:分:秒
def custom_date_format(self, obj):
    try:
        return format_html(
            '<span style="color: black;">{}</span>',
            obj.strftime('%Y-%m-%d %H:%M:%S'))
    except:
        pass
    return obj

# 当前日期和时间
def current_time():
    dt=datetime.now()
    return  datetime.strftime(dt,'%Y-%m-%d %H:%M:%S')


# 自定义日期格式: 年-月-日 时:分:秒
def date_html(self, date):
    try:
        return format_html(
            '<span style="color: black;">{}</span>',
            date.strftime('%Y-%m-%d %H:%M:%S'))
    except:
        pass
    return date

# 当前日期和时间
def current_str():
    dt=datetime.now()
    return  datetime.strftime(dt,'%Y-%m-%d %H:%M:%S')