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

from utils.get_real_url import get_real_url_from_platform_content
from utils.common import PromptBox, get_window_center_point


class SearchWidget(QDialog):
    """

    """
    watch_live_signal = pyqtSignal(str)
    """在线观看"""

    def __init__(self):
        super(SearchWidget, self).__init__()
        self.platform_label = QLabel('直播平台: ')
        self.platform_combobox = QComboBox()
        self.platform_combobox.currentIndexChanged.connect(self.answer_platform_combobox_current_index_changed)
        self.platform_list = ["斗鱼直播", "虎牙直播", "哔哩哔哩直播", "战旗直播", "网易CC直播", "火猫直播", "企鹅电竞", "YY直播", "一直播", "快手直播", "花椒直播",
                              "映客直播", "西瓜直播", "触手直播", "NOW直播", "抖音直播", "爱奇艺直播", "酷狗直播", "龙珠直播", "PPS奇秀直播", "六间房",
                              "17直播",
                              "来疯直播", "优酷轮播台", "网易LOOK直播", "千帆直播"]
        self.platform_result = None

        self.search_type_label = QLabel('搜索类型: ')
        self.search_type_combobox = QComboBox()
        self.search_type_combobox.currentIndexChanged.connect(self.answer_search_type_combobox_current_index_changed)
        self.search_type_list = ["房间号", "主播名"]

        self.search_content_label = QLabel('搜索内容: ')
        self.search_content_line_edit = QLineEdit()
        self.get_live_btn = QPushButton('获取直播源')
        self.get_live_btn.clicked.connect(self.answer_get_live_btn_clicked)

        self.search_result_label = QLabel('搜索结果: ')
        self.live_result_line_edit = QLineEdit()
        self.live_result_line_edit.setReadOnly(True)
        self.copy_live_btn = QPushButton('复制直播源')
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
        self.platform_combobox.addItems(self.platform_list)
        self.search_type_combobox.addItems(self.search_type_list)

        platform_layout = QHBoxLayout()
        platform_layout.setContentsMargins(10, 10, 10, 10)
        platform_layout.setSpacing(5)
        platform_layout.addWidget(self.platform_label)
        platform_layout.addWidget(self.platform_combobox)
        platform_layout.addStretch()

        search_type_layout = QHBoxLayout()
        search_type_layout.setContentsMargins(10, 10, 10, 10)
        search_type_layout.setSpacing(5)
        search_type_layout.addWidget(self.search_type_label)
        search_type_layout.addWidget(self.search_type_combobox)
        search_type_layout.addStretch()

        search_content_layout = QHBoxLayout()
        search_content_layout.setContentsMargins(10, 10, 10, 10)
        search_content_layout.setSpacing(5)
        search_content_layout.addWidget(self.search_content_label)
        search_content_layout.addWidget(self.search_content_line_edit)
        search_content_layout.addWidget(self.get_live_btn)
        search_content_layout.addStretch()

        search_result_layout = QHBoxLayout()
        search_result_layout.setContentsMargins(10, 10, 10, 10)
        search_result_layout.setSpacing(5)
        search_result_layout.addWidget(self.search_result_label)
        search_result_layout.addWidget(self.live_result_line_edit)
        search_result_layout.addWidget(self.copy_live_btn)
        search_result_layout.addWidget(self.watch_live_btn)
        search_result_layout.addWidget(self.clean_btn)
        search_result_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(platform_layout)
        main_layout.addLayout(search_type_layout)
        main_layout.addLayout(search_content_layout)
        main_layout.addLayout(search_result_layout)
        self.setLayout(main_layout)

        self.setWindowTitle("信息搜索")
        self.setWindowIcon(QIcon('./resources/img/search@64x64.png'))
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def answer_platform_combobox_current_index_changed(self, index):
        """

        :param index:
        :return:
        """
        self.copy_live_btn.setDisabled(True)
        self.watch_live_btn.setDisabled(True)

    def answer_search_type_combobox_current_index_changed(self, index):
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
        content = self.search_content_line_edit.text()
        if content:
            result = get_real_url_from_platform_content(self.platform_combobox.currentIndex(), content)
            print("search result: ", result)
            if 'http' in result:
                self.live_result_line_edit.setText(result)
                self.copy_live_btn.setDisabled(False)
                self.watch_live_btn.setDisabled(False)
            else:
                self.copy_live_btn.setDisabled(True)
                self.watch_live_btn.setDisabled(True)
                _box = PromptBox(2, "直播间未开播或不存在!", 1)
                width, height = get_window_center_point(_box)
                _box.move(width, height)
                _box.exec_()
        else:
            _box = PromptBox(3, "输入内容不能为空!", 1)
            width, height = get_window_center_point(_box)
            _box.move(width, height)
            _box.exec_()

    def answer_copy_live_btn_clicked(self):
        """

        :return:
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.live_result_line_edit.text())
        # original_text = clipboard.text()
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
        self.platform_combobox.setCurrentIndex(0)
        self.search_type_combobox.setCurrentIndex(0)
        self.search_content_line_edit.clear()
        self.live_result_line_edit.clear()
        self.copy_live_btn.setDisabled(True)
        self.watch_live_btn.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    search_widget = SearchWidget()
    search_widget.show()
    sys.exit(app.exec_())
