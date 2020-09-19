# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 客户端的状态管理，使用 Qt 状态机

@Attention :
"""

from enum import Enum


class VLCPlayerStatus(Enum):

    USE = False
    UNUSED = False
    OPENM = False
    PLAYING = False
    PAUSED = False
    STOPPED = False
