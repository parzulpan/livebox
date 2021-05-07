# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 通用功能

@Attention :
"""
import platform

from PyQt5.QtWidgets import QDesktopWidget, QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, qApp, QFontDialog, \
    QApplication, QRadioButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QTranslator, QProcess

from utils.path_helper import PathHelper
from utils.crud_json import *
from utils.enums import *
from widgets.loading_widget import LoadingWidget

transform_dict = {"original": "原始色", "light_yellow": "浅色黄", "light_teal": "浅色蓝绿", "light_amber": "浅色琥珀", "light_blue": "浅色蓝",
                  "light_purple": "浅色紫", "light_cyan": "浅色青", "light_lightgreen": "浅色浅绿", "light_pink": "浅色粉",
                  "light_red": "浅色红", "dark_yellow": "暗黑黄", "dark_teal": "暗黑蓝绿", "dark_amber": "暗黑琥珀",
                  "dark_blue": "暗黑蓝", "dark_purple": "暗黑紫", "dark_cyan": "暗黑青", "dark_lightgreen": "暗黑浅绿",
                  "dark_pink": "暗黑粉", "dark_red": "暗黑红"}


def get_keys(d: dict, value: str):
    """ 根据字典的 value 得到 key

    :param d:
    :param value:
    :return:
    """
    keys = [k for k, v in d.items() if v == value]
    if len(keys) == 0:
        return "null"
    elif len(keys) == 1:
        return keys[0]
    else:
        return keys


def get_value(d: dict, key: str):
    """ 根据字典的 key 得到 value

    :param d:
    :param key:
    :return:
    """
    if d[key]:
        return d[key]
    else:
        return "null"


def get_window_center_point(widget):
    """ 使窗口居中显示

    :param widget: 需要居中显示的窗口
    :return:
    """

    desktop_widget = QDesktopWidget()
    screen_rect = desktop_widget.screenGeometry()
    return (screen_rect.width() - widget.width()) / 2, (screen_rect.height() - widget.height()) / 2


def loading():
    """

    :return:
    """
    loading_widget = LoadingWidget()
    width, height = get_window_center_point(loading_widget)
    loading_widget.move(width, height)
    loading_widget.exec_()


def restart_real_live():
    """ 进程控制实现自动重启
    Notes:
    常用的有两种方式实现重启：
    1. 进程控制，退出当前进程，再通过 QProcess 启动一个新的进程
    2. 事件循环，退出应用程序，然后通过 Application 事件循环控制程序启动

    :return:
    """
    qApp.quit()
    p = QProcess
    p.startDetached(qApp.applicationFilePath())


def get_system_platform():
    """

    :return:
    """

    _platform = platform.system()
    print("system_platform: ", _platform)
    if CommonEnum.WindowsPlatform.value[1] == _platform:
        return CommonEnum.WindowsPlatform
    elif CommonEnum.LinuxPlatform.value[1] == _platform:
        return CommonEnum.LinuxPlatform
    elif CommonEnum.DarwinPlatform.value[1] == _platform:
        return CommonEnum.DarwinPlatform
    else:
        return CommonEnum.LinuxPlatform


def set_theme(theme: str, dynamic=True):
    """

    :param theme:
    :param dynamic:
    :return:
    """
    _theme = get_keys(transform_dict, theme)
    if dynamic:
        # with open(PathHelper.get_qss_path(f"{_theme}.qss"), "r", encoding="utf-8") as f:
        #     qss = f.read()
        #     qApp.setStyleSheet(qss)
        pass
    default_json2python4file["preferences"]["personalise"]["theme"] = _theme
    python2json2file(default_json2python4file)


def get_theme():
    """

    :return:
    """
    return default_json2python4file["preferences"]["personalise"]["theme"]


def set_skin(skin: CommonEnum, dynamic=True):
    """

    :param skin:
    :param dynamic:
    :return:
    """

    _skin = skin.value[1]
    if dynamic:
        # with open(PathHelper.get_qss_path(f"{_skin}.qss"), "r", encoding="utf-8") as f:
        #     qss = f.read()
        #     qApp.setStyleSheet(qss)
        pass
    default_json2python4file["preferences"]["personalise"]["skin"] = _skin
    python2json2file(default_json2python4file)


def get_skin():
    """

    :return:
    """

    _skin = default_json2python4file["preferences"]["personalise"]["skin"]
    if _skin == CommonEnum.SkinBlue.value[1]:
        return CommonEnum.SkinBlue
    elif _skin == CommonEnum.SKinDark.value[1]:
        return CommonEnum.SKinDark
    elif _skin == CommonEnum.SkinWhite.value[1]:
        return CommonEnum.SkinWhite
    else:
        return CommonEnum.SkinBlue


def set_font(parent=None, dynamic=True):
    """

    :param parent:
    :param dynamic:
    :return:
    """

    font = qApp.font()
    font, changed = QFontDialog().getFont(font, parent, caption="字体设置")
    if changed:
        if dynamic:
            qApp.setFont(font)
            qApp.processEvents()
        default_json2python4file["preferences"]["personalise"]["font-family"] = font.family()
        default_json2python4file["preferences"]["personalise"]["font-style"] = font.styleName()
        default_json2python4file["preferences"]["personalise"]["font-size"] = font.pointSize()
        python2json2file(default_json2python4file)


def get_font():
    """

    :return:
    """

    font_family = default_json2python4file["preferences"]["personalise"]["font-family"]
    font_style = default_json2python4file["preferences"]["personalise"]["font-style"]
    font_size = default_json2python4file["preferences"]["personalise"]["font-size"]
    return {"font_family": font_family, "font_style": font_style, "font_size": font_size}


def set_language(language: CommonEnum, dynamic=True):
    """

    :param language:
    :param dynamic:
    :return:
    """

    _language = language.value[1]
    if dynamic:
        # TODO: 国际化支持
        # trans = QTranslator()
        # trans.load()
        # qApp.installTranslator(trans)
        pass
    default_json2python4file["preferences"]["personalise"]["language"] = _language
    python2json2file(default_json2python4file)


def get_language():
    """

    :return:
    """

    _language = default_json2python4file["preferences"]["personalise"]["language"]
    if _language == CommonEnum.LanguageZN.value[1]:
        return CommonEnum.LanguageZN
    elif _language == CommonEnum.LanguageTN.value[1]:
        return CommonEnum.LanguageTN
    elif _language == CommonEnum.LanguageEN.value[1]:
        return CommonEnum.LanguageEN
    else:
        return CommonEnum.LanguageZN


def set_tool_bar_visible(visible: int):
    """

    :param visible:
    :return:
    """

    default_json2python4file["preferences"]["personalise"]["tool_bar_visible"] = visible
    python2json2file(default_json2python4file)


def get_tool_bar_visible():
    """

    :return:
    """

    return default_json2python4file["preferences"]["personalise"]["tool_bar_visible"]


def set_tool_bar_pos(tool_bar_pos: CommonEnum):
    """

    :param tool_bar_pos:
    :return:
    """
    _tool_bar_pos = tool_bar_pos.value[1]
    default_json2python4file["preferences"]["personalise"]["tool_bar_pos"] = _tool_bar_pos
    python2json2file(default_json2python4file)


def get_tool_bar_pos():
    """

    :return:
    """

    _tool_bar_pos = default_json2python4file["preferences"]["personalise"]["tool_bar_pos"]
    if _tool_bar_pos == CommonEnum.ToolBarPosLeft.value[1]:
        return CommonEnum.ToolBarPosLeft
    elif _tool_bar_pos == CommonEnum.ToolBarPosRight.value[1]:
        return CommonEnum.ToolBarPosRight
    elif _tool_bar_pos == CommonEnum.ToolBarPosTop.value[1]:
        return CommonEnum.ToolBarPosTop
    elif _tool_bar_pos == CommonEnum.ToolBarPosBottom.value[1]:
        return CommonEnum.ToolBarPosBottom
    else:
        return CommonEnum.ToolBarPosTop


def set_app_info(data: dict):
    """

    :param data:
    :return:
    """

    default_json2python4file["app_info"] = data
    python2json2file(default_json2python4file)


def get_app_info():
    """

    :return:
    """

    return default_json2python4file["app_info"]


class PromptBox(QDialog):
    """ 通用提示弹窗

    """

    def __init__(self, box_type: int, content: str, btn_cnt: int = 1):
        """

        :param box_type: 提示弹窗类型，0代表成功提示弹窗，1代表询问提示弹窗，2代表警告提示弹窗，3代表错误提示弹窗
        :param content: 提示弹窗的文本信息，注意:当文本过长时,可用\n将文本换行
        :param btn_cnt: 提示弹窗类型的按钮个数，1代表有一个按钮，2代表有两个按钮，默认为1
        :return: True or False
        """
        super(PromptBox, self).__init__()
        self._icon_label = QLabel()
        # self._icon_label.setFixedSize(48, 48)

        self._content_label = QLabel(content)

        self._btn_one = QPushButton("确 定")
        self._btn_one.clicked.connect(self.answer_btn_one_clicked)
        self._btn_two = QPushButton("取 消")
        self._btn_two.clicked.connect(self.answer_btn_two_clicked)

        self._btn_layout = QHBoxLayout()
        self._btn_layout.setContentsMargins(5, 5, 5, 5)
        self._btn_layout.setSpacing(10)
        self._btn_layout.addStretch()

        if box_type == 0:
            self._icon_label.setPixmap(QPixmap(PathHelper.get_img_path("box_success@32x32.png")))
        elif box_type == 1:
            self._icon_label.setPixmap(QPixmap(PathHelper.get_img_path("box_question@32x32.png")))
        elif box_type == 2:
            self._icon_label.setPixmap(QPixmap(PathHelper.get_img_path("box_warning@32x32.png")))
        elif box_type == 3:
            self._icon_label.setPixmap(QPixmap(PathHelper.get_img_path("box_error@32x32.png")))
        else:
            self._icon_label.setPixmap(QPixmap(PathHelper.get_img_path("box_success@32x32.png")))

        if btn_cnt == 1:
            self._btn_layout.addWidget(self._btn_one)
        elif btn_cnt == 2:
            self._btn_layout.addWidget(self._btn_two)
            self._btn_layout.addWidget(self._btn_one)
        else:
            self._btn_layout.addWidget(self._btn_one)

        self._label_layout = QHBoxLayout()
        self._label_layout.setContentsMargins(5, 5, 5, 5)
        self._label_layout.setSpacing(15)
        # self._label_layout.addStretch()
        self._label_layout.addWidget(self._icon_label)
        self._label_layout.addWidget(self._content_label)
        self._label_layout.addStretch()

        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(5, 5, 5, 5)
        self._main_layout.setSpacing(10)
        self._main_layout.addLayout(self._label_layout)
        self._main_layout.addLayout(self._btn_layout)
        self.setLayout(self._main_layout)

        self.setWindowTitle("提示")
        self.setWindowIcon(QIcon(PathHelper.get_img_path("logo@48x48.png")))
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setFixedSize(280, 140)

    def answer_btn_one_clicked(self):
        """

        :return:
        """
        # self.close()
        # return True
        self.accept()

    def answer_btn_two_clicked(self):
        """

        :return:
        """
        # self.close()
        # return False
        self.reject()


class ControlBtn(QPushButton):
    """ 播放控制按钮

    """

    def __init__(self, img, clicked_img):
        super(ControlBtn, self).__init__()
        self.setAutoFillBackground(True)
        img = PathHelper.get_img_path(img)
        clicked_img = PathHelper.get_img_path(clicked_img)
        self.setCheckable(True)
        self.setStyleSheet(
            "QPushButton{min-width:32px; min-height:32px; max-width:32px; max-height:32px; "
            "border-image:url(\"%s\"); }"
            "QPushButton:checked{border-image:url(\"%s\"); }"
            "QPushButton::menu-indicator{image: None; }" % (img, clicked_img))


class PreferencesQRadioButton(QRadioButton):
    """ 偏好设置的单选按钮

    """

    def __int__(self):
        super(PreferencesQRadioButton, self).__int__()
        self.setCheckable(True)
