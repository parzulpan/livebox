# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""

from utils.enums import LiveEnum
from core.real_url.douyu import get_real_url as DouYu
from core.real_url.huya import get_real_url as HuYa
from core.real_url.bilibili import get_real_url as BiliBili
from core.real_url.egame import get_real_url as EGame
from core.real_url.esport import get_real_url as ESport
from core.real_url.zhanqi import get_real_url as ZhanQi
from core.real_url.acfun import get_real_url as AcFun
from core.real_url.longzhu import get_real_url as LongZhu
from core.real_url.douyin import get_real_url as DouYin
from core.real_url.kuaishou import get_real_url as KuaiShou
from core.real_url.ixigua import get_real_url as IXiGua
from core.real_url.iqiyi import get_real_url as IQiYi
from core.real_url.kugou import get_real_url as KuGou
from core.real_url.yizhibo import get_real_url as YiZhiBo
from core.real_url.yy import get_real_url as YY
from core.real_url.inke import get_real_url as InKe
from core.real_url.huomao import get_real_url as HuoMao
from core.real_url.immomo import get_real_url as ImMoMo
from core.real_url.jd import get_real_url as JD
from core.real_url.renren import get_real_url as RenRen
from core.real_url.huajiao import get_real_url as HuaJiao
from core.real_url.chushou import get_real_url as ChuShou
from core.real_url.wali import get_real_url as WaLi
from core.real_url.xunlei import get_real_url as XunLei
from core.real_url.now import get_real_url as Now
from core.real_url.cc import get_real_url as CC
from core.real_url.pps import get_real_url as PPS
from core.real_url.v6cn import get_real_url as V6CN
from core.real_url.live17 import get_real_url as Live17
from core.real_url.laifeng import get_real_url as LaiFeng
from core.real_url.youku import get_real_url as YouKu
from core.real_url.look import get_real_url as Look
from core.real_url.qf import get_real_url as QF
from core.real_url.showself import get_real_url as ShowSelf
from core.real_url.woxiu import get_real_url as WoXiu
from core.real_url.yqs import get_real_url as YQS


import core.real_url.tv as TV

import core.real_url.radio_station as RadioStation


def get_real_url_from_platform_content(platform, content):
    """

    :param platform:
    :param content:
    :return:
    """

    if platform == LiveEnum.DouYu.value:
        result = DouYu(content)

    elif platform == LiveEnum.HuYa.value:
        result = HuYa(content)

    elif platform == LiveEnum.BiliBili.value:
        result = BiliBili(content)

    elif platform == LiveEnum.EGame.value:
        result = EGame(content)

    elif platform == LiveEnum.ESport.value:
        result = ESport(content)

    elif platform == LiveEnum.ZhanQi.value:
        result = ZhanQi(content)

    elif platform == LiveEnum.AcFun.value:
        result = AcFun(content)

    elif platform == LiveEnum.LongZhu.value:
        result = LongZhu(content)

    elif platform == LiveEnum.DouYin.value:
        result = DouYin(content)

    elif platform == LiveEnum.KuaiShou.value:
        result = KuaiShou(content)

    elif platform == LiveEnum.IXiGua.value:
        result = IXiGua(content)

    elif platform == LiveEnum.IQiYi.value:
        result = IQiYi(content)

    elif platform == LiveEnum.KuGou.value:
        result = KuGou(content)

    elif platform == LiveEnum.YiZhiBo.value:
        result = YiZhiBo(content)

    elif platform == LiveEnum.YY.value:
        result = YY(content)

    elif platform == LiveEnum.InKe.value:
        result = InKe(content)

    elif platform == LiveEnum.HuoMao.value:
        result = HuoMao(content)

    elif platform == LiveEnum.ImMoMo.value:
        result = ImMoMo(content)

    elif platform == LiveEnum.JD.value:
        result = JD(content)

    elif platform == LiveEnum.RenRen.value:
        result = RenRen(content)

    elif platform == LiveEnum.HuaJiao.value:
        result = HuaJiao(content)

    elif platform == LiveEnum.ChuShou.value:
        result = ChuShou(content)

    elif platform == LiveEnum.WaLi.value:
        result = WaLi(content)

    elif platform == LiveEnum.XunLei.value:
        result = XunLei(content)

    elif platform == LiveEnum.Now.value:
        result = Now(content)

    elif platform == LiveEnum.CC.value:
        result = CC(content)

    elif platform == LiveEnum.PPS.value:
        result = PPS(content)

    elif platform == LiveEnum.V6CN.value:
        result = V6CN(content)

    elif platform == LiveEnum.Live17.value:
        result = Live17(content)

    elif platform == LiveEnum.LaiFeng.value:
        result = LaiFeng(content)

    elif platform == LiveEnum.YouKu.value:
        result = YouKu(content)

    elif platform == LiveEnum.Look.value:
        result = Look(content)

    elif platform == LiveEnum.QF.value:
        result = QF(content)

    elif platform == LiveEnum.ShowSelf.value:
        result = ShowSelf(content)

    elif platform == LiveEnum.WoXiu.value:
        result = WoXiu(content)

    elif platform == LiveEnum.YQS.value:
        result = YQS(content)

    else:
        result = False

    return result


def get_real_url_from_tv_name_content(tv_name, tv_quality):
    """

    :param tv_name:
    :param tv_quality:
    :return:
    """

    return TV.get_tv_url(tv_name, tv_quality)


def get_real_url_from_radio_station_content(radio_station_type, radio_station_id):
    """

    :param radio_station_type:
    :param radio_station_id:
    :return:
    """
    return RadioStation.get_radio_station_url(radio_station_type, radio_station_id)
