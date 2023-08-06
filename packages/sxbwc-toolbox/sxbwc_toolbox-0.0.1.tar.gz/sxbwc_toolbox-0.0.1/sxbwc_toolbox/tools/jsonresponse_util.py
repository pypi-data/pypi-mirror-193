# -*- encoding: utf-8 -*-
"""
@文件名:   jsonresponse_util.py
@版权:     (C)Copyright 山西博维创 2022-2024

@创建时间              @作者       @版本        @说明
---------------      -------    --------    -----------
2022/10/21 0:38      戎伟峰       1.0         json响应
"""
import json

from django.http import HttpResponse


def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error