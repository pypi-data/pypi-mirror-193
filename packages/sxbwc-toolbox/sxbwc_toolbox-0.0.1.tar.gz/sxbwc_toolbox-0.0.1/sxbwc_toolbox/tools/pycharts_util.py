# -*- encoding: utf-8 -*-
"""
@文件名:   pycharts_util.py
@版权:     (C)Copyright 山西博维创 2022-2024

@创建时间              @作者       @版本        @说明
---------------      -------    --------    -----------
2022/10/21 0:39      戎伟峰       1.0         pyechart-折线
"""
import pyecharts.options as opts
from pyecharts.charts import Line, Pie
from pyecharts.globals import ThemeType


def line(x,y,title='') :
    """
       折线
       :param x:
       :param y:
       :return:
    """
    c = (
        Line()
            .add_xaxis(xaxis_data=x)
            .add_yaxis(
                series_name='', # title
                y_axis=y,
                is_connect_nones=True)
            .set_global_opts(title_opts=opts.TitleOpts(title='')) # title
            .dump_options_with_quotes()
    )
    return c


def pie(x,y,title='') :
    """
       饼图
       :param x:
       :param y:
       :return:
    """
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            # 为饼图增加标签和数据
            .add("", list(zip(x, y)))
            # 为饼图增加主标题和副标题
            .set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=""))
            # 为饼图增加数据标签
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}\n({d}%)"))
            .dump_options_with_quotes()
    )



    return c