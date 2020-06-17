# -*- coding: utf-8 -*-
# @Date       : 6/15/2020 
# @Author     : parzulpan
# @Email      : parzulpan@gmail.com
# @Description: 请输入此文件的功能描述
# @Attention  :

import sys
from ctypes import windll, WinDLL, cdll, CDLL

from PyQt5.QtWidgets import QMainWindow, QApplication, QMenuBar, QMenu, QAction, QDesktopWidget, QVBoxLayout
from PyQt5.QtGui import QKeySequence, QIcon, QDesktopServices
from PyQt5.QtCore import Qt, QSize, QUrl

from util.common import get_window_center_point
from widgets.search_widget import SearchWidget
from widgets.live_widget import LiveWidget
from widgets.about_widget import AboutWidget


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
        self.search_action.triggered.connect(self.show_search_widget)
        self.close_action = QAction("关闭(C)", self.file_menu)
        self.close_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_C))
        self.close_action.triggered.connect(self.answer_close_action_triggered)
        self.quit_action = QAction("退出(Q)", self.file_menu)
        self.quit_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_Q))
        self.quit_action.triggered.connect(lambda: sys.exit())

        self.enhance_menu = QMenu("增强(&E)", self.menu_bar)
        self.skin_action = QAction("换肤(S)", self.enhance_menu)
        self.skin_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_S))
        self.hide_action = QAction("隐藏(V)", self.enhance_menu)
        self.hide_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_V))
        self.hide_action.setCheckable(True)
        self.hide_action.triggered.connect(self.answer_hide_action_triggered)

        self.plugin_menu = QMenu("插件(&P)", self.menu_bar)
        self.screenshot_action = QAction("截图(J)", self.plugin_menu)
        self.screenshot_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_J))
        self.screenshot_action.triggered.connect(self.answer_screenshot_action_triggered)

        self.help_menu = QMenu("帮助(&H)", self.menu_bar)
        self.help_action = QAction("帮助文档(H)", self.help_menu)
        self.help_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_H))
        self.help_action.triggered.connect(self.answer_help_action_triggered)
        self.about_action = QAction("关于软件(A)", self.help_menu)
        self.about_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_A))
        self.about_action.triggered.connect(self.answer_about_action_triggered)

        self.tool_bar = self.addToolBar("tool_bar")
        self.tool_bar.setIconSize(QSize(32, 32))
        self.tool_bar.setStyleSheet("QToolBar{spacing:5px; }")
        self.search_tool_action = QAction("", self.tool_bar)
        self.search_tool_action.setToolTip("信息搜索")
        self.search_tool_action.setIcon(QIcon("./resources/img/search@128x128.png"))
        self.search_widget = SearchWidget()
        self.search_tool_action.triggered.connect(self.show_search_widget)
        self.search_widget.watch_live_signal.connect(self.answer_watch_live_signal)

        self.attention_tool_action = QAction("", self.tool_bar)
        self.attention_tool_action.setToolTip("历史关注")
        self.attention_tool_action.setIcon(QIcon("./resources/img/attention@128x128.png"))
        self.attention_tool_action.triggered.connect(self.show_search_widget)

        self.pure_tool_action = QAction("", self.tool_bar)
        self.pure_tool_action.setToolTip("纯净模式")
        self.pure_tool_action.setIcon(QIcon("./resources/img/pure@128x128.png"))
        self.pure_tool_action.triggered.connect(self.show_search_widget)

        self.nlp_tool_action = QAction("", self.tool_bar)
        self.nlp_tool_action.setToolTip("智能字幕")
        self.nlp_tool_action.setIcon(QIcon("./resources/img/nlp@128x128.png"))
        self.nlp_tool_action.triggered.connect(self.show_search_widget)

        self.note_tool_action = QAction("", self.tool_bar)
        self.note_tool_action.setToolTip("边看边记")
        self.note_tool_action.setIcon(QIcon("./resources/img/note@128x128.png"))
        self.note_tool_action.triggered.connect(self.show_search_widget)

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
        self.plugin_menu.addAction(self.screenshot_action)
        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.about_action)

        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.enhance_menu)
        self.menu_bar.addMenu(self.plugin_menu)
        self.menu_bar.addMenu(self.help_menu)

        self.setMenuBar(self.menu_bar)

        # 工具栏
        self.tool_bar.addAction(self.search_tool_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.attention_tool_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.pure_tool_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.nlp_tool_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.note_tool_action)
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

    @staticmethod
    def answer_help_action_triggered():
        """

        :return:
        """
        desktop_services = QDesktopServices()
        desktop_services.openUrl(QUrl("https://github.com/parzulpan/real-live"))

    @staticmethod
    def answer_about_action_triggered():
        """

        :return:
        """
        about_widget = AboutWidget()
        width, height = get_window_center_point(about_widget)
        about_widget.move(width, height)
        about_widget.exec_()

    def answer_watch_live_signal(self, url):
        """

        :param url:
        :return:
        """
        self.live_widget.set_player_widget(True)
        self.live_widget.vlc_widget.play_url(url)

    def answer_close_action_triggered(self):
        """

        :return:
        """
        self.live_widget.set_player_widget(False)
        self.live_widget.vlc_widget.release()

    def answer_hide_action_triggered(self, checked):
        """

        :param checked:
        :return:
        """
        if checked:
            self.tool_bar.hide()
        else:
            self.tool_bar.show()

    @staticmethod
    def answer_screenshot_action_triggered():
        """

        :return:
        """
        # dll = windll.LoadLibrary('./bin/OEScreenshot.dll')
        # dll = WinDLL('./bin/OEScreenshot.dll')
        # dll = cdll.LoadLibrary('./bin/OEScreenshot.dll')
        dll = CDLL('./bin/OEScreenshot.dll')
        print(dll)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
