# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 偏好设置页面

@Attention :
"""
import sys

from PyQt5.QtWidgets import QWidget, QStackedWidget, QListWidget, QListWidgetItem, QLabel, QRadioButton, QPushButton, \
    QHBoxLayout, QVBoxLayout, QFrame, QDialog, QApplication, qApp, QFontDialog, QButtonGroup
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

from utils.common import *


class PreferencesWidget(QDialog):

    def __init__(self):
        super(PreferencesWidget, self).__init__()

        # 个性化
        self.personalise_stack = QWidget()
        # 播放器
        self.player_stack = QWidget()

        self.h_line_1 = QFrame()
        self.h_line_1.setFrameShape(QFrame.HLine)
        self.h_line_1.setFrameShadow(QFrame.Sunken)
        self.h_line_2 = QFrame()
        self.h_line_2.setFrameShape(QFrame.HLine)
        self.h_line_2.setFrameShadow(QFrame.Sunken)
        self.h_line_3 = QFrame()
        self.h_line_3.setFrameShape(QFrame.HLine)
        self.h_line_3.setFrameShadow(QFrame.Sunken)
        self.h_line_4 = QFrame()
        self.h_line_4.setFrameShape(QFrame.HLine)
        self.h_line_4.setFrameShadow(QFrame.Sunken)

        self.language_label = QLabel("界面语言")
        self.language_btn_group = QButtonGroup()
        self.simplified_chinese_btn = PreferencesQRadioButton("简体中文")
        self.traditional_chinese_btn = PreferencesQRadioButton("繁体中文")
        self.english_btn = PreferencesQRadioButton("English")
        self.language_btn_group.addButton(self.simplified_chinese_btn)
        self.language_btn_group.addButton(self.traditional_chinese_btn)
        self.language_btn_group.addButton(self.english_btn)
        self.skin_label = QLabel("界面皮肤")
        self.skin_btn_group = QButtonGroup()
        self.dark_skin_btn = PreferencesQRadioButton("暗黑模式")
        self.white_skin_btn = PreferencesQRadioButton("纯白模式")
        self.blue_skin_btn = PreferencesQRadioButton("浅蓝模式")
        self.skin_btn_group.addButton(self.dark_skin_btn)
        self.skin_btn_group.addButton(self.white_skin_btn)
        self.skin_btn_group.addButton(self.blue_skin_btn)
        self.font_label = QLabel("界面字体")
        self.font_btn = QPushButton("点击设置")
        self.font_btn.clicked.connect(self.answer_font_btn_clicked)
        self.tool_bar_label = QLabel("工具栏")
        self.tool_bar_group = QButtonGroup()
        self.tool_bar_hide = PreferencesQRadioButton("默认隐藏")
        self.tool_bar_show = PreferencesQRadioButton("默认显示")
        self.tool_bar_group.addButton(self.tool_bar_hide)
        self.tool_bar_group.addButton(self.tool_bar_show)
        self.tool_bar_pos_group = QButtonGroup()
        self.tool_bar_pos_left = PreferencesQRadioButton("显示在左边")
        self.tool_bar_pos_right = PreferencesQRadioButton("显示在右边")
        self.tool_bar_pos_top = PreferencesQRadioButton("显示在上边")
        self.tool_bar_pos_bottom = PreferencesQRadioButton("显示在下边")
        self.tool_bar_pos_group.addButton(self.tool_bar_pos_left)
        self.tool_bar_pos_group.addButton(self.tool_bar_pos_right)
        self.tool_bar_pos_group.addButton(self.tool_bar_pos_top)
        self.tool_bar_pos_group.addButton(self.tool_bar_pos_bottom)
        self.personalise_stack_ui()
        self.player_stack_ui()

        self._stack = QStackedWidget()
        self._stack.addWidget(self.personalise_stack)
        self._stack.addWidget(self.player_stack)
        self._btn_left_list = QListWidget()
        _personalise_item = QListWidgetItem('个性化')
        _personalise_item.setTextAlignment(Qt.AlignCenter)
        _personalise_item.setSizeHint(QSize(100, 50))
        self._btn_left_list.insertItem(0, _personalise_item)
        _player_item = QListWidgetItem('播放器')
        _player_item.setTextAlignment(Qt.AlignCenter)
        _player_item.setSizeHint(QSize(100, 50))
        self._btn_left_list.insertItem(1, _player_item)
        self._btn_left_list.setCurrentRow(0)
        self._btn_left_list.setMinimumWidth(102)
        self._btn_left_list.setMaximumWidth(120)
        self._btn_left_list.currentRowChanged.connect(self.widget_display)

        self.preferences_cancel_btn = QPushButton("取消")
        self.preferences_ok_btn = QPushButton("应用")
        self.preferences_ok_btn.clicked.connect(self.on_preferences_ok_btn_clicked)

        cancel_ok_btn_layout = QHBoxLayout()
        cancel_ok_btn_layout.setContentsMargins(0, 5, 5, 5)
        cancel_ok_btn_layout.setSpacing(5)
        cancel_ok_btn_layout.addStretch()
        cancel_ok_btn_layout.addWidget(self.preferences_cancel_btn)
        cancel_ok_btn_layout.addWidget(self.preferences_ok_btn)

        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)
        self._h_layout = QHBoxLayout()
        self._h_layout.setContentsMargins(0, 0, 0, 0)
        self._h_layout.setSpacing(0)
        self._h_layout.addWidget(self._btn_left_list)
        self._h_layout.addWidget(self._stack)
        self._main_layout.addLayout(self._h_layout)
        self._main_layout.addWidget(self.h_line_4)
        self._main_layout.addLayout(cancel_ok_btn_layout)
        self.setLayout(self._main_layout)

        self.setWindowTitle("偏好设置")
        self.setMinimumSize(500, 400)
        self.setWindowIcon(QIcon(PathHelper.get_img_path("preferences@64x64.png")))
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.update_all_stack_ui()

    def personalise_stack_ui(self):
        """

        :return:
        """
        language_btn_layout = QHBoxLayout()
        language_btn_layout.setContentsMargins(0, 5, 5, 5)
        language_btn_layout.setSpacing(5)
        language_btn_layout.addWidget(self.simplified_chinese_btn)
        language_btn_layout.addWidget(self.traditional_chinese_btn)
        language_btn_layout.addWidget(self.english_btn)

        skin_btn_layout = QHBoxLayout()
        skin_btn_layout.setContentsMargins(0, 5, 5, 5)
        skin_btn_layout.setSpacing(5)
        skin_btn_layout.addWidget(self.dark_skin_btn)
        skin_btn_layout.addWidget(self.white_skin_btn)
        skin_btn_layout.addWidget(self.blue_skin_btn)

        font_btn_layout = QHBoxLayout()
        font_btn_layout.setContentsMargins(0, 5, 5, 5)
        font_btn_layout.setSpacing(5)
        font_btn_layout.addWidget(self.font_btn)

        tool_bar_visibility_btn_layout = QHBoxLayout()
        tool_bar_visibility_btn_layout.setContentsMargins(0, 5, 5, 5)
        tool_bar_visibility_btn_layout.setSpacing(5)
        tool_bar_visibility_btn_layout.addWidget(self.tool_bar_hide)
        tool_bar_visibility_btn_layout.addWidget(self.tool_bar_show)

        tool_bar_pos_btn_layout = QHBoxLayout()
        tool_bar_pos_btn_layout.setContentsMargins(0, 5, 5, 5)
        tool_bar_pos_btn_layout.setSpacing(5)
        tool_bar_pos_btn_layout.addWidget(self.tool_bar_pos_left)
        tool_bar_pos_btn_layout.addWidget(self.tool_bar_pos_right)
        tool_bar_pos_btn_layout.addWidget(self.tool_bar_pos_top)
        tool_bar_pos_btn_layout.addWidget(self.tool_bar_pos_bottom)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)
        main_layout.addWidget(self.language_label)
        main_layout.addLayout(language_btn_layout)
        main_layout.addWidget(self.h_line_1)
        main_layout.addWidget(self.skin_label)
        main_layout.addLayout(skin_btn_layout)
        main_layout.addWidget(self.h_line_2)
        main_layout.addWidget(self.font_label)
        main_layout.addLayout(font_btn_layout)
        main_layout.addWidget(self.h_line_3)
        main_layout.addWidget(self.tool_bar_label)
        main_layout.addLayout(tool_bar_visibility_btn_layout)
        main_layout.addLayout(tool_bar_pos_btn_layout)
        self.personalise_stack.setLayout(main_layout)

    def player_stack_ui(self):
        """

        :return:
        """
        pass

    def update_all_stack_ui(self):
        """

        :return:
        """
        _language = get_language()
        if _language == CommonEnum.LanguageZN:
            self.simplified_chinese_btn.setChecked(True)
        elif _language == CommonEnum.LanguageTN:
            self.traditional_chinese_btn.setChecked(True)
        elif _language == CommonEnum.LanguageEN:
            self.english_btn.setChecked(True)
        else:
            self.simplified_chinese_btn.setChecked(True)

        _skin = get_skin()
        if _skin == CommonEnum.SKinDark:
            self.dark_skin_btn.setChecked(True)
        elif _skin == CommonEnum.SkinWhite:
            self.white_skin_btn.setChecked(True)
        elif _skin == CommonEnum.SkinBlue:
            self.blue_skin_btn.setChecked(True)
        else:
            self.blue_skin_btn.setChecked(True)

        _tool_bar_visible = get_tool_bar_visible()
        if _tool_bar_visible:
            self.tool_bar_show.setChecked(True)
        else:
            self.tool_bar_hide.setChecked(True)

        _tool_bar_pos = get_tool_bar_pos()
        if _tool_bar_pos == CommonEnum.ToolBarPosLeft:
            self.tool_bar_pos_left.setChecked(True)
        elif _tool_bar_pos == CommonEnum.ToolBarPosRight:
            self.tool_bar_pos_right.setChecked(True)
        elif _tool_bar_pos == CommonEnum.ToolBarPosTop:
            self.tool_bar_pos_top.setChecked(True)
        elif _tool_bar_pos == CommonEnum.ToolBarPosBottom:
            self.tool_bar_pos_bottom.setChecked(True)
        else:
            self.tool_bar_pos_top.setChecked(True)

    def widget_display(self, i):
        """ 控制显示的页面

        :param i:
        :return:
        """
        self._stack.setCurrentIndex(i)

    def answer_font_btn_clicked(self, checked):
        """

        :param checked:
        :return:
        """
        set_font(self, False)

    def on_preferences_ok_btn_clicked(self):
        """ 点击应用按钮，更新设置（需要重启应用）

        :return:
        """
        _box = PromptBox(1, "设置成功，重启软件后生效！\n确定立即重启吗？", 2)
        width, height = get_window_center_point(_box)
        _box.move(width, height)
        _flag = _box.exec_()
        _app_info = get_app_info()
        _app_type = _app_info["app_type"]
        # 确认重启且处于 release 状态，则自动重启
        if _flag:

            _language_checkedButton = self.language_btn_group.checkedButton()
            if _language_checkedButton == self.simplified_chinese_btn:
                set_language(CommonEnum.LanguageZN, False)
            elif _language_checkedButton == self.traditional_chinese_btn:
                set_language(CommonEnum.LanguageTN, False)
            elif _language_checkedButton == self.english_btn:
                set_language(CommonEnum.LanguageEN, False)
            else:
                set_language(CommonEnum.LanguageZN, False)

            _skin_checkedButton = self.skin_btn_group.checkedButton()
            print(_skin_checkedButton)
            if _skin_checkedButton == self.dark_skin_btn:
                set_skin(CommonEnum.SKinDark, False)
            elif _skin_checkedButton == self.white_skin_btn:
                set_skin(CommonEnum.SkinWhite, False)
            elif _skin_checkedButton == self.blue_skin_btn:
                set_skin(CommonEnum.SkinBlue, False)
            else:
                set_skin(CommonEnum.SKinDark, False)

            _tool_bar_checkedButton = self.tool_bar_group.checkedButton()
            if _tool_bar_checkedButton == self.tool_bar_hide:
                set_tool_bar_visible(0)
            elif _tool_bar_checkedButton == self.tool_bar_show:
                set_tool_bar_visible(1)
            else:
                set_tool_bar_visible(1)

            _ool_bar_pos_checkedButton = self.tool_bar_pos_group.checkedButton()
            if _ool_bar_pos_checkedButton == self.tool_bar_pos_left:
                set_tool_bar_pos(CommonEnum.ToolBarPosLeft)
            elif _ool_bar_pos_checkedButton == self.tool_bar_pos_right:
                set_tool_bar_pos(CommonEnum.ToolBarPosRight)
            elif _ool_bar_pos_checkedButton == self.tool_bar_pos_top:
                set_tool_bar_pos(CommonEnum.ToolBarPosTop)
            elif _ool_bar_pos_checkedButton == self.tool_bar_pos_bottom:
                set_tool_bar_pos(CommonEnum.ToolBarPosBottom)
            else:
                set_tool_bar_pos(CommonEnum.ToolBarPosTop)

            if _app_type == CommonEnum.AppType.value[1]:
                restart_real_live()
            else:
                _box = PromptBox(0, "debug 状态请手动重启！", 1)
                width, height = get_window_center_point(_box)
                _box.move(width, height)
                _box.exec_()
        self.close()

    def on_preferences_cancel_btn_clicked(self):
        """ 点击取消按钮

        :return:
        """
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    _widget = PreferencesWidget()
    _widget.show()
    sys.exit(app.exec_())
