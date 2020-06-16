# -*- coding: utf-8 -*-
# @Date       : 6/15/2020 
# @Author     : parzulpan
# @Email      : parzulpan@gmail.com
# @Description: 请输入此文件的功能描述
# @Attention  :

import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QApplication
from PyQt5.QtGui import QPixmap


class LiveWidget(QWidget):
    """

    """
    def __init__(self):
        """

        """
        super(LiveWidget, self).__init__()

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
        player_layout = QVBoxLayout()
        player_layout.setContentsMargins(0, 0, 0, 0)
        player_layout.setSpacing(0)
        player_layout.addWidget(self.player_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(player_layout)
        self.setLayout(main_layout)

    def set_player_widget(self, widget=None):
        """

        :param widget:
        :return:
        """
        self.live_null_label.setPixmap(QPixmap("./resources/img/live_null.png"))
        # self.live_null_label.setMaximumSize(1920, 1080)
        # self.live_null_label.setVisible(True)
        _layout = QHBoxLayout()
        _layout.setContentsMargins(0, 0, 0, 0)
        _layout.setSpacing(0)
        _layout.addWidget(self.live_null_label)
        self.player_widget.setLayout(_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    live_widget = LiveWidget()
    live_widget.show()
    sys.exit(app.exec_())
