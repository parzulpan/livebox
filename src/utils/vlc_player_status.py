# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : VLC 播放器当前状态，使用状态模式

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
