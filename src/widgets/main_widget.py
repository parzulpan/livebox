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
    QToolBar, QActionGroup, QFontDialog, QSlider, QLabel, QFileDialog
from PyQt5.QtGui import QKeySequence, QIcon, QDesktopServices, QFont
from PyQt5.QtCore import Qt, QSize, QUrl

from utils.common import get_window_center_point, ControlBtn, PromptBox
from utils.crud_cfg import *
from utils.path_helper import PathHelper
from widgets.radio_station_widget import RadioStationWidget
from widgets.search_widget import SearchWidget
from widgets.tv_widget import TvWidget
from widgets.live_widget import LiveWidget
from widgets.about_widget import AboutWidget


class MainWindow(QMainWindow):
    """

    """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.menu_bar = QMenuBar()

        self.file_menu = QMenu("文件(&F)", self.menu_bar)
        self.local_action = QAction("本地文件(L)", self.file_menu)
        self.local_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_L))
        self.local_action.triggered.connect(self.show_local_widget)
        self.live_search_action = QAction("直播搜索(F)", self.file_menu)
        self.live_search_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_F))
        self.live_search_action.triggered.connect(self.show_search_widget)
        self.tv_live_search_action = QAction("高清电视(F)", self.file_menu)
        self.tv_live_search_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_F))
        self.tv_live_search_action.triggered.connect(self.show_tv_widget)
        self.radio_station_search_action = QAction("广播电台(F)", self.file_menu)
        self.radio_station_search_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_F))
        self.radio_station_search_action.triggered.connect(self.show_radio_station_widget)
        self.close_action = QAction("关闭(C)", self.file_menu)
        self.close_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_C))
        self.close_action.triggered.connect(self.answer_close_action_triggered)
        self.quit_action = QAction("退出(Q)", self.file_menu)
        self.quit_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_Q))
        self.quit_action.triggered.connect(lambda: sys.exit())

        self.play_menu = QMenu("播放(&L)", self.menu_bar)
        self.play_pause_action = QAction("播放/暂停(P)", self.play_menu)
        self.stop_action = QAction("停止(S)", self.play_menu)
        self.resume_action = QAction("恢复(R)", self.play_menu)
        self.rate_action = QAction("倍速(R)", self.play_menu)
        self.jump_action = QAction("跳转(J)", self.play_menu)
        self.mute_action = QAction("静音(M)", self.play_menu)
        self.volume_up_action = QAction("增大音量(U)", self.play_menu)
        self.volume_down_action = QAction("减小音量(D)", self.play_menu)

        self.enhance_menu = QMenu("增强(&E)", self.menu_bar)
        self.skin_menu = QMenu("换肤", self.enhance_menu)
        self.dark_skin_action = QAction("暗黑模式", self.skin_menu)
        self.dark_skin_action.setCheckable(True)
        self.dark_skin_action.triggered.connect(self.answer_dark_skin_action_triggered)
        self.white_skin_action = QAction("纯白模式", self.skin_menu)
        self.white_skin_action.setCheckable(True)
        self.white_skin_action.triggered.connect(self.answer_white_skin_action_triggered)
        self.blue_skin_action = QAction("浅蓝模式", self.skin_menu)
        self.blue_skin_action.setCheckable(True)
        self.blue_skin_action.triggered.connect(self.answer_blue_skin_action_triggered)
        self.skin_action_group = QActionGroup(self)
        self.skin_action_group.addAction(self.dark_skin_action)
        self.skin_action_group.addAction(self.white_skin_action)
        self.skin_action_group.addAction(self.blue_skin_action)

        self.language_menu = QMenu("语言", self.enhance_menu)
        self.zh_CN_action = QAction("简体中文", self.language_menu)
        self.zh_CN_action.setCheckable(True)
        self.zh_CN_action.triggered.connect(self.answer_zh_CN_action_triggered)
        self.en_action = QAction("English", self.language_menu)
        self.en_action.setCheckable(True)
        self.en_action.triggered.connect(self.answer_en_action_triggered)
        self.language_action_group = QActionGroup(self)
        self.language_action_group.addAction(self.zh_CN_action)
        self.language_action_group.addAction(self.en_action)

        self.font_action = QAction("字体(F)", self.enhance_menu)
        self.font_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_S))
        self.font_action.triggered.connect(self.answer_font_action_triggered)
        self.hide_action = QAction("隐藏工具栏(V)", self.enhance_menu)
        self.hide_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_V))
        self.hide_action.setCheckable(True)
        self.hide_action.triggered.connect(self.answer_hide_action_triggered)

        self.tool_menu = QMenu("工具(&T)", self.menu_bar)
        self.screenshot_action = QAction("截图(J)", self.tool_menu)
        self.screenshot_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_J))
        self.screenshot_action.triggered.connect(self.answer_screenshot_action_triggered)
        self.gif_action = QAction("动图(G)", self.tool_menu)
        self.gif_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_G))
        self.gif_action.triggered.connect(self.answer_gif_action_triggered)
        self.screen_record_action = QAction("录屏(L)", self.tool_menu)
        self.screen_record_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_L))
        self.screen_record_action.triggered.connect(self.answer_screen_record_action_triggered)

        self.help_menu = QMenu("帮助(&H)", self.menu_bar)
        self.help_action = QAction("帮助文档(H)", self.help_menu)
        self.help_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_H))
        self.help_action.triggered.connect(self.answer_help_action_triggered)
        self.change_log_action = QAction("更新日志(U)", self.help_menu)
        self.change_log_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_U))
        self.change_log_action.triggered.connect(self.answer_change_log_action_triggered)
        self.check_version_action = QAction("检查版本(C)", self.help_menu)
        self.check_version_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_C))
        self.check_version_action.triggered.connect(self.answer_check_version_action_triggered)
        self.about_action = QAction("关于软件(A)", self.help_menu)
        self.about_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_A))
        self.about_action.triggered.connect(self.answer_about_action_triggered)

        self.tool_bar = QToolBar()
        self.tool_bar.setFloatable(False)
        self.tool_bar.setMovable(True)
        self.tool_bar.setIconSize(QSize(35, 35))
        # self.tool_bar.setStyleSheet("QToolBar{border: 1px solid #313335; spacing:5px; }")
        self.addToolBar(Qt.TopToolBarArea, self.tool_bar)
        self.live_tool_action = QAction("", self.tool_bar)
        self.live_tool_action.setToolTip("直播搜索")
        self.live_tool_action.setIcon(QIcon(PathHelper.get_img_path("search@128x128.png")))
        self.search_widget = SearchWidget()
        self.live_tool_action.triggered.connect(self.show_search_widget)
        self.search_widget.watch_live_signal.connect(self.answer_watch_live_signal)

        self.tv_live_tool_action = QAction("", self.tool_bar)
        self.tv_live_tool_action.setToolTip("高清电视")
        self.tv_live_tool_action.setIcon(QIcon(PathHelper.get_img_path("tv@128x128.png")))
        self.tv_widget = TvWidget()
        self.tv_live_tool_action.triggered.connect(self.show_tv_widget)
        self.tv_widget.watch_live_signal.connect(self.answer_watch_live_signal)

        self.radio_station_tool_action = QAction("", self.tool_bar)
        self.radio_station_tool_action.setToolTip("广播电台")
        self.radio_station_tool_action.setIcon(QIcon(PathHelper.get_img_path("radio_station@128x128.png")))
        self.radio_station_widget = RadioStationWidget()
        self.radio_station_tool_action.triggered.connect(self.show_radio_station_widget)
        self.radio_station_widget.listen_radio_station_signal.connect(self.answer_listen_radio_station_signal)

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
        # self.preferences_tool_action.triggered.connect(self.show_search_widget)

        self.nlp_tool_action = QAction("", self.tool_bar)
        self.nlp_tool_action.setToolTip("智能字幕")
        self.nlp_tool_action.setIcon(QIcon(PathHelper.get_img_path("nlp@128x128.png")))
        # self.nlp_tool_action.triggered.connect(self.show_search_widget)

        self.note_tool_action = QAction("", self.tool_bar)
        self.note_tool_action.setToolTip("边看边记")
        self.note_tool_action.setIcon(QIcon(PathHelper.get_img_path("note@128x128.png")))
        # self.note_tool_action.triggered.connect(self.show_search_widget)

        self.play_pause_btn = ControlBtn("pause@128x128.png", "play@128x128.png")
        self.play_pause_btn.setToolTip("播放/暂停")
        self.play_pause_btn.setShortcut(Qt.Key_Space)
        self.play_pause_btn.clicked.connect(self.answer_play_pause_btn_clicked)

        self.refresh_btn = ControlBtn("refresh@128x128.png", "refresh@128x128.png")
        self.refresh_btn.setToolTip("刷新")
        self.refresh_btn.clicked.connect(self.answer_refresh_btn_clicked)

        self.rewind_btn = ControlBtn("rewind@128x128.png", "rewind@128x128.png")
        self.rewind_btn.setToolTip("后退10秒")
        self.rewind_btn.clicked.connect(self.answer_rewind_btn_clicked)

        self.stop_btn = ControlBtn("stop@128x128.png", "stop@128x128.png")
        self.stop_btn.setToolTip("停止")
        self.stop_btn.clicked.connect(self.answer_stop_btn_clicked)

        self.fast_forward_btn = ControlBtn("fast_forward@128x128.png", "fast_forward@128x128.png")
        self.fast_forward_btn.setToolTip("前进10秒")
        self.fast_forward_btn.clicked.connect(self.answer_fast_forward_btn_clicked)

        self.fullscreen_narrow_btn = ControlBtn("fullscreen@128x128.png", "narrow@128x128.png")
        self.fullscreen_narrow_btn.setToolTip("最大化/最小化")
        self.fullscreen_narrow_btn.setShortcut(Qt.Key_Escape)
        self.fullscreen_narrow_btn.clicked.connect(self.answer_fullscreen_narrow_btn_clicked)

        self.volume_btn = ControlBtn("volume@128x128.png", "mute@128x128.png")
        self.volume_btn.setToolTip("音量")
        self.volume_btn.clicked.connect(self.answer_volume_btn_clicked)

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setFixedWidth(150)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setSingleStep(1)
        self.volume_slider.setTickInterval(1)
        self.volume_slider.setTickPosition(QSlider.TicksAbove)
        self.volume_slider.valueChanged.connect(self.answer_volume_slider_value_changed)

        self.current_volume = None
        self.current_slider_value = None
        self.volume_slider_value_label = QLabel("")
        self.current_url = None

        self.live_widget = LiveWidget()

        self._init_ui()
        self._init_cfg()

    def _init_ui(self):
        """

        :return:
        """
        # 菜单栏
        self.file_menu.addAction(self.local_action)
        self.file_menu.addAction(self.live_search_action)
        self.file_menu.addAction(self.tv_live_search_action)
        self.file_menu.addAction(self.radio_station_search_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.close_action)
        self.file_menu.addAction(self.quit_action)

        self.play_menu.addAction(self.play_pause_action)
        self.play_menu.addAction(self.stop_action)
        self.play_menu.addAction(self.resume_action)
        self.play_menu.addSeparator()
        self.play_menu.addAction(self.rate_action)
        self.play_menu.addAction(self.jump_action)
        self.play_menu.addSeparator()
        self.play_menu.addAction(self.mute_action)
        self.play_menu.addAction(self.volume_up_action)
        self.play_menu.addAction(self.volume_down_action)

        self.enhance_menu.addMenu(self.skin_menu)
        self.skin_menu.addAction(self.dark_skin_action)
        self.skin_menu.addAction(self.white_skin_action)
        self.skin_menu.addAction(self.blue_skin_action)
        self.enhance_menu.addMenu(self.language_menu)
        self.language_menu.addAction(self.zh_CN_action)
        self.language_menu.addAction(self.en_action)
        self.enhance_menu.addAction(self.font_action)
        self.enhance_menu.addSeparator()
        self.enhance_menu.addAction(self.hide_action)

        self.tool_menu.addAction(self.screenshot_action)
        self.tool_menu.addAction(self.gif_action)
        self.tool_menu.addAction(self.screen_record_action)
        self.tool_menu.addSeparator()

        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.change_log_action)
        self.help_menu.addAction(self.check_version_action)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.about_action)

        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.play_menu)
        self.menu_bar.addMenu(self.enhance_menu)
        self.menu_bar.addMenu(self.tool_menu)
        self.menu_bar.addMenu(self.help_menu)

        self.setMenuBar(self.menu_bar)

        # 工具栏
        self.tool_bar.addAction(self.live_tool_action)
        self.tool_bar.addAction(self.tv_live_tool_action)
        self.tool_bar.addAction(self.radio_station_tool_action)
        self.tool_bar.addAction(self.hot_live_tool_action)
        self.tool_bar.addAction(self.attention_tool_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.nlp_tool_action)
        self.tool_bar.addAction(self.note_tool_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.preferences_tool_action)
        # 工具栏播放控制
        self.tool_bar.addSeparator()
        self.tool_bar.addSeparator()
        self.tool_bar.addSeparator()
        self.tool_bar.addWidget(self.play_pause_btn)
        self.tool_bar.addWidget(self.refresh_btn)
        self.tool_bar.addWidget(self.rewind_btn)
        self.tool_bar.addWidget(self.stop_btn)
        self.tool_bar.addWidget(self.fast_forward_btn)
        self.tool_bar.addWidget(self.fullscreen_narrow_btn)
        self.tool_bar.addSeparator()
        self.tool_bar.addWidget(self.volume_btn)
        self.tool_bar.addWidget(self.volume_slider_value_label)
        self.tool_bar.addWidget(self.volume_slider)

        # 显示区域
        self.setCentralWidget(self.live_widget)

        self.set_window_info()

    def _init_cfg(self):
        """

        :return:
        """
        # 工具栏可见性
        visible = retrieve_content("preferences", "tool_bar_visible")
        if visible == "True":
            self.hide_action.setChecked(False)
            self.hide_action.triggered.emit(False)
        else:
            self.hide_action.setChecked(True)
            self.hide_action.triggered.emit(True)

        # 工具栏位置
        position = retrieve_content("preferences", "tool_bar_position")

        # 皮肤设置
        skin = retrieve_content("preferences", "skin")
        if skin == "dark":
            self.dark_skin_action.setChecked(True)
            self.dark_skin_action.triggered.emit()
        elif skin == "white":
            self.white_skin_action.setChecked(True)
            self.white_skin_action.triggered.emit()
        else:
            self.blue_skin_action.setChecked(True)
            self.blue_skin_action.triggered.emit()

        # 语言设置
        language = retrieve_content("preferences", "language")
        if language == "zh_CN":
            self.zh_CN_action.setChecked(True)
            self.zh_CN_action.triggered.emit()
        elif language == "en":
            self.en_action.setChecked(True)
            self.en_action.triggered.emit()
        else:
            pass

        # 字体设置
        font_family = retrieve_content("preferences", "font-family")
        font_style = retrieve_content("preferences", "font-style")
        font_size = retrieve_content("preferences", "font-size")
        font = QFont()
        font.setFamily(font_family)
        font.setStyleName(font_style)
        font.setPointSize(int(font_size))
        qApp.setFont(font)
        qApp.processEvents()

    def set_window_info(self):
        """

        :return:
        """
        desktop_widget = QDesktopWidget()
        screen_rect = desktop_widget.screenGeometry()
        self.setGeometry(screen_rect)
        title = retrieve_content("software_info", "software_name") + " " + retrieve_content("software_info",
                                                                                            "software_version")
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
                self.answer_watch_live_signal(file_name)
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
    def answer_help_action_triggered():
        """

        :return:
        """
        desktop_services = QDesktopServices()
        desktop_services.openUrl(QUrl("https://github.com/parzulpan/real-live/blob/master/resources/Help.md"))

    @staticmethod
    def answer_change_log_action_triggered():
        """

        :return:
        """
        desktop_services = QDesktopServices()
        desktop_services.openUrl(QUrl("https://github.com/parzulpan/real-live/blob/master/resources/ChangeLog.md"))

    @staticmethod
    def answer_check_version_action_triggered():
        """

        :return:
        """
        # TODO: 获取GitHub API 进行检查并弹窗
        desktop_services = QDesktopServices()
        desktop_services.openUrl(QUrl("https://github.com/parzulpan/real-live/releases"))

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
        self.live_widget.vlc_widget.play_url(url)
        self.live_widget.set_player_widget(True)

    def answer_listen_radio_station_signal(self, url):
        """

        :param url:
        :return:
        """
        self.live_widget.vlc_widget.play_url(url)
        self.live_widget.set_player_widget(True)

    def answer_close_action_triggered(self):
        """

        :return:
        """
        self.live_widget.set_player_widget(False)
        self.live_widget.vlc_widget.stop()

    def answer_hide_action_triggered(self, checked):
        """

        :param checked:
        :return:
        """
        if checked:
            self.tool_bar.hide()
            update_contents("preferences", "tool_bar_visible", "False")
            # self.live_widget.vlc_widget.control_widget.hide()
        else:
            self.tool_bar.show()
            update_contents("preferences", "tool_bar_visible", "True")
            # self.live_widget.vlc_widget.control_widget.show()

    def answer_tool_bar_top_level_changed(self, area):
        """

        :return:
        """
        print("top_level_changed")
        print(area)
        if self.tool_bar.allowedAreas() == Qt.LeftToolBarArea:
            print("LeftToolBarArea")
        elif self.tool_bar.allowedAreas() == Qt.RightToolBarArea:
            print("RightToolBarArea")
        elif self.tool_bar.allowedAreas() == Qt.BottomToolBarArea:
            print("BottomToolBarArea")
        elif self.tool_bar.allowedAreas() == Qt.TopToolBarArea:
            print("TopToolBarArea")
        else:
            print("else")

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

    @staticmethod
    def answer_dark_skin_action_triggered(checked):
        """

        :param checked:
        :return:
        """
        with open(PathHelper.get_qss_path("dark.qss"), "r", encoding="utf-8") as f:
            qss = f.read()
            qApp.setStyleSheet(qss)
        update_contents("preferences", "skin", "dark")

    @staticmethod
    def answer_white_skin_action_triggered(checked):
        """

        :param checked:
        :return:
        """
        with open(PathHelper.get_qss_path("white.qss"), "r", encoding="utf-8") as f:
            qss = f.read()
            qApp.setStyleSheet(qss)
        update_contents("preferences", "skin", "white")

    @staticmethod
    def answer_blue_skin_action_triggered(checked):
        """

        :param checked:
        :return:
        """
        with open(PathHelper.get_qss_path("blue.qss"), "r", encoding="utf-8") as f:
            qss = f.read()
            qApp.setStyleSheet(qss)
        update_contents("preferences", "skin", "blue")

    def answer_font_action_triggered(self, checked):
        """

        :param checked:
        :return:
        """
        font = qApp.font()
        font, changed = QFontDialog().getFont(font, self, caption="字体设置")
        if changed:
            qApp.setFont(font)
            qApp.processEvents()
            update_contents("preferences", "font-family", font.family())
            update_contents("preferences", "font-style", font.styleName())
            update_contents("preferences", "font-size", str(font.pointSize()))

    def answer_zh_CN_action_triggered(self, checked):
        """

        :param checked:
        :return:
        """
        update_contents("preferences", "language", "zh_CN")
        pass

    def answer_en_action_triggered(self, checked):
        """

        :param checked:
        :return:
        """
        update_contents("preferences", "language", "en")
        pass

    def closeEvent(self, event) -> None:
        """

        :param event:
        :return:
        """
        pass

    def answer_play_pause_btn_clicked(self):
        """

        :return:
        """
        if self.play_pause_btn.isChecked():
            self.pause()
        else:
            self.resume()

    def answer_refresh_btn_clicked(self):
        """

        :return:
        """
        self.play_url(self.current_url)

    def answer_rewind_btn_clicked(self):
        """

        :return:
        """
        pass

    def answer_stop_btn_clicked(self):
        """

        :return:
        """
        self.stop()

    def answer_fast_forward_btn_clicked(self):
        """

        :return:
        """
        pass

    def answer_fullscreen_narrow_btn_clicked(self):
        """

        :return:
        """
        pass

    def answer_volume_btn_clicked(self):
        """

        :return:
        """
        if self.volume_btn.isChecked():
            self.current_volume = self.get_volume()
            self.current_slider_value = self.volume_slider.value()
            self.set_volume(0)
            self.volume_slider.setValue(0)
        else:
            self.set_volume(self.current_volume)
            self.volume_slider.setValue(self.current_slider_value)

    def answer_volume_slider_value_changed(self):
        """

        :return:
        """
        # volume_value = self.volume_slider.value()
        # if 0 == volume_value:
        #     self.volume_btn.setChecked(True)
        # else:
        #     self.volume_btn.setChecked(False)
        # self.volume_slider_value_label.setText("{0}%".format(volume_value))
        # self.set_volume(volume_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
