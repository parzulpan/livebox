# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : .json 文件的增删改查

@Attention :
"""

import json

from utils.path_helper import PathHelper


default_json_file = PathHelper.get_json_path()


def python2json(data):
    """ 将 Python 对象编码成 JSON 字符串

    :param data:
    :return:
    """
    return json.dumps(data)


def json2python(data):
    """ 将已编码的 JSON 字符串解码为 Python 对象

    :param data:
    :return:
    """
    return json.loads(data)


def python2json2file(data, json_file=None):
    """ 将 Python 类型序列化为 json 对象后写入文件

    :param data:
    :param json_file:
    :return:
    """
    if json_file:
        with open(json_file, "w+") as f:
            json.dump(data, f, indent=4)
    else:
        with open(default_json_file, "w+") as f:
            json.dump(data, f, indent=4)


def json2python4file(json_file=None):
    """ 读取文件中 json 形式的字符串元素转化为 Python 类型

    :param json_file:
    :return:
    """
    if json_file:
        with open(json_file, "r+") as f:
            return json.load(f)
    else:
        with open(default_json_file, "r+") as f:
            return json.load(f)


default_json2python4file = json2python4file()


if __name__ == '__main__':
    print(default_json2python4file)
