# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""
import sys

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QApplication,\
    QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal

from utils.common import PromptBox, get_window_center_point
from utils.get_real_url import get_real_url_from_radio_station_content


class RadioStationWidget(QDialog):
    """

    """
    listen_radio_station_signal = pyqtSignal(str)
    """在线观看"""

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
        self.radio_station_id_list = ['环球资讯广播 FM90.5', '中文环球广播']

        self.search_result_label = QLabel('获取结果: ')
        self.audio_result_line_edit = QLineEdit()
        # self.audio_result_line_edit.setReadOnly(True)

        self.get_audio_btn = QPushButton('获取音频源')
        self.get_audio_btn.clicked.connect(self.answer_get_audio_btn_clicked)
        self.copy_audio_btn = QPushButton('复制音频源')
        self.copy_audio_btn.setDisabled(True)
        self.copy_audio_btn.clicked.connect(self.answer_copy_audio_btn_clicked)
        self.watch_audio_btn = QPushButton('在线观看')
        self.watch_audio_btn.setDisabled(True)
        self.watch_audio_btn.clicked.connect(self.answer_watch_audio_btn_clicked)
        self.clean_btn = QPushButton('信息清空')
        self.clean_btn.clicked.connect(self.answer_clean_btn_clicked)

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.radio_station_type_combobox.addItems(self.radio_station_type_list)
        self.radio_station_id_combobox.addItems(self.radio_station_id_list)

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
        search_result_layout.addWidget(self.watch_audio_btn)
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
        self.copy_audio_btn.setDisabled(True)
        self.watch_audio_btn.setDisabled(True)

    def answer_radio_station_id_combobox_current_index_changed(self, index):
        """

        :param index:
        :return:
        """
        self.copy_audio_btn.setDisabled(True)
        self.watch_audio_btn.setDisabled(True)

    def answer_get_audio_btn_clicked(self):
        """

        :return:
        """
        result = get_real_url_from_radio_station_content(self.radio_station_type_combobox.currentText(),
                                                         self.radio_station_id_combobox.currentIndex())
        print("search result: ", result)
        if result:
            self.audio_result_line_edit.setText(result)
            self.copy_audio_btn.setDisabled(False)
            self.watch_audio_btn.setDisabled(False)
        else:
            self.copy_audio_btn.setDisabled(True)
            self.watch_audio_btn.setDisabled(True)
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
        self.listen_radio_station_signal.emit(self.audio_result_line_edit.text())

    def answer_clean_btn_clicked(self):
        """

        :return:
        """
        self.radio_station_type_combobox.setCurrentIndex(0)
        self.radio_station_id_combobox.setCurrentIndex(0)
        self.audio_result_line_edit.clear()
        self.copy_audio_btn.setDisabled(True)
        self.watch_audio_btn.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    radio_station_widget = RadioStationWidget()
    radio_station_widget.show()
    sys.exit(app.exec_())
