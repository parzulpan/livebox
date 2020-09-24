# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 软件主页面，使用单例模式

@Attention :
"""

import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QMenuBar, QMenu, QAction, QDesktopWidget, qApp, \
    QToolBar, QActionGroup, QFontDialog, QSlider, QLabel, QFileDialog, QWidget
from PyQt5.QtGui import QKeySequence, QIcon, QDesktopServices, QFont
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from utils import states
from utils.common import *
from utils.path_helper import PathHelper
from utils.enums import PlayerEnum
from utils.states import PlayerState
from widgets.radio_station_widget import RadioStationWidget
from widgets.search_widget import SearchWidget
from widgets.tv_widget import TvWidget
from widgets.about_widget import AboutWidget
from widgets.preferences_widget import PreferencesWidget
from widgets.vlc_player_widget import VlcPlayerWidget


class MainWindow(QMainWindow):
    """

    """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.menu_bar = QMenuBar()

        self.media_menu = QMenu("媒体(M)", self.menu_bar)
        self.local_action = QAction("本地文件(L)", self.media_menu)
        self.local_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_L))
        self.local_action.triggered.connect(self.show_local_widget)
        self.live_search_action = QAction("直播搜索(F)", self.media_menu)
        self.live_search_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_F))
        self.live_search_action.triggered.connect(self.show_search_widget)
        self.tv_live_search_action = QAction("高清电视(T)", self.media_menu)
        self.tv_live_search_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_T))
        self.tv_live_search_action.triggered.connect(self.show_tv_widget)
        self.radio_station_search_action = QAction("广播电台(R)", self.media_menu)
        self.radio_station_search_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_R))
        self.radio_station_search_action.triggered.connect(self.show_radio_station_widget)
        self.close_action = QAction("关闭(C)", self.media_menu)
        self.close_action.setShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_C))
        self.close_action.triggered.connect(self.answer_close_action_triggered)
        self.quit_action = QAction("退出(Q)", self.media_menu)
        self.quit_action.setShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_Q))
        self.quit_action.triggered.connect(lambda: sys.exit())

        self.enhance_menu = QMenu("增强(E)", self.menu_bar)
        self.screenshot_action = QAction("截图(J)", self.enhance_menu)
        self.screenshot_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_J))
        self.screenshot_action.triggered.connect(self.answer_screenshot_action_triggered)
        self.gif_action = QAction("动图(G)", self.enhance_menu)
        self.gif_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_G))
        self.gif_action.triggered.connect(self.answer_gif_action_triggered)
        self.screen_record_action = QAction("录屏(L)", self.enhance_menu)
        self.screen_record_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_L))
        self.screen_record_action.triggered.connect(self.answer_screen_record_action_triggered)
        self.preferences_action = QAction("偏好设置(P)", self.enhance_menu)
        self.preferences_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_P))
        self.preferences_action.triggered.connect(self.show_preferences_widget)

        self.my_menu = QMenu("我的(P)", self.menu_bar)
        self.connect_github_action = QAction("连接到GitHub", self.my_menu)
        self.backup_data_action = QAction("备份数据", self.my_menu)
        self.restore_from_backup_action = QAction("从备份中恢复", self.my_menu)

        self.help_menu = QMenu("帮助(H)", self.menu_bar)
        self.help_action = QAction("帮助文档(H)", self.help_menu)
        self.help_action.setShortcut(QKeySequence(Qt.CTRL + Qt.ALT + Qt.Key_H))
        self.help_action.triggered.connect(self.answer_help_action_triggered)
        self.change_log_action = QAction("更新日志(U)", self.help_menu)
        self.change_log_action.setShortcut(QKeySequence(Qt.CTRL + Qt.ALT + Qt.Key_U))
        self.change_log_action.triggered.connect(self.answer_change_log_action_triggered)
        self.check_version_action = QAction("检查版本(C)", self.help_menu)
        self.check_version_action.setShortcut(QKeySequence(Qt.CTRL + Qt.ALT + Qt.Key_C))
        self.check_version_action.triggered.connect(self.answer_check_version_action_triggered)
        self.about_action = QAction("关于软件(A)", self.help_menu)
        self.about_action.setShortcut(QKeySequence(Qt.CTRL + Qt.ALT + Qt.Key_A))
        self.about_action.triggered.connect(self.answer_about_action_triggered)

        self.tool_bar = QToolBar()
        self.tool_bar.setFloatable(False)
        self.tool_bar.setMovable(True)
        self.tool_bar.setIconSize(QSize(35, 35))
        # self.tool_bar.setStyleSheet("QToolBar{border: 1px solid #313335; spacing:5px; }")
        self.live_tool_action = QAction("", self.tool_bar)
        self.live_tool_action.setToolTip("直播搜索")
        self.live_tool_action.setIcon(QIcon(PathHelper.get_img_path("search@128x128.png")))
        self.search_widget = SearchWidget()
        self.live_tool_action.triggered.connect(self.show_search_widget)
        self.search_widget.watch_live_signal.connect(self.answer_play_action_triggered)

        self.tv_live_tool_action = QAction("", self.tool_bar)
        self.tv_live_tool_action.setToolTip("高清电视")
        self.tv_live_tool_action.setIcon(QIcon(PathHelper.get_img_path("tv@128x128.png")))
        self.tv_widget = TvWidget()
        self.tv_live_tool_action.triggered.connect(self.show_tv_widget)
        self.tv_widget.watch_tv_signal.connect(self.answer_play_action_triggered)

        self.radio_station_tool_action = QAction("", self.tool_bar)
        self.radio_station_tool_action.setToolTip("广播电台")
        self.radio_station_tool_action.setIcon(QIcon(PathHelper.get_img_path("radio_station@128x128.png")))
        self.radio_station_widget = RadioStationWidget()
        self.radio_station_tool_action.triggered.connect(self.show_radio_station_widget)
        self.radio_station_widget.listen_radio_station_signal.connect(self.answer_play_action_triggered)

        self.hot_live_tool_action = QAction("", self.tool_bar)
        self.hot_live_tool_action.setToolTip("热门直播")
        self.hot_live_tool_action.setIcon(QIcon(PathHelper.get_img_path("hot@128x128.png")))

        self.attention_tool_action = QAction("", self.tool_bar)
        self.attention_tool_action.setToolTip("我的关注")
        self.attention_tool_action.setIcon(QIcon(PathHelper.get_img_path("attention@128x128.png")))
        # self.attention_tool_action.triggered.connect(self.show_search_widget)

        self.preferences_tool_action = QAction("", self.tool_bar)
        self.preferences_tool_action.setToolTip("偏好设置")
        self.preferences_tool_action.setIcon(QIcon(PathHelper.get_img_path("preferences@128x128.png")))
        self.preferences_tool_action.triggered.connect(self.show_preferences_widget)

        self.nlp_tool_action = QAction("", self.tool_bar)
        self.nlp_tool_action.setToolTip("智能字幕")
        self.nlp_tool_action.setIcon(QIcon(PathHelper.get_img_path("nlp@128x128.png")))
        # self.nlp_tool_action.triggered.connect(self.show_search_widget)

        self.note_tool_action = QAction("", self.tool_bar)
        self.note_tool_action.setToolTip("边看边记")
        self.note_tool_action.setIcon(QIcon(PathHelper.get_img_path("note@128x128.png")))
        # self.note_tool_action.triggered.connect(self.show_search_widget)

        self.vlc_widget = VlcPlayerWidget()

        self._init_ui()
        self.init_cfg()

    def _init_ui(self):
        """

        :return:
        """
        # 菜单栏
        self.media_menu.addAction(self.local_action)
        self.media_menu.addAction(self.live_search_action)
        self.media_menu.addAction(self.tv_live_search_action)
        self.media_menu.addAction(self.radio_station_search_action)
        self.media_menu.addSeparator()
        self.media_menu.addAction(self.close_action)
        self.media_menu.addAction(self.quit_action)

        self.enhance_menu.addAction(self.screenshot_action)
        self.enhance_menu.addAction(self.gif_action)
        self.enhance_menu.addAction(self.screen_record_action)
        self.enhance_menu.addSeparator()
        self.enhance_menu.addAction(self.preferences_action)

        self.my_menu.addAction(self.connect_github_action)
        self.my_menu.addSeparator()
        self.my_menu.addAction(self.backup_data_action)
        self.my_menu.addAction(self.restore_from_backup_action)

        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.change_log_action)
        self.help_menu.addAction(self.check_version_action)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.about_action)

        self.menu_bar.addMenu(self.media_menu)
        self.menu_bar.addMenu(self.enhance_menu)
        self.menu_bar.addMenu(self.my_menu)
        self.menu_bar.addMenu(self.help_menu)

        self.setMenuBar(self.menu_bar)

        # 工具栏
        self.tool_bar.addAction(self.live_tool_action)
        self.tool_bar.addAction(self.tv_live_tool_action)
        self.tool_bar.addAction(self.radio_station_tool_action)
        self.tool_bar.addAction(self.hot_live_tool_action)
        self.tool_bar.addAction(self.attention_tool_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.nlp_tool_action)
        self.tool_bar.addAction(self.note_tool_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.preferences_tool_action)

        # 显示区域
        self.setCentralWidget(self.vlc_widget)

        self.set_window_info()

    def init_cfg(self):
        """

        :return:
        """

        # 工具栏设置
        visible = get_tool_bar_visible()
        if visible:
            self.tool_bar.show()
        else:
            self.tool_bar.hide()
        pos = get_tool_bar_pos()
        if pos == CommonEnum.ToolBarPosTop:
            self.addToolBar(Qt.TopToolBarArea, self.tool_bar)
        elif pos == CommonEnum.ToolBarPosRight:
            self.addToolBar(Qt.RightToolBarArea, self.tool_bar)
        elif pos == CommonEnum.ToolBarPosBottom:
            self.addToolBar(Qt.BottomToolBarArea, self.tool_bar)
        elif pos == CommonEnum.ToolBarPosLeft:
            self.addToolBar(Qt.LeftToolBarArea, self.tool_bar)
        else:
            self.addToolBar(Qt.TopToolBarArea, self.tool_bar)

        # 皮肤设置
        skin = get_skin()
        set_skin(skin)

        # 语言设置
        language = get_language()
        set_language(language)

        # 字体设置
        font_dict = get_font()
        font = QFont()
        font.setFamily(font_dict["font_family"])
        font.setStyleName(font_dict["font_style"])
        font.setPointSize(font_dict["font_size"])
        qApp.setFont(font)
        qApp.processEvents()

    def set_window_info(self):
        """

        :return:
        """
        desktop_widget = QDesktopWidget()
        screen_rect = desktop_widget.screenGeometry()
        self.setGeometry(screen_rect)
        _app_info = get_app_info()
        title = _app_info["name"] + " " + _app_info["version"]
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(PathHelper.get_img_path("logo@48x48.png")))
        self.showMaximized()

    def show_local_widget(self):
        """

        :return:
        """
        file_name, file_type = QFileDialog.getOpenFileName(self, "选择音视频文件", ".", "All Files (*)")
        if file_name:
            _type = os.path.splitext(file_name)[-1][1:]
            _type_list = ["3g2", "3gp", "3gp2", "3gpp", "amv", "asf", "avi", "bik", "bin", "divx", "drc", "dv", "f4v",
                          "flv", "gvi", "gxf", "iso", "m1v", "m2v", "m2t", "m2ts", "m4v", "mkv", "mov", "mp2", "mp4",
                          "mp4v", "mpe", "mpeg", "mpeg1", "mpeg2", "mpeg4", "mpg", "mpv2", "mts", "mxf", "mxg", "nsv",
                          "nuv", "ogg", "ogm", "ogv", "ps", "rec", "rm", "rmvb", "rpl", "thp", "tod", "ts", "tts",
                          "txd", "vob", "vro", "webm", "wm", "wmv", "wtv", "xesc",
                          "3ga", "669", "a52", "acc", "ac3", "adt", "adts", "aif", "aiff", "amr", "aob", "ape", "awb",
                          "caf", "dts", "flac", "it",
                          "kar", "m4a", "m4b", "m4p", "m5p", "mid", "mka", "mlp", "mod", "mpa", "mp1", "mp2", "mp3",
                          "mpc", "mpga", "mus", "oga",
                          "ogg", "oma", "opus", "qcp", "ra", "rmi", "s3m", "sid", "spx", "thd", "tta", "voc", "vqf",
                          "w64", "wav", "wma", "wv", "xa", "xm"]
            if _type in _type_list:
                self.answer_play_action_triggered(file_name, PlayerEnum.MrlTypeLocal.value[1])
            else:
                _box = PromptBox(2, "音视频文件错误!", 1)
                width, height = get_window_center_point(_box)
                _box.move(width, height)
                _box.exec_()

    def show_search_widget(self):
        """

        :return:
        """
        width, height = get_window_center_point(self.search_widget)
        self.search_widget.move(width, height)
        self.search_widget.exec_()

    def show_tv_widget(self):
        """

        :return:
        """
        width, height = get_window_center_point(self.tv_widget)
        self.tv_widget.move(width, height)
        self.tv_widget.exec_()

    def show_radio_station_widget(self):
        """

        :return:
        """
        width, height = get_window_center_point(self.radio_station_widget)
        self.radio_station_widget.move(width, height)
        self.radio_station_widget.exec_()

    @staticmethod
    def show_preferences_widget():
        """

        :return:
        """
        preferences_widget = PreferencesWidget()
        width, height = get_window_center_point(preferences_widget)
        preferences_widget.move(width, height)
        preferences_widget.exec_()

    @staticmethod
    def answer_help_action_triggered():
        """

        :return:
        """
        desktop_services = QDesktopServices()
        _app_info = get_app_info()
        desktop_services.openUrl(QUrl(_app_info["help_url"]))

    @staticmethod
    def answer_change_log_action_triggered():
        """

        :return:
        """
        desktop_services = QDesktopServices()
        _app_info = get_app_info()
        desktop_services.openUrl(QUrl(_app_info["change_log_url"]))

    @staticmethod
    def answer_check_version_action_triggered():
        """

        :return:
        """
        # TODO: 获取 GitHub API 进行检查并弹窗
        desktop_services = QDesktopServices()
        _app_info = get_app_info()
        desktop_services.openUrl(QUrl(_app_info["update"]))

    @staticmethod
    def answer_about_action_triggered():
        """

        :return:
        """
        about_widget = AboutWidget()
        width, height = get_window_center_point(about_widget)
        about_widget.move(width, height)
        about_widget.exec_()

    def answer_play_action_triggered(self, url: str, url_type: PlayerEnum):
        """

        :param url:
        :param url_type:
        :return:
        """
        # if url_type == PlayerEnum.MrlTypeRS.value[1]:
        #     self.vlc_widget = VlcPlayerWidget("--audio-visual=visual", "--effect-list=spectrometer",
        #                                       "--effect-fft-window=flattop")
        # else:
        #     self.vlc_widget = VlcPlayerWidget()
        # loading_widget = LoadingWidget()
        # width, height = get_window_center_point(loading_widget)
        # loading_widget.move(width, height)
        # loading_widget.show()
        self.vlc_widget.vlc_play(url, url_type)
        # while PlayerState.Load == PlayerEnum.LoadPlaying:
        #     loading_widget.close()

    def answer_close_action_triggered(self):
        """

        :return:
        """
        self.vlc_widget.vlc_stop()

    @staticmethod
    def answer_screenshot_action_triggered():
        """

        :return:
        """
        pass

    def answer_gif_action_triggered(self):
        """

        :return:
        """
        pass

    def answer_screen_record_action_triggered(self):
        """

        :return:
        """
        pass

    def closeEvent(self, event) -> None:
        """

        :param event:
        :return:
        """
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
