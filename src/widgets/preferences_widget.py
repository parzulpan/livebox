# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 偏好设置页面

@Attention :
"""
import sys

from PyQt5.QtWidgets import QWidget, QStackedWidget, QListWidget, QListWidgetItem, QLabel, QRadioButton, QPushButton,\
    QHBoxLayout, QVBoxLayout, QFrame, QDialog, QApplication, qApp, QFontDialog, QButtonGroup
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

from utils.crud_cfg import *


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

        self.language_label = QLabel("界面语言")
        self.language_btn_group = QButtonGroup()
        self.simplified_chinese_btn = QRadioButton("简体中文")
        self.traditional_chinese_btn = QRadioButton("繁体中文")
        self.english_btn = QRadioButton("English")
        self.language_btn_group.addButton(self.simplified_chinese_btn)
        self.language_btn_group.addButton(self.traditional_chinese_btn)
        self.language_btn_group.addButton(self.english_btn)
        self.skin_label = QLabel("界面皮肤")
        self.skin_btn_group = QButtonGroup()
        self.dark_skin_btn = QRadioButton("暗黑模式")
        self.white_skin_btn = QRadioButton("纯白模式")
        self.blue_skin_btn = QRadioButton("浅蓝模式")
        self.skin_btn_group.addButton(self.dark_skin_btn)
        self.skin_btn_group.addButton(self.white_skin_btn)
        self.skin_btn_group.addButton(self.blue_skin_btn)
        self.font_label = QLabel("界面字体")
        self.font_btn = QPushButton("点击设置")
        self.font_btn.clicked.connect(self.answer_font_btn_clicked)
        self.tool_bar_visibility_label = QLabel("工具栏默认隐藏")
        self.tool_bar_visibility_group = QButtonGroup()
        self.tool_bar_hide = QRadioButton("是")
        self.tool_bar_show = QRadioButton("否")
        self.tool_bar_visibility_group.addButton(self.tool_bar_hide)
        self.tool_bar_visibility_group.addButton(self.tool_bar_show)
        self.personalise_stack_ui()
        self.player_stack_ui()

        self._stack = QStackedWidget()
        self._stack.addWidget(self.personalise_stack)
        self._stack.addWidget(self.player_stack)
        self._btn_left_list = QListWidget()
        _personalise_item = QListWidgetItem('个性化')
        _personalise_item.setTextAlignment(Qt.AlignCenter)
        _personalise_item.setSizeHint(QSize(80, 40))
        self._btn_left_list.insertItem(0, _personalise_item)
        _player_item = QListWidgetItem('播放器')
        _player_item.setTextAlignment(Qt.AlignCenter)
        _player_item.setSizeHint(QSize(80, 40))
        self._btn_left_list.insertItem(1, _player_item)
        self._btn_left_list.setCurrentRow(0)
        self._btn_left_list.setFixedWidth(82)
        self._btn_left_list.currentRowChanged.connect(self.widget_display)

        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)
        self._h_layout = QHBoxLayout()
        self._h_layout.setContentsMargins(0, 0, 0, 0)
        self._h_layout.setSpacing(0)
        self._h_layout.addWidget(self._btn_left_list)
        self._h_layout.addWidget(self._stack)
        self._main_layout.addLayout(self._h_layout)
        self.setLayout(self._main_layout)

        self.setWindowTitle("偏好设置")
        self.setWindowIcon(QIcon(PathHelper.get_img_path("preferences@64x64.png")))
        self.setWindowFlags(Qt.WindowCloseButtonHint)

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
        main_layout.addWidget(self.tool_bar_visibility_label)
        main_layout.addLayout(tool_bar_visibility_btn_layout)
        self.personalise_stack.setLayout(main_layout)

    def update_personalise_stack_ui(self):
        """

        :return:
        """
        pass

    def player_stack_ui(self):
        """

        :return:
        """
        pass

    def update_player_stack_ui(self):
        """

        :return:
        """
        pass

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
        font: QFont = qApp.font()
        font, changed = QFontDialog().getFont(font, self, caption="字体设置")
        if changed:
            qApp.setFont(font)
            qApp.processEvents()
            update_contents("preferences", "font-family", font.family())
            update_contents("preferences", "font-style", font.styleName())
            update_contents("preferences", "font-size", str(font.pointSize()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    _widget = PreferencesWidget()
    _widget.show()
    sys.exit(app.exec_())
