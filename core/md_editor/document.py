# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""
from PyQt5.QtCore import QObject, pyqtSignal


class Document(QObject):

    text_changed = pyqtSignal(str)

    def __init__(self):
        super(Document, self).__init__()
        self.m_text = None

    def set_text(self, text: str) -> None:
        """

        :param text:
        :return:
        """
        if text == self.m_text:
            return
        self.m_text = text
        self.text_changed.emit(self.m_text)
