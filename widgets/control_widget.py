# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 播放控制

@Attention :
"""

import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QSlider
from PyQt5.QtCore import Qt

from utils.common import CommonBtn


class ControlWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.play_pause_btn = CommonBtn("pause@64x64.png", "play@64x64.png")
        self.play_pause_btn.setToolTip("播放/暂停")
        self.play_pause_btn.setShortcut(Qt.Key_Space)
        self.play_pause_btn.clicked.connect(self.answer_play_pause_btn_clicked)

        self.refresh_btn = CommonBtn("refresh@64x64.png", "refresh@64x64.png")
        self.refresh_btn.setToolTip("刷新")
        self.refresh_btn.clicked.connect(self.answer_refresh_btn_clicked)

        self.rewind_btn = CommonBtn("rewind@64x64.png", "rewind@64x64.png")
        self.rewind_btn.setToolTip("后退10秒")
        self.rewind_btn.clicked.connect(self.answer_rewind_btn_clicked)

        self.stop_btn = CommonBtn("stop@64x64.png", "stop@64x64.png")
        self.stop_btn.setToolTip("停止")
        self.stop_btn.clicked.connect(self.answer_stop_btn_clicked)

        self.fast_forward_btn = CommonBtn("fast_forward@64x64.png", "fast_forward@64x64.png")
        self.fast_forward_btn.setToolTip("前进10秒")
        self.fast_forward_btn.clicked.connect(self.answer_fast_forward_btn_clicked)

        self.fullscreen_narrow_btn = CommonBtn("fullscreen@64x64.png", "narrow@64x64.png")
        self.fullscreen_narrow_btn.setToolTip("最大化/最小化")
        self.fullscreen_narrow_btn.setShortcut(Qt.Key_Escape)
        self.fullscreen_narrow_btn.clicked.connect(self.answer_fullscreen_narrow_btn_clicked)

        self.collect_btn = CommonBtn("collect@64x64.png", "collect@64x64.png")
        self.collect_btn.setToolTip("收藏")
        self.collect_btn.clicked.connect(self.answer_collect_btn_clicked)

        self.menu_btn = CommonBtn("menu@64x64.png", "menu@64x64.png")
        self.menu_btn.setToolTip("菜单")
        self.menu_btn.clicked.connect(self.answer_menu_btn_clicked)

        self.volume_btn = CommonBtn("volume@64x64.png", "mute@64x64.png")
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

        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(5, 5, 5, 5)

        self._init_ui()

    def _init_ui(self):

        self.main_layout.addWidget(self.play_pause_btn)
        self.main_layout.addWidget(self.refresh_btn)
        self.main_layout.addSpacing(10)
        self.main_layout.addWidget(self.rewind_btn)
        self.main_layout.addWidget(self.stop_btn)
        self.main_layout.addWidget(self.fast_forward_btn)
        self.main_layout.addSpacing(10)
        self.main_layout.addWidget(self.fullscreen_narrow_btn)
        self.main_layout.addWidget(self.collect_btn)
        self.main_layout.addWidget(self.menu_btn)
        self.main_layout.addSpacing(10)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.volume_btn)
        self.main_layout.addWidget(self.volume_slider_value_label)
        self.main_layout.addWidget(self.volume_slider)
        self.main_layout.addSpacing(10)
        self.setLayout(self.main_layout)

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

    def answer_collect_btn_clicked(self):
        """

        :return:
        """
        pass

    def answer_menu_btn_clicked(self):
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
        volume_value = self.volume_slider.value()
        if 0 == volume_value:
            self.volume_btn.setChecked(True)
        else:
            self.volume_btn.setChecked(False)
        self.volume_slider_value_label.setText("{0}%".format(volume_value))
        self.set_volume(volume_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    control_widget = ControlWidget()
    control_widget.show()
    sys.exit(app.exec_())
