# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 软件启动入口，使用单例模式

@Attention :
"""

import sys

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication
from pyqt5_material import apply_stylesheet

from utils.common import get_theme
from widgets.main_widget import MainWindow
from utils.singleton import SingletonFunctionVersion
from utils.states import run_state_mgr


@SingletonFunctionVersion
def run():
    app = QApplication(sys.argv)
    trans = QTranslator()
    trans.load('eng-chs')
    app.installTranslator(trans)
    theme = get_theme()
    if theme != "original":
        apply_stylesheet(app, theme=f"{theme}.xml")
    main_window = MainWindow()
    main_window.show()
    run_state_mgr(main_window)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
