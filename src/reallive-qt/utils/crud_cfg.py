# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : .ini 文件的增删改查

@Attention : 已弃用，改用 json 数据交互
"""

import configparser

from utils.path_helper import PathHelper

cfg_file = PathHelper.get_config_path()

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
