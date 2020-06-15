# -*- coding: utf-8 -*-
# @Date       : 6/15/2020 
# @Author     : parzulpan
# @Email      : parzulpan@gmail.com
# @Description: 请输入此文件的功能描述
# @Attention  :

from util.live_enum import LiveEnum
import real_url.douyu as Douyu
import real_url.huya as Huya
import real_url.bilibili as Bilibili
import real_url.zhanqi as Zhanqi
import real_url.cc as Cc
import real_url.huomao as Huomao
import real_url.egame as Egame
import real_url.yy as Yy
import real_url.yizhibo as Yizhibo
import real_url.kuaishou as Kuaishou
import real_url.huajiao as Huajiao
import real_url.inke as Inke
import real_url.ixigua as Ixigua
import real_url.chushou as Chushou
import real_url.now as Now
import real_url.douyin as Douyin
import real_url.iqiyi as Iqiyi
import real_url.kugou as Kugou
import real_url.longzhu as Longzhu
import real_url.pps as Pps
import real_url.v6cn as V6cn
import real_url.live17 as Live17
import real_url.laifeng as Laifeng
import real_url.youku as Youku
import real_url.look as Look
import real_url.qf as Qf


def get_real_url_from_platform_content(platform, content):
    """

    :param platform:
    :param content:
    :return:
    """

    if platform == LiveEnum.Douyu.value:
        result = Douyu.get_real_url(content)

    elif platform == LiveEnum.Huya.value:
        result = Huya.get_real_url(content)

    elif platform == LiveEnum.Bilibili.value:
        result = Bilibili.get_real_url_flv(content)

    elif platform == LiveEnum.Zhanqi.value:
        result = Zhanqi.get_real_url(content)

    elif platform == LiveEnum.Cc.value:
        result = Cc.get_real_url(content)

    elif platform == LiveEnum.Huomao.value:
        result = Huomao.get_real_url(content)

    elif platform == LiveEnum.Egame.value:
        result = Egame.get_real_url(content)

    elif platform == LiveEnum.Yy.value:
        result = Yy.get_real_url(content)

    elif platform == LiveEnum.Yizhibo.value:
        result = Yizhibo.get_real_url(content)

    elif platform == LiveEnum.Kuaishou.value:
        result = Kuaishou.get_real_url(content)

    elif platform == LiveEnum.Huajiao.value:
        result = Huajiao.get_real_url(content)

    elif platform == LiveEnum.Inke.value:
        result = Inke.get_real_url(content)

    elif platform == LiveEnum.Ixigua.value:
        result = Ixigua.get_real_url(content)

    elif platform == LiveEnum.Chushou.value:
        result = Chushou.get_real_url(content)

    elif platform == LiveEnum.Now.value:
        result = Now.get_real_url(content)

    elif platform == LiveEnum.Douyin.value:
        result = Douyin.get_real_url(content)

    elif platform == LiveEnum.Iqiyi.value:
        result = Iqiyi.get_real_url(content)

    elif platform == LiveEnum.Kugou.value:
        result = Kugou.get_real_url(content)

    elif platform == LiveEnum.Longzhu.value:
        result = Longzhu.get_real_url(content)

    elif platform == LiveEnum.Pps.value:
        result = Pps.get_real_url(content)

    elif platform == LiveEnum.V6cn.value:
        result = V6cn.get_real_url(content)

    elif platform == LiveEnum.Live17.value:
        result = Live17.get_real_url(content)

    elif platform == LiveEnum.Laifeng.value:
        result = Laifeng.get_real_url(content)

    elif platform == LiveEnum.Youku.value:
        result = Youku.get_real_url(content)

    elif platform == LiveEnum.Look.value:
        result = Look.get_real_url(content)

    elif platform == LiveEnum.Qf.value:
        result = Qf.get_real_url(content)

    else:
        result = ""
        pass

    return result
