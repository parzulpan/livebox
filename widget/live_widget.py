# -*- coding: utf-8 -*-
# @Date       : 6/15/2020 
# @Author     : parzulpan
# @Email      : parzulpan@gmail.com
# @Description: 请输入此文件的功能描述
# @Attention  :

import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QApplication
from PyQt5.QtGui import QPixmap, QIcon

from util.get_real_url import get_real_url_from_platform_content


class LiveWidget(QWidget):
    """

    """
    def __init__(self):
        """

        """
        super(LiveWidget, self).__init__()

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
        self.search_content_line_edit = QLineEdit()

        self.get_live_btn = QPushButton('获取直播源')
        self.get_live_btn.clicked.connect(self.answer_get_live_btn_clicked)
        self.live_result_line_edit = QLineEdit()

        self.copy_live_btn = QPushButton('复制直播源')
        self.copy_live_btn.clicked.connect(self.answer_copy_live_btn_clicked)

        self.clean_btn = QPushButton('信息清空')

        self.pot_btn = QPushButton('PotPlayer播放')

        self.vlc_btn = QPushButton('VLC播放')

        self.player_widget = QWidget()
        self.live_null_label = QLabel()
        self.set_player_widget()

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.platform_combobox.addItems(self.platform_list)
        self.search_type_combobox.addItems(self.search_type_list)

        info_layout = QHBoxLayout()
        info_layout.setContentsMargins(10, 10, 10, 10)
        info_layout.setSpacing(5)
        info_layout.addWidget(self.platform_label)
        info_layout.addWidget(self.platform_combobox)
        info_layout.addWidget(self.search_type_label)
        info_layout.addWidget(self.search_type_combobox)
        info_layout.addWidget(self.search_content_line_edit)
        info_layout.addWidget(self.get_live_btn)
        info_layout.addWidget(self.live_result_line_edit)
        info_layout.addWidget(self.copy_live_btn)
        info_layout.addWidget(self.clean_btn)

        player_layout = QVBoxLayout()
        player_layout.setContentsMargins(0, 0, 0, 0)
        player_layout.setSpacing(0)
        player_layout.addWidget(self.player_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(info_layout)
        main_layout.addLayout(player_layout)
        self.setLayout(main_layout)

        self.setWindowTitle("网络直播观看平台")
        self.setWindowIcon(QIcon('../resources/img/logo@48x48.png'))

    def set_player_widget(self, widget=None):
        """

        :param widget:
        :return:
        """
        self.live_null_label.setPixmap(QPixmap("../resources/img/live_null.png"))
        self.live_null_label.setMaximumSize(1920, 1080)
        # self.live_null_label.setVisible(True)
        _layout = QHBoxLayout()
        _layout.setContentsMargins(0, 0, 0, 0)
        _layout.setSpacing(0)
        _layout.addWidget(self.live_null_label)
        self.player_widget.setLayout(_layout)

    def answer_platform_combobox_current_index_changed(self, index):
        """

        :param index:
        :return:
        """
        pass

    def answer_search_type_combobox_current_index_changed(self, index):
        """

        :param index:
        :return:
        """
        pass

    def answer_get_live_btn_clicked(self):
        """

        :return:
        """
        content = self.search_content_line_edit.text()
        result = get_real_url_from_platform_content(self.platform_combobox.currentIndex(), content)
        self.live_result_line_edit.setText(result)

    def answer_copy_live_btn_clicked(self):
        """

        :return:
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.live_result_line_edit.text())
        # original_text = clipboard.text()

    def answer_clean_btn_clicked(self):
        """

        :return:
        """
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    live_widget = LiveWidget()
    live_widget.show()
    sys.exit(app.exec_())
