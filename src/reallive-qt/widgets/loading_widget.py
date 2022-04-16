# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 加载/缓冲页面

@Attention :
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QLabel
from PyQt5.QtGui import QMovie

from utils.path_helper import PathHelper


class LoadingWidget(QDialog):

    def __init__(self):
        super(LoadingWidget, self).__init__()
        self.label = QLabel(self)
        self.label.setFixedSize(100, 100)
        self.label.setScaledContents(True)
        self.movie = QMovie(PathHelper.get_img_path("loading.gif"))
        self.label.setMovie(self.movie)
        self.movie.start()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    _widget = LoadingWidget()
    _widget.show()
    sys.exit(app.exec_())
