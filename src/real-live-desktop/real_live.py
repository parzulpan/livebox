# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 软件启动入口，使用单例模式

@Attention :
"""

import sys

from PyQt5.QtWidgets import QApplication

from widgets.main_widget import MainWindow
from utils.singleton import SingletonFunctionVersion
from utils.states import run_state_mgr


@SingletonFunctionVersion
def run():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    run_state_mgr(main_window)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
