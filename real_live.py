# -*- coding: utf-8 -*-
# @Date       : 6/15/2020
# @Author     : parzulpan
# @Email      : parzulpan@gmail.com
# @Description: 请输入此文件的功能描述
# @Attention  :

import sys

from PyQt5.QtWidgets import QApplication

from widgets.main_widget import MainWindow


def run():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
