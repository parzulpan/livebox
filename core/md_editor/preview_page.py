# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWebEngineWidgets import QWebEnginePage


class PreviewPage(QWebEnginePage):
    """

    """
    def __init__(self):
        super(PreviewPage, self).__init__()
        pass

    def accept_navigation_request(self, url: QUrl, style, is_frame: bool) -> bool:
        """

        :param url:
        :param style:
        :param is_frame:
        :return:
        """
        if url.scheme() == str("qrc"):
            return True
        desktop_services = QDesktopServices()
        desktop_services.openUrl(url)
        return False
