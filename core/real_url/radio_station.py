# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""

universal_radio_station_dict = {}


local_radio_station_dict = {}


def get_radio_station_url(radio_station_type, radio_station_id):
    """

    :param radio_station_type:
    :param radio_station_id:
    :return:
    """
    if radio_station_type == "通用":
        return universal_radio_station_dict[radio_station_id]
    else:
        return local_radio_station_dict[radio_station_id]
