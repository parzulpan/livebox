# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 高清电视页面

@Attention :
"""

import sys

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QApplication,\
    QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal

from utils.common import PromptBox, get_window_center_point
from utils.get_real_url import get_real_url_from_tv_name_content


class TvWidget(QDialog):
    """

    """
    watch_live_signal = pyqtSignal(str)
    """在线观看"""

    def __init__(self):
        super(TvWidget, self).__init__()

        self.tv_name_label = QLabel('电视频道: ')
        self.tv_name_combobox = QComboBox()
        self.tv_name_combobox.currentIndexChanged.connect(self.answer_tv_name_combobox_current_index_changed)
        self.tv_name_list = ["CCTV-1 综合",
                             "CCTV-2 财经",
                             "CCTV-3 综艺",
                             "CCTV-4 中文国际",
                             "CCTV-5 体育",
                             "CCTV-5 +",
                             "CCTV-6 电影",
                             "CCTV-7 军事农业",
                             "CCTV-8 电视剧",
                             "CCTV-9 记录",
                             "CCTV-10 科教",
                             "CCTV-12 社会与法",
                             "CCTV-14 少儿",
                             "CCTV-第一剧场",
                             "CCTV-国防军事",
                             "CCTV-怀旧剧场",
                             "CCTV-风云剧场",
                             "CCTV-风云足球",
                             "CCTV-风云音乐",
                             "CCTV-世界地理",
                             "北京卫视",
                             "安徽卫视",
                             "重庆卫视",
                             "东方卫视",
                             "天津卫视",
                             "东南卫视",
                             "江西卫视",
                             "河北卫视",
                             "湖南卫视",
                             "湖北卫视",
                             "辽宁卫视",
                             "四川卫视",
                             "江苏卫视",
                             "浙江卫视",
                             "山东卫视",
                             "广东卫视",
                             "深圳卫视",
                             "黑龙江卫视",
                             "NewsTV-爱情喜剧",
                             "NewsTV-搏击",
                             "NewsTV-潮妈辣婆",
                             "NewsTV-动画王国",
                             "NewsTV-古装剧场",
                             "NewsTV-海外剧场",
                             "NewsTV-家庭剧场",
                             "NewsTV-健康有约",
                             "NewsTV-金牌综艺",
                             "NewsTV-惊悚悬疑",
                             "NewsTV-精品大剧",
                             "NewsTV-精品电影",
                             "NewsTV-精品记录",
                             "NewsTV-精品体育",
                             "NewsTV-军旅剧场",
                             "NewsTV-军事评论",
                             "NewsTV-明星大片",
                             "NewsTV-农业致富",
                             "NewsTV-完美游戏",
                             "NewsTV-中国功夫",
                             "CHC电影", ]

        self.tv_quality_label = QLabel('电视画质: ')
        self.tv_quality_combobox = QComboBox()
        self.tv_quality_combobox.currentIndexChanged.connect(self.answer_tv_quality_combobox_current_index_changed)
        self.tv_quality_list = ['高清', '普通']

        self.search_result_label = QLabel('获取结果: ')
        self.live_result_line_edit = QLineEdit()
        self.live_result_line_edit.setReadOnly(True)

        self.get_live_btn = QPushButton('获取电视源')
        self.get_live_btn.clicked.connect(self.answer_get_live_btn_clicked)
        self.copy_live_btn = QPushButton('复制电视源')
        self.copy_live_btn.setDisabled(True)
        self.copy_live_btn.clicked.connect(self.answer_copy_live_btn_clicked)
        self.watch_live_btn = QPushButton('在线观看')
        self.watch_live_btn.setDisabled(True)
        self.watch_live_btn.clicked.connect(self.answer_watch_live_btn_clicked)
        self.clean_btn = QPushButton('信息清空')
        self.clean_btn.clicked.connect(self.answer_clean_btn_clicked)

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.tv_name_combobox.addItems(self.tv_name_list)
        self.tv_quality_combobox.addItems(self.tv_quality_list)

        tv_name_layout = QHBoxLayout()
        tv_name_layout.setContentsMargins(10, 10, 10, 10)
        tv_name_layout.setSpacing(5)
        tv_name_layout.addWidget(self.tv_name_label)
        tv_name_layout.addWidget(self.tv_name_combobox)
        tv_name_layout.addStretch()

        tv_quality_layout = QHBoxLayout()
        tv_quality_layout.setContentsMargins(10, 10, 10, 10)
        tv_quality_layout.setSpacing(5)
        tv_quality_layout.addWidget(self.tv_quality_label)
        tv_quality_layout.addWidget(self.tv_quality_combobox)
        tv_quality_layout.addStretch()

        search_result_layout = QHBoxLayout()
        search_result_layout.setContentsMargins(10, 10, 10, 10)
        search_result_layout.setSpacing(5)
        search_result_layout.addWidget(self.search_result_label)
        search_result_layout.addWidget(self.live_result_line_edit)
        search_result_layout.addWidget(self.get_live_btn)
        search_result_layout.addWidget(self.copy_live_btn)
        search_result_layout.addWidget(self.watch_live_btn)
        search_result_layout.addWidget(self.clean_btn)
        search_result_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(tv_name_layout)
        main_layout.addLayout(tv_quality_layout)
        main_layout.addLayout(search_result_layout)
        self.setLayout(main_layout)

        self.setWindowTitle("高清电视")
        self.setWindowIcon(QIcon('./resources/img/tv@64x64.png'))
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def answer_tv_name_combobox_current_index_changed(self, index):
        """

        :param index:
        :return:
        """
        self.copy_live_btn.setDisabled(True)
        self.watch_live_btn.setDisabled(True)

    def answer_tv_quality_combobox_current_index_changed(self, index):
        """

        :param index:
        :return:
        """
        self.copy_live_btn.setDisabled(True)
        self.watch_live_btn.setDisabled(True)

    def answer_get_live_btn_clicked(self):
        """

        :return:
        """
        result = get_real_url_from_tv_name_content(self.tv_name_combobox.currentText(),
                                                   self.tv_quality_combobox.currentIndex())
        print("search result: ", result)
        if result:
            self.live_result_line_edit.setText(result)
            self.copy_live_btn.setDisabled(False)
            self.watch_live_btn.setDisabled(False)
        else:
            self.copy_live_btn.setDisabled(True)
            self.watch_live_btn.setDisabled(True)
            _box = PromptBox(2, "获取频道结果失败!", 1)
            width, height = get_window_center_point(_box)
            _box.move(width, height)
            _box.exec_()

    def answer_copy_live_btn_clicked(self):
        """

        :return:
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.live_result_line_edit.text())
        _box = PromptBox(0, "已复制直播源到剪切板!", 1)
        width, height = get_window_center_point(_box)
        _box.move(width, height)
        _box.exec_()

    def answer_watch_live_btn_clicked(self):
        """

        :return:
        """
        self.close()
        self.watch_live_signal.emit(self.live_result_line_edit.text())

    def answer_clean_btn_clicked(self):
        """

        :return:
        """
        self.tv_name_combobox.setCurrentIndex(0)
        self.tv_quality_combobox.setCurrentIndex(0)
        self.live_result_line_edit.clear()
        self.copy_live_btn.setDisabled(True)
        self.watch_live_btn.setDisabled(True)
