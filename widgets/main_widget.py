# -*- coding: utf-8 -*-
# @Date       : 6/15/2020 
# @Author     : parzulpan
# @Email      : parzulpan@gmail.com
# @Description: 请输入此文件的功能描述
# @Attention  :

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMenuBar, QMenu, QAction, QDesktopWidget, QVBoxLayout
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtCore import Qt

from util.common import get_window_center_point
from widgets.search_widget import SearchWidget
from widgets.live_widget import LiveWidget


class MainWindow(QMainWindow):
    """

    """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.menu_bar = QMenuBar()

        self.file_menu = QMenu("文件(&F)", self.menu_bar)
        self.open_action = QAction("打开(O)", self.file_menu)
        self.open_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_O))
        self.search_action = QAction("搜索(F)", self.file_menu)
        self.search_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_F))
        self.close_action = QAction("关闭(C)", self.file_menu)
        self.close_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_C))
        self.quit_action = QAction("退出(Q)", self.file_menu)
        self.quit_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_Q))

        self.enhance_menu = QMenu("增强(&E)", self.menu_bar)
        self.skin_action = QAction("换肤(S)", self.enhance_menu)
        self.skin_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_S))
        self.hide_action = QAction("隐藏(V)", self.enhance_menu)
        self.hide_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_V))

        self.help_menu = QMenu("帮助(&H)", self.menu_bar)
        self.help_action = QAction("帮助文档(H)", self.help_menu)
        self.help_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_H))
        self.about_action = QAction("关于软件(A)", self.help_menu)
        self.about_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_A))

        self.tool_bar = self.addToolBar("tool_bar")
        self.search_tool_action = QAction("", self.tool_bar)
        self.search_tool_action.setToolTip("搜索")
        self.search_tool_action.setIcon(QIcon("./resources/img/search@128x128.png"))
        self.search_widget = SearchWidget()
        self.search_tool_action.triggered.connect(self.show_search_widget)

        self.live_widget = LiveWidget()

        self.init_ui()
        self.set_window_info()

    def init_ui(self):
        """

        :return:
        """
        # 菜单栏
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.search_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.close_action)
        self.file_menu.addAction(self.quit_action)
        self.enhance_menu.addAction(self.skin_action)
        self.enhance_menu.addAction(self.hide_action)
        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.about_action)

        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.enhance_menu)
        self.menu_bar.addMenu(self.help_menu)

        self.setMenuBar(self.menu_bar)

        # 工具栏
        self.tool_bar.addAction(self.search_tool_action)
        self.tool_bar.addSeparator()

        # 显示区域
        self.setCentralWidget(self.live_widget)

    def set_window_info(self):
        """

        :return:
        """
        desktop_widget = QDesktopWidget()
        screen_rect = desktop_widget.screenGeometry()
        print(screen_rect.width(), screen_rect.height())
        self.setGeometry(screen_rect)
        self.setWindowTitle("网络直播观看平台 V1.0.0")
        self.setWindowIcon(QIcon('./resources/img/logo@48x48.png'))
        self.showMaximized()

    def show_search_widget(self):
        """

        :return:
        """
        width, height = get_window_center_point(self.search_widget)
        self.search_widget.move(width, height)
        self.search_widget.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
