# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 自动补全最近搜索

@Attention :
"""


def add_update_search(pipeline, content):
    """ 添加到更新最近搜索

    """
    content = str(content)
    pipeline = pipeline.pipeline(True)
    pipeline.lrem("recent_search:", 1, content)
    pipeline.lpush("recent_search:", content)
    pipeline.ltrim("recent_search:", 0, 9)
    pipeline.execute()


def remove_search(pipeline, content):
    """ 移除指定的搜索记录

    """
    content = str(content)
    pipeline.lrem("recent_search:", 1, content)


def get_recent_search_list(conn):
    """ 获得最近搜索结果，让前端进行匹配并自动补全

    """
    candidates = conn.lrange("recent_search:", 0, -1)
    return candidates
