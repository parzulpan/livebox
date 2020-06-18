# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QApplication,\
    QDialog
from PyQt5.QtGui import QIcon, QPixmap, QDesktopServices
from PyQt5.QtCore import Qt, QUrl


class AboutWidget(QDialog):
    """

    """
    def __init__(self):
        super(AboutWidget, self).__init__()

        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap('./resources/img/logo@64x64.png'))
        self.logo_content_label = QLabel('网络直播观看平台 V1.0.0')

        self.h_line = QLabel('------------------------------------------------------------------------')

        self.intro_label = QLabel('简介：')
        self.intro_content_label = QLabel(
            'real-live是一个网络直播观看平台，它支持当前几十种主流的直播平台，\n'
            '通过选择直播平台和输入查询信息即可获取直播平台的直播源，可以选择在本平台上在线观看，\n'
            '或者将直播源复制到PotPlayer、VLC等播放器中观看。')

        self.author_label = QLabel("作者：")
        self.author_content_label = QLabel("Parzulpan")

        self.link_label = QLabel("链接：")
        self.link_content_label = QLabel("https://github.com/parzulpan/real-live")
        self.copy_link_btn = QPushButton('访问该链接')
        self.copy_link_btn.clicked.connect(self.answer_copy_link_btn_clicked)

        self.star_label = QLabel("如果觉得本项目不错，可以给个★鼓励哦(●ˇ∀ˇ●)")

        self._init_ui()

    def _init_ui(self):
        """

        :return:
        """
        logo_layout = QHBoxLayout()
        logo_layout.setContentsMargins(5, 5, 5, 5)
        logo_layout.setSpacing(5)
        logo_layout.addStretch()
        logo_layout.addWidget(self.logo_label)
        logo_layout.addWidget(self.logo_content_label)
        logo_layout.addStretch()

        line_layout = QHBoxLayout()
        line_layout.setContentsMargins(5, 5, 5, 5)
        line_layout.setSpacing(5)
        line_layout.addStretch()
        line_layout.addWidget(self.h_line)
        line_layout.addStretch()

        intro_layout = QHBoxLayout()
        intro_layout.setContentsMargins(5, 5, 5, 5)
        intro_layout.setSpacing(5)
        intro_layout.addWidget(self.intro_label)
        intro_layout.addWidget(self.intro_content_label)
        intro_layout.addStretch()

        author_layout = QHBoxLayout()
        author_layout.setContentsMargins(5, 5, 5, 5)
        author_layout.setSpacing(5)
        author_layout.addWidget(self.author_label)
        author_layout.addWidget(self.author_content_label)
        author_layout.addStretch()

        link_layout = QHBoxLayout()
        link_layout.setContentsMargins(5, 5, 5, 5)
        link_layout.setSpacing(5)
        link_layout.addWidget(self.link_label)
        link_layout.addWidget(self.link_content_label)
        link_layout.addWidget(self.copy_link_btn)
        link_layout.addStretch()

        star_layout = QHBoxLayout()
        star_layout.setContentsMargins(5, 5, 5, 5)
        star_layout.setSpacing(5)
        star_layout.addWidget(self.star_label)
        star_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(logo_layout)
        main_layout.addLayout(line_layout)
        main_layout.addLayout(intro_layout)
        main_layout.addLayout(author_layout)
        main_layout.addLayout(link_layout)
        main_layout.addLayout(star_layout)
        self.setLayout(main_layout)

        self.setWindowTitle("关于软件")
        self.setWindowIcon(QIcon('./resources/img/about@64x64.png'))
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    @staticmethod
    def answer_copy_link_btn_clicked():
        """

        :return:
        """
        # clipboard = QApplication.clipboard()
        # clipboard.setText(self.link_content_label.text())
        # # original_text = clipboard.text()
        desktop_services = QDesktopServices()
        desktop_services.openUrl(QUrl("https://github.com/parzulpan/real-live"))
