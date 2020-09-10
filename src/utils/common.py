# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""

from PyQt5.QtWidgets import QDesktopWidget, QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from utils.path_helper import PathHelper


def get_window_center_point(widget):
    """ 使窗口居中显示

    :param widget: 需要居中显示的窗口
    :return:
    """
    desktop_widget = QDesktopWidget()
    screen_rect = desktop_widget.screenGeometry()
    return (screen_rect.width()-widget.width()) / 2, (screen_rect.height()-widget.height()) / 2


class PromptBox(QDialog):
    """ 通用提示弹窗

    """
    def __init__(self, box_type: int, content: str, btn_cnt: int = 1):
        """

        :param box_type: 提示弹窗类型，0代表成功提示弹窗，1代表询问提示弹窗，2代表警告提示弹窗，3代表错误提示弹窗
        :param content: 提示弹窗的文本信息，注意:当文本过长时,可用\n将文本换行
        :param btn_cnt: 提示弹窗类型的按钮个数，1代表有一个按钮，2代表有两个按钮，默认为1
        :return: True or False
        """
        super(PromptBox, self).__init__()
        self._icon_label = QLabel()
        # self._icon_label.setFixedSize(48, 48)

        self._content_label = QLabel(content)

        self._btn_one = QPushButton("确 定")
        self._btn_one.clicked.connect(self.answer_btn_one_clicked)
        self._btn_two = QPushButton("取 消")
        self._btn_two.clicked.connect(self.answer_btn_two_clicked)

        self._btn_layout = QHBoxLayout()
        self._btn_layout.setContentsMargins(5, 5, 5, 5)
        self._btn_layout.setSpacing(10)
        self._btn_layout.addStretch()

        if box_type == 0:
            self._icon_label.setPixmap(QPixmap(PathHelper.get_img_path("box_success@32x32.png")))
        elif box_type == 1:
            self._icon_label.setPixmap(QPixmap(PathHelper.get_img_path("box_question@32x32.png")))
        elif box_type == 2:
            self._icon_label.setPixmap(QPixmap(PathHelper.get_img_path("box_warning@32x32.png")))
        elif box_type == 3:
            self._icon_label.setPixmap(QPixmap(PathHelper.get_img_path("box_error@32x32.png")))
        else:
            pass

        if btn_cnt == 1:
            self._btn_layout.addWidget(self._btn_one)
        elif btn_cnt == 2:
            self._btn_layout.addWidget(self._btn_two)
        else:
            pass

        self._label_layout = QHBoxLayout()
        self._label_layout.setContentsMargins(5, 5, 5, 5)
        self._label_layout.setSpacing(15)
        # self._label_layout.addStretch()
        self._label_layout.addWidget(self._icon_label)
        self._label_layout.addWidget(self._content_label)
        self._label_layout.addStretch()

        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(5, 5, 5, 5)
        self._main_layout.setSpacing(10)
        self._main_layout.addLayout(self._label_layout)
        self._main_layout.addLayout(self._btn_layout)
        self.setLayout(self._main_layout)

        self.setWindowTitle("提示")
        self.setWindowIcon(QIcon(PathHelper.get_img_path("logo@48x48.png")))
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setFixedSize(280, 140)

    def answer_btn_one_clicked(self):
        """

        :return:
        """
        # self.close()
        # return True
        self.accept()

    def answer_btn_two_clicked(self):
        """

        :return:
        """
        # self.close()
        # return False
        self.reject()


class CommonBtn(QPushButton):
    """

    """
    def __init__(self, img, clicked_img):
        super(CommonBtn, self).__init__()
        self.setAutoFillBackground(True)
        img = PathHelper.get_img_path(img)
        clicked_img = PathHelper.get_img_path(clicked_img)
        self.setCheckable(True)
        self.setStyleSheet(
            "QPushButton{border-radius:5px;min-width:24px; min-height:24px; max-width:24px; max-height:24px; "
            "border-image:url(\"%s\"); }"
            "QPushButton:checked{border-image:url(\"%s\"); }"
            "QPushButton::menu-indicator{image: None; }" % (img, clicked_img))



