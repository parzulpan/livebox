# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QDialog, QFrame
from PyQt5.QtGui import QIcon, QPixmap, QDesktopServices
from PyQt5.QtCore import Qt, QUrl

from utils.crud_cfg import *


class AboutWidget(QDialog):
    """

    """
    def __init__(self):
        super(AboutWidget, self).__init__()

        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap(PathHelper.get_img_path("logo@64x64.png")))
        title = retrieve_content("software_info", "software_name") + " " + retrieve_content("software_info",
                                                                                            "software_version")
        self.logo_content_label = QLabel(title)

        self.h_line = QFrame()
        self.h_line.setFrameShape(QFrame.HLine)
        self.h_line.setFrameShadow(QFrame.Sunken)

        self.intro_content_label = QLabel("简介：real-live是网络直播聚合平台，支持视频直播、高清电视和广播电台等。\n"
                                          "通过输入查询信息即可获取相应的直播源，可以选择在本平台上在线欣赏，\n"
                                          "在线播放器分为采用FFmpeg+SDL自研的RealPlayer和开源的VLC接口封装的VLCPlayer，\n"
                                          "选择一种自己喜欢的Player即可。或者将直播源复制到PotPlayer、VLC等播放器中进行欣赏。")

        self.author_content_label = QLabel("作者：Parzulpan")

        self.link_content_label = QLabel("链接：https://github.com/parzulpan/real-live")
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

        intro_layout = QHBoxLayout()
        intro_layout.setContentsMargins(5, 5, 5, 5)
        intro_layout.setSpacing(5)
        intro_layout.addWidget(self.intro_content_label)
        intro_layout.addStretch()

        author_layout = QHBoxLayout()
        author_layout.setContentsMargins(5, 5, 5, 5)
        author_layout.setSpacing(5)
        author_layout.addWidget(self.author_content_label)
        author_layout.addStretch()

        link_layout = QHBoxLayout()
        link_layout.setContentsMargins(5, 5, 5, 5)
        link_layout.setSpacing(5)
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
        main_layout.addWidget(self.h_line)
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
