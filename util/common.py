# -*- coding: utf-8 -*-
"""
@Time      : 2020/6/16

@Author    : parzulpan

@Summary   : 通用功能

@Attention : 
"""
from PyQt5.QtWidgets import QDesktopWidget, QDialog


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
    def __init__(self):
        super(PromptBox, self).__init__()
        pass

    def _init_ui(self):
        """

        :return:
        """
        pass
