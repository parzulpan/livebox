# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""

tv_url_dict = {"CCTV-1 综合": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv1hd",
               "CCTV-2 财经": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv2hd",
               "CCTV-3 综艺": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv3hd",
               "CCTV-4 中文国际": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv4hd",
               "CCTV-5 体育": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv5hd",
               "CCTV-5 +": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv5phd",
               "CCTV-6 电影": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv6hd",
               "CCTV-7 军事农业": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv7hd",
               "CCTV-8 电视剧": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv8hd",
               "CCTV-9 记录": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv9hd",
               "CCTV-10 科教": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv10hd",
               "CCTV-12 社会与法": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv12hd",
               "CCTV-14H 少儿": "rtmp://ivi.bupt.edu.cn:1935/livetv/cctv14hd",
               "CCTV-第一剧场": "rtmp://ivi.bupt.edu.cn:1935/livetv/dyjctv",
               "CCTV-国防军事": "rtmp://ivi.bupt.edu.cn:1935/livetv/gfjstv",
               "CCTV-怀旧剧场": "rtmp://ivi.bupt.edu.cn:1935/livetv/hjjctv",
               "CCTV-风云剧场": "rtmp://ivi.bupt.edu.cn:1935/livetv/fyjctv",
               "CCTV-风云足球": "rtmp://ivi.bupt.edu.cn:1935/livetv/fyzqtv",
               "CCTV-风云音乐": "rtmp://ivi.bupt.edu.cn:1935/livetv/fyyytv",
               "CCTV-世界地理": "rtmp://ivi.bupt.edu.cn:1935/livetv/sjdltv",
               "北京卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/btv1hd",
               "安徽卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/ahhd",
               "重庆卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/cqhd",
               "东方卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/dfhd",
               "天津卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/tjhd",
               "东南卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/dnhd",
               "江西卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/jxhd",
               "河北卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/hebhd",
               "湖南卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/hunanhd",
               "湖北卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/hbhd",
               "辽宁卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/lnhd",
               "四川卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/schd",
               "江苏卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/jshd",
               "浙江卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/zjhd",
               "山东卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/sdhd",
               "广东卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/gdhd",
               "深圳卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/szhd",
               "黑龙江卫视": "rtmp://ivi.bupt.edu.cn:1935/livetv/hljhd",
               "CHC电影": "rtmp://ivi.bupt.edu.cn:1935/livetv/chchd", }


def get_tv_url(tv_name, tv_quality):
    """

    :param tv_name:
    :param tv_quality:
    :return:
    """
    return tv_url_dict[tv_name]
