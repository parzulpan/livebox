# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 数据库帮助工具

@Attention :
"""

import redis


def get_redis_client():
    """

    """

    pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r


def get_redis_pipeline():
    """

    """

    return get_redis_client().pipeline()


def get_mysql_client():
    """

    """
    pass