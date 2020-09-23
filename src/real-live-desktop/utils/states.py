# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 客户端的状态管理，使用 Qt 状态机，本质为状态模式

@Attention :
"""

from PyQt5.QtCore import QState, QStateMachine

from utils.enums import PlayerEnum


class PlayerState(object):
    """

    """
    # 播放器媒体资源定位器（MRL）类型
    MrlType = PlayerEnum.MrlTypeLocal.value[1]

    # 播放器加载状态
    Load = PlayerEnum.LoadNothingSpecial

    # 播放器大小状态
    Size = PlayerEnum.SizeInitial

    # 播放器音量状态
    Volume = PlayerEnum.VolumeUnmuted

    # 每次增加/减少的时间
    EachIncreaseTime = 5000
    EachDecreaseTime = -5000

    # 每次增加/减少的音量
    EachIncreaseVolume = 5
    EachDecreaseVolume = -5


def run_state_mgr():
    """ 使用并行状态，并对状态进行分组

    :return:
    """
    pass