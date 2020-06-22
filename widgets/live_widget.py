# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication

from widgets.vlc_widget import VLCWidget


class LiveWidget(QWidget):
    """

    """
    def __init__(self):
        """

        """
        super(LiveWidget, self).__init__()

        self.pot_btn = QPushButton('PotPlayer播放')

        self.vlc_btn = QPushButton('VLC播放')
        self.vlc_widget = VLCWidget()

        self.player_widget = QWidget()
        self.player_layout = QVBoxLayout()
        self._layout = QVBoxLayout()

        self.set_player_widget()

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        # player_layout = QVBoxLayout()
        self.player_layout.setContentsMargins(0, 0, 0, 0)
        self.player_layout.setSpacing(0)
        self.player_layout.addWidget(self.player_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(self.player_layout)
        self.setLayout(main_layout)

        self.setStyleSheet("background-image:url(./resources/img/live_null.png); ")

    def clear_layout(self):
        """

        :return:
        """
        for i in range(self._layout.count()):
            print("i {0}".format(i))
            self._layout.removeItem(self._layout.itemAt(i))
        self._layout.setParent(None)
        self.player_layout.removeItem(self._layout)

    def set_widget_visible(self, visible):
        """

        :return:
        """
        if visible:
            # self.vlc_widget.setVisible(True)
            self.vlc_widget.show()
        else:
            # self.vlc_widget.setVisible(False)
            self.vlc_widget.hide()

    def set_player_widget(self, is_visible=False):
        """

        :param is_visible:
        :return:
        """
        # self.clear_layout()

        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self.vlc_widget)

        self.set_widget_visible(is_visible)

        self.player_widget.setLayout(self._layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    live_widget = LiveWidget()
    live_widget.show()
    sys.exit(app.exec_())
