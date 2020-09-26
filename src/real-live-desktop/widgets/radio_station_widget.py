# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 广播电台页面

@Attention :
"""

import sys

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QApplication,\
    QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal

from utils.common import PromptBox, get_window_center_point
from utils.enums import PlayerEnum
from utils.get_real_url import get_real_url_from_radio_station_content


class RadioStationWidget(QDialog):
    """

    """
    listen_radio_station_signal = pyqtSignal(str, str)
    """在线收听"""

    def __init__(self):
        super(RadioStationWidget, self).__init__()

        self.radio_station_type_label = QLabel('电台类别: ')
        self.radio_station_type_combobox = QComboBox()
        self.radio_station_type_combobox.currentIndexChanged.connect(
            self.answer_radio_station_type_combobox_current_index_changed)
        self.radio_station_type_list = ['通用', '地方']

        self.radio_station_id_label = QLabel('电台频道: ')
        self.radio_station_id_combobox = QComboBox()
        self.radio_station_id_combobox.currentIndexChanged.connect(
            self.answer_radio_station_id_combobox_current_index_changed)
        self.universal_radio_station_id_list = ["中国交通广播",
                                                "环球资讯广播 FM90.5",
                                                "中文环球广播",
                                                "经典音乐广播 101.8",
                                                "哈语广播",
                                                "藏语广播",
                                                "维语广播",
                                                "中国乡村之声",
                                                "经济之声",
                                                "中国之声",
                                                "音乐之声",
                                                "中华之声",
                                                "神州之声",
                                                "华夏之声",
                                                "香港之声",
                                                "文艺之声",
                                                "老年之声",
                                                "闽南之音",
                                                "南海之声",
                                                "客家之声",
                                                "海峡飞虹",
                                                "轻松调频 FM91.5",
                                                "Hit FM FM88.7", ]
        self.local_radio_station_id_list = ["北京新闻广播 FM100.6",
                                            "北京音乐广播 FM97.4",
                                            "北京交通广播 FM103.9",
                                            "北京文艺广播 FM87.6",
                                            "北京欢乐时光 FM106.5",
                                            "北京怀旧金曲 FM107.5",
                                            "北京古典音乐 FM98.6",
                                            "北京教学广播 FM99.4",
                                            "北京长书广播 FM104.3",
                                            "北京戏曲曲艺 FM105.1",
                                            "北京房山经典音乐 FM96.9",
                                            "北京好音乐 FM95.9",
                                            "重庆新闻广播 FM96.8",
                                            "重庆经济广播 FM101.5",
                                            "重庆交通广播 FM95.5",
                                            "重庆音乐广播 FM88.1",
                                            "重庆都市广播 FM93.8",
                                            "重庆文艺广播 FM103.5",
                                            "巴渝之声 FM104.5"
                                            "南川人民广播电台 FM107.0",
                                            "万盛旅游交通广播 FM92.2",
                                            "万州交通广播",
                                            "福建新闻广播 FM103.6",
                                            "福建经济广播 FM96.1",
                                            "福建音乐广播 FM91.3",
                                            "福建交通广播 FM100.7",
                                            "福建东南广播 AM585",
                                            "福建私家车广播 FM98.7",
                                            "甘肃新闻综合广播 FM96.1",
                                            "甘肃都市调频 FM106.6",
                                            "甘肃交通广播 FM93.4",
                                            "甘肃经济广播 FM93.4",
                                            "甘肃农村广播 FM92.2",
                                            "兰州新闻综合广播 FM97.3",
                                            "兰州交通音乐广播 FM99.5",
                                            "兰州生活文艺广播 FM100.8",
                                            "广东新闻频道 FM91.4",
                                            "广东珠江经济台 FM97.4",
                                            "广东音乐之声 FM99.3",
                                            "广东城市之声 FM103.6",
                                            "广东南方生活广播 FM93.6",
                                            "广东羊城交通广播 FM105.2",
                                            "广东文体广播 FM107.7",
                                            "广东股市广播 FM95.3",
                                            "广东优悦广播 FM105.7",
                                            "广州新闻电台 FM96.2",
                                            "广州汽车音乐电台 FM102.7",
                                            "广州交通电台 FM106.1",
                                            "东莞音乐广播 FM104",
                                            "东莞交通广播",
                                            "当涂人民广播电台 FM90.1", ]

        self.search_result_label = QLabel('获取结果: ')
        self.audio_result_line_edit = QLineEdit()
        self.audio_result_line_edit.setReadOnly(True)

        self.get_audio_btn = QPushButton('获取音频源')
        self.get_audio_btn.clicked.connect(self.answer_get_audio_btn_clicked)
        self.copy_audio_btn = QPushButton('复制音频源')
        self.copy_audio_btn.setDisabled(True)
        self.copy_audio_btn.clicked.connect(self.answer_copy_audio_btn_clicked)
        self.listen_audio_btn = QPushButton('在线收听')
        self.listen_audio_btn.setDisabled(True)
        self.listen_audio_btn.clicked.connect(self.answer_watch_audio_btn_clicked)
        self.clean_btn = QPushButton('信息清空')
        self.clean_btn.clicked.connect(self.answer_clean_btn_clicked)

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.radio_station_type_combobox.addItems(self.radio_station_type_list)
        self.radio_station_id_combobox.addItems(self.universal_radio_station_id_list)

        radio_station_type_layout = QHBoxLayout()
        radio_station_type_layout.setContentsMargins(10, 10, 10, 10)
        radio_station_type_layout.setSpacing(5)
        radio_station_type_layout.addWidget(self.radio_station_type_label)
        radio_station_type_layout.addWidget(self.radio_station_type_combobox)
        radio_station_type_layout.addStretch()

        radio_station_id_layout = QHBoxLayout()
        radio_station_id_layout.setContentsMargins(10, 10, 10, 10)
        radio_station_id_layout.setSpacing(5)
        radio_station_id_layout.addWidget(self.radio_station_id_label)
        radio_station_id_layout.addWidget(self.radio_station_id_combobox)
        radio_station_id_layout.addStretch()

        search_result_layout = QHBoxLayout()
        search_result_layout.setContentsMargins(10, 10, 10, 10)
        search_result_layout.setSpacing(5)
        search_result_layout.addWidget(self.search_result_label)
        search_result_layout.addWidget(self.audio_result_line_edit)
        search_result_layout.addWidget(self.get_audio_btn)
        search_result_layout.addWidget(self.copy_audio_btn)
        search_result_layout.addWidget(self.listen_audio_btn)
        search_result_layout.addWidget(self.clean_btn)
        search_result_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(radio_station_type_layout)
        main_layout.addLayout(radio_station_id_layout)
        main_layout.addLayout(search_result_layout)
        self.setLayout(main_layout)

        self.setWindowTitle("广播电台")
        self.setWindowIcon(QIcon('./resources/img/radio_station@64x64.png'))
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def answer_radio_station_type_combobox_current_index_changed(self, index):
        """

        :param index:
        :return:
        """
        self.radio_station_id_combobox.clear()
        if index == 0:
            self.radio_station_id_combobox.addItems(self.universal_radio_station_id_list)
        else:
            self.radio_station_id_combobox.addItems(self.local_radio_station_id_list)
        self.copy_audio_btn.setDisabled(True)
        self.listen_audio_btn.setDisabled(True)

    def answer_radio_station_id_combobox_current_index_changed(self, index):
        """

        :param index:
        :return:
        """
        self.copy_audio_btn.setDisabled(True)
        self.listen_audio_btn.setDisabled(True)

    def answer_get_audio_btn_clicked(self):
        """

        :return:
        """
        result = get_real_url_from_radio_station_content(self.radio_station_type_combobox.currentText(),
                                                         self.radio_station_id_combobox.currentText())
        print("search result: ", result)
        if result:
            self.audio_result_line_edit.setText(result)
            self.copy_audio_btn.setDisabled(False)
            self.listen_audio_btn.setDisabled(False)
        else:
            self.copy_audio_btn.setDisabled(True)
            self.listen_audio_btn.setDisabled(True)
            _box = PromptBox(2, "获取结果失败!", 1)
            width, height = get_window_center_point(_box)
            _box.move(width, height)
            _box.exec_()

    def answer_copy_audio_btn_clicked(self):
        """

        :return:
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.audio_result_line_edit.text())
        _box = PromptBox(0, "已复制音频源到剪切板!", 1)
        width, height = get_window_center_point(_box)
        _box.move(width, height)
        _box.exec_()

    def answer_watch_audio_btn_clicked(self):
        """

        :return:
        """
        self.close()
        self.listen_radio_station_signal.emit(self.audio_result_line_edit.text(), PlayerEnum.MrlTypeRS.value[1])

    def answer_clean_btn_clicked(self):
        """

        :return:
        """
        self.radio_station_type_combobox.setCurrentIndex(0)
        self.radio_station_id_combobox.setCurrentIndex(0)
        self.audio_result_line_edit.clear()
        self.copy_audio_btn.setDisabled(True)
        self.listen_audio_btn.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    radio_station_widget = RadioStationWidget()
    radio_station_widget.show()
    sys.exit(app.exec_())
