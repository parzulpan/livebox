# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 枚举值管理

@Attention :
"""

from enum import Enum


class LiveEnum(Enum):
    """

    """
    DouYu = 0
    HuYa = 1
    BiliBili = 2
    EGame = 3
    ESport = 4
    ZhanQi = 5
    AcFun = 6
    LongZhu = 7
    DouYin = 8
    KuaiShou = 9
    IXiGua = 10
    IQiYi = 11
    KuGou = 12
    YiZhiBo = 13
    YY = 14
    InKe = 15
    HuoMao = 16
    ImMoMo = 17
    JD = 18
    RenRen = 19
    HuaJiao = 20
    ChuShou = 21
    WaLi = 22
    XunLei = 23
    Now = 24
    CC = 25
    PPS = 26
    V6CN = 27
    Live17 = 28
    LaiFeng = 29
    YouKu = 30
    Look = 31
    QF = 32
    ShowSelf = 33
    WoXiu = 34
    YQS = 35


class PlayerEnum(Enum):
    """

    """
    # 播放器媒体资源定位器（MRL）类型
    # Local：本地文件
    # Live：视频直播
    # TV：高清电视
    # RS：广播电台
    MrlTypeLocal = 100, "Local"
    MrlTypeLive = 101, "Live"
    MrlTypeTV = 101, "TV"
    MrlTypeRS = 101, "RS"

    # 播放器加载状态
    # NothingSpecial：处于空闲状态，等待发出命令
    # Opening：正在打开媒体资源定位器（MRL）
    # Buffering：正在缓冲
    # Playing：正在播放媒体
    # Paused：处于暂停状态
    # Stopped：处于停止状态，此时关闭播放器
    # EncounteredError：遇到错误，无法继续
    # EndReached：已到达当前播放列表的末尾
    LoadNothingSpecial = 200
    LoadOpening = 201
    LoadBuffering = 202
    LoadPlaying = 203
    LoadPaused = 204
    LoadStopped = 205
    LoadEncounteredError = 206
    LoadEndReached = 207

    # 播放器大小状态
    # PlayerMax：播放器全屏
    # PlayerInitial：播放器初始状态
    SizeMax = 300
    SizeInitial = 301

    # 播放器音量状态
    # Muted：静音
    # Unmuted：非静音
    VolumeMuted = 400
    VolumeUnmuted = 401
