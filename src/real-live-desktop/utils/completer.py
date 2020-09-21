# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 自动补全工具

@Attention :
"""

from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt


def set_completer(content, component):
    """ 为控件添加自动补全

    :param content: 候选内容
    :param component: 控件
    :return:
    """
    # 增加自动补全
    completer = QCompleter(content)
    # 设置匹配模式，有三种： Qt.MatchStartsWith 开头匹配（默认）  Qt.MatchContains 内容匹配  Qt.MatchEndsWith 结尾匹配
    completer.setFilterMode(Qt.MatchContains)
    # 设置补全模式，有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
    completer.setCompletionMode(QCompleter.PopupCompletion)
    # 给控件设置补全器
    component.setCompleter(completer)
