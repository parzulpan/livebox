# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 软件启动，使用单例模式

@Attention :
"""

import sys

from PyQt5.QtWidgets import QApplication

from widgets.main_widget import MainWindow
from utils.singleton import SingletonFunctionVersion


@SingletonFunctionVersion
def run():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
