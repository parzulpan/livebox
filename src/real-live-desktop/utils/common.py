# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 通用功能

@Attention :
"""

from PyQt5.QtWidgets import QDesktopWidget, QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, qApp, QFontDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from utils.path_helper import PathHelper
from utils.crud_json import *


def get_window_center_point(widget):
    """ 使窗口居中显示

    :param widget: 需要居中显示的窗口
    :return:
    """
    desktop_widget = QDesktopWidget()
    screen_rect = desktop_widget.screenGeometry()
    return (screen_rect.width()-widget.width()) / 2, (screen_rect.height()-widget.height()) / 2


def set_skin(skin: str):
    """

    :param skin:
    :return:
    """
    with open(PathHelper.get_qss_path(f"{skin}.qss"), "r", encoding="utf-8") as f:
        qss = f.read()
        qApp.setStyleSheet(qss)
    default_json2python4file["preferences"]["personalise"]["skin"] = skin
    python2json2file(default_json2python4file)


def get_skin():
    """

    :return:
    """
    return default_json2python4file["preferences"]["personalise"]["skin"]


def set_font():
    """

    :return:
    """
    font = qApp.font()
    font, changed = QFontDialog().getFont(font, None, caption="字体设置")
    if changed:
        qApp.setFont(font)
        qApp.processEvents()
        default_json2python4file["preferences"]["personalise"]["font-family"] = font.family()
        default_json2python4file["preferences"]["personalise"]["font-style"] = font.font.styleName()
        default_json2python4file["preferences"]["personalise"]["font-size"] = font.pointSize()
        python2json2file(default_json2python4file)


def get_font():
    """

    :return:
    """
    font_family = default_json2python4file["preferences"]["personalise"]["font-family"]
    font_style = default_json2python4file["preferences"]["personalise"]["font-style"]
    font_size = default_json2python4file["preferences"]["personalise"]["font-size"]
    return {"font_family": font_family, "font_style": font_style, "font_size": font_size}


def set_language(language: str):
    """

    :param language:
    :return:
    """
    default_json2python4file["preferences"]["personalise"]["language"] = language
    python2json2file(default_json2python4file)


def get_language():
    """

    :return:
    """
    return default_json2python4file["preferences"]["personalise"]["language"]


def set_tool_bar_visible(visible: int):
    """

    :param visible:
    :return:
    """
    default_json2python4file["preferences"]["personalise"]["tool_bar_visible"] = visible
    python2json2file(default_json2python4file)


def get_tool_bar_visible():
    """

    :return:
    """

    return default_json2python4file["preferences"]["personalise"]["tool_bar_visible"]


def set_app_info(data: dict):
    """

    :param data:
    :return:
    """

    default_json2python4file["app_info"] = data
    python2json2file(default_json2python4file)


def get_app_info():
    """

    :return:
    """

    return default_json2python4file["app_info"]


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


class ControlBtn(QPushButton):
    """

    """
    def __init__(self, img, clicked_img):
        super(ControlBtn, self).__init__()
        self.setAutoFillBackground(True)
        img = PathHelper.get_img_path(img)
        clicked_img = PathHelper.get_img_path(clicked_img)
        self.setCheckable(True)
        self.setStyleSheet(
            "QPushButton{min-width:32px; min-height:32px; max-width:32px; max-height:32px; "
            "border-image:url(\"%s\"); }"
            "QPushButton:checked{border-image:url(\"%s\"); }"
            "QPushButton::menu-indicator{image: None; }" % (img, clicked_img))



