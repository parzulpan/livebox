# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""

import configparser

cfg_file = "./resources/config.ini"

cfg = configparser.ConfigParser()

cfg.read(cfg_file, encoding='utf-8')


def create_content(section, option=None, value=None):
    """

    :param section:
    :param option:
    :param value:
    :return:
    """
    if option and value:
        cfg.add_section(section)
        cfg.set(section, option, value)
    else:
        cfg.add_section(section)
    cfg.write(open(cfg_file, "w+", encoding="utf-8"))


def retrieve_content(section, option=None):
    """

    :param section:
    :param option:
    :return:
    """
    if option:
        return cfg.get(section, option)
    else:
        return cfg.items(section)


def update_contents(section, option=None, value=None):
    """

    :param section:
    :param option:
    :param value:
    :return:
    """
    if option and value:
        cfg.set(section, option, value)
    else:
        cfg.add_section(section)
    cfg.write(open(cfg_file, "w+", encoding="utf-8"))


def delete_content(section, option=None):
    """

    :param section:
    :param option:
    :return:
    """
    if option:
        cfg.remove_option(section, option)
    else:
        cfg.remove_section(section)
