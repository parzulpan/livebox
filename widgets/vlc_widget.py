# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""

import sys
import os
import platform

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QHBoxLayout, QVBoxLayout, QFrame, QMainWindow, \
    QLabel
from PyQt5.QtCore import Qt

from utils.common import CommonBtn

# 设置VLC库路径，需在import vlc之前
os.environ['PYTHON_VLC_MODULE_PATH'] = "./core/vlc_3.0.9.2"
import vlc


class VLCWidget(QMainWindow):
    """

    """

    def __init__(self, *args):
        super(VLCWidget, self).__init__()

        self.media_player = None
        self.instance = None
        if args:
            self.instance = vlc.Instance(*args)
            self.media_player = self.instance.media_player_new()
        else:
            self.media_player = vlc.MediaPlayer()

        if platform.system() == "Windows":
            self.media_player_frame = QFrame()
            self.media_player.set_hwnd(self.media_player_frame.winId())
        elif platform.system() == "Linux":
            self.media_player_frame = QFrame()
            self.media_player.set_xwindow(self.media_player_frame.winId())
        elif platform.system() == "Darwin":
            # self.media_player_frame = QMacCocoaViewContainer(0)
            self.media_player.set_nsobject(self.media_player_frame.winId())
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.palette = self.media_player_frame.palette()
        self.palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.media_player_frame.setPalette(self.palette)
        self.media_player_frame.setAutoFillBackground(True)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.control_widget = QWidget()
        self.control_widget.setFixedHeight(24+5+5)
        self.control_layout = QHBoxLayout(self.control_widget)
        self.control_layout.setContentsMargins(5, 5, 5, 5)
        self.control_layout.setSpacing(0)
        self.play_pause_btn = CommonBtn("./resources/img/pause@64x64.png",
                                        "./resources/img/play@64x64.png")
        self.play_pause_btn.setToolTip("播放/暂停")
        self.play_pause_btn.setShortcut(Qt.Key_Space)
        self.play_pause_btn.clicked.connect(self.answer_play_pause_btn_clicked)
        self.refresh_btn = CommonBtn("./resources/img/refresh@64x64.png",
                                     "./resources/img/refresh@64x64.png")
        self.refresh_btn.setToolTip("刷新")
        self.refresh_btn.clicked.connect(self.answer_refresh_btn_clicked)

        self.rewind_btn = CommonBtn("./resources/img/rewind@64x64.png",
                                    "./resources/img/rewind@64x64.png")
        self.rewind_btn.setToolTip("后退10秒")
        self.rewind_btn.clicked.connect(self.answer_rewind_btn_clicked)
        self.stop_btn = CommonBtn("./resources/img/stop@64x64.png",
                                  "./resources/img/stop@64x64.png")
        self.stop_btn.setToolTip("停止")
        self.stop_btn.clicked.connect(self.answer_stop_btn_clicked)
        self.fast_forward_btn = CommonBtn("./resources/img/fast_forward@64x64.png",
                                          "./resources/img/fast_forward@64x64.png")
        self.fast_forward_btn.setToolTip("前进10秒")
        self.fast_forward_btn.clicked.connect(self.answer_fast_forward_btn_clicked)

        self.fullscreen_narrow_btn = CommonBtn("./resources/img/fullscreen@64x64.png",
                                               "./resources/img/narrow@64x64.png")
        self.fullscreen_narrow_btn.setToolTip("最大化/最小化")
        self.fullscreen_narrow_btn.setShortcut(Qt.Key_Escape)
        self.fullscreen_narrow_btn.clicked.connect(self.answer_fullscreen_narrow_btn_clicked)
        self.collect_btn = CommonBtn("./resources/img/collect@64x64.png",
                                     "./resources/img/collect@64x64.png")
        self.collect_btn.setToolTip("收藏")
        self.collect_btn.clicked.connect(self.answer_collect_btn_clicked)
        self.menu_btn = CommonBtn("./resources/img/menu@64x64.png",
                                  "./resources/img/menu@64x64.png")
        self.menu_btn.setToolTip("菜单")
        self.menu_btn.clicked.connect(self.answer_menu_btn_clicked)

        self.volume_btn = CommonBtn("./resources/img/volume@64x64.png",
                                    "./resources/img/mute@64x64.png")
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

        self._init_ui()

    def _init_ui(self):
        """

        :return:
        """
        self.control_layout.addWidget(self.play_pause_btn)
        self.control_layout.addWidget(self.refresh_btn)
        self.control_layout.addSpacing(10)
        self.control_layout.addWidget(self.rewind_btn)
        self.control_layout.addWidget(self.stop_btn)
        self.control_layout.addWidget(self.fast_forward_btn)
        self.control_layout.addSpacing(10)
        self.control_layout.addWidget(self.fullscreen_narrow_btn)
        self.control_layout.addWidget(self.collect_btn)
        self.control_layout.addWidget(self.menu_btn)
        self.control_layout.addSpacing(10)
        self.control_layout.addStretch()
        self.control_layout.addWidget(self.volume_btn)
        self.control_layout.addWidget(self.volume_slider_value_label)
        self.control_layout.addWidget(self.volume_slider)
        self.control_layout.addSpacing(10)

        self.main_layout.addWidget(self.media_player_frame)
        self.main_layout.addWidget(self.control_widget)
        # self.main_layout.addSpacing(1)
        # self.main_layout.addLayout(self.control_layout)

        self.widget.setLayout(self.main_layout)

    def release_player(self):
        """ 释放资源

        :return:
        """
        return self.media_player.release()

    def play_url(self, url=None):
        """

        :param url:
        :return:
        """
        try:
            # url = "http://tx2play1.douyucdn.cn/live/288016rlols5.flv?uuid="
            if url:
                self.current_url = url
                self.media_player.set_mrl(url)
                self.media_player_frame.show()
                self.control_widget.show()
                self.volume_slider.setValue(80)
                self.play_pause_btn.setChecked(False)
                return self.media_player.play()
            else:
                pass
        except Exception as e:
            print('[play_url exception] {0}'.format(e))
            return False

    def pause(self):
        """ 暂停

        :return:
        """
        self.media_player.pause()

    def resume(self):
        """ 恢复

        :return:
        """
        self.media_player.set_pause(0)

    def stop(self):
        """ 停止

        :return:
        """
        self.media_player_frame.hide()
        self.control_widget.hide()
        self.media_player.stop()
        # self.release_player()

    def is_playing(self):
        """ 是否正在播放

        :return:
        """
        return self.media_player.is_playing()

    def get_time(self):
        """ 已播放时间，返回毫秒值

        :return:
        """
        return self.media_player.get_time()

    def set_time(self, ms):
        """ 拖动指定的毫秒值处播放。成功返回0，失败返回-1 (需要注意，只有当前多媒体格式或流媒体协议支持才会生效)

        :param ms:
        :return:
        """
        return self.media_player.set_time(ms)

    def get_length(self):
        """ 音视频总长度，返回毫秒值

        :return:
        """
        return self.media_player.get_length()

    def get_volume(self):
        """ 获取当前音量（0~100）

        :return:
        """
        return self.media_player.audio_get_volume()

    def set_volume(self, volume):
        """

        :param volume:
        :return:
        """
        return self.media_player.audio_set_volume(volume)

    def get_state(self):
        """ 返回当前状态：正在播放、暂停中、其他

        :return:
        """
        state = self.media_player.get_state()
        if state == vlc.State(3):
            return 1
        elif state == vlc.State(4):
            return 0
        else:
            return -1

    def set_position(self, float_val):
        """ 拖动当前进度，传入0.0~1.0之间的浮点数(需要注意，只有当前多媒体格式或流媒体协议支持才会生效)

        :param float_val:
        :return:
        """
        return self.media_player.set_position(float_val)

    def get_rate(self):
        """ 获取当前文件播放速率

        :return:
        """
        return self.media_player.get_rate()

    def set_rate(self, rate):
        """ 设置播放速率（如：1.2，表示加速1.2倍播放）

        :param rate:
        :return:
        """
        return self.media_player.set_rate(rate)

    def set_ratio(self, ratio):
        """ 设置宽高比率（如"16:9","4:3"）

        :param ratio:
        :return:
        """
        # 必须设置为0，否则无法修改屏幕宽高
        self.media_player.video_set_scale(0)
        self.media_player.video_set_aspect_ratio(ratio)

    def add_callback(self, event_type, callback):
        """ 注册监听器

        :param event_type: VLC的监听器类型
        :param callback:
        :return:
        """
        # VLC的监听器类型
        # MediaPlayerNothingSpecial：vlc处于空闲状态，只是等待发出命令
        # MediaPlayerOpening：vlc正在打开媒体资源定位器（MRL）
        # MediaPlayerBuffering(intcache)：vlc正在缓冲
        # MediaPlayerPlaying：vlc正在播放媒体
        # MediaPlayerPaused：vlc处于暂停状态
        # MediaPlayerStopped：vlc处于停止状态
        # MediaPlayerForward：vlc通过媒体快进（这永远不会被调用）
        # MediaPlayerBackward：vlc正在快退（这永远不会被调用）
        # MediaPlayerEncounteredError：vlc遇到错误，无法继续
        # MediaPlayerEndReached：vlc已到达当前播放列表的末尾
        # MediaPlayerTimeChanged：时间发生改变
        # MediaPlayerPositionChanged：进度发生改变
        # MediaPlayerSeekableChanged：流媒体是否可搜索的状态发生改变（true表示可搜索，false表示不可搜索）
        # MediaPlayerPausableChanged：媒体是否可暂停状态发生改变（true表示可暂停，false表示不可暂停）
        # MediaPlayerMediaChanged: 媒体发生改变
        # MediaPlayerTitleChanged: 标题发生改变（DVD / Blu - ray）
        # MediaPlayerChapterChanged: 章节发生改变（DVD / Blu - ray）
        # MediaPlayerLengthChanged: (在vlc版本 < 2.2.0仅适用于Mozilla）长度已更改
        # MediaPlayerVout:视频输出的数量发生改变
        # MediaPlayerMuted:静音
        # MediaPlayerUnmuted:取消静音
        # MediaPlayerAudioVolume:音量发生改变

        self.media_player.event_manager().event_attach(event_type, callback)

    def remove_callback(self, event_type, callback):
        """ 移除监听器

        :param event_type:
        :param callback:
        :return:
        """
        self.media_player.event_manager().event_detach(event_type, callback)

    def set_marquee(self):
        """ 设置字幕

        :return:
        """
        # VideoMarqueeOption.Color ：文本颜色，值为16进制数
        # VideoMarqueeOption.Enable：是否开启文本显示，1表示开启
        # VideoMarqueeOption.Opacity：文本透明度，0透明，255完全不透明
        # VideoMarqueeOption.Position：文本显示的位置
        # VideoMarqueeOption.Refresh：字符串刷新的间隔（毫秒）对时间格式字串刷新有用
        # VideoMarqueeOption.Size：文字大小，单位像素
        # VideoMarqueeOption.Text：要显示的文本内容
        # VideoMarqueeOption.Timeout：文本停留时间。0表示永远停留（毫秒值）
        # VideoMarqueeOption.marquee_X：设置显示文本的x坐标值
        # VideoMarqueeOption.marquee_Y：设置显示文本的y坐标值
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Enable, 1)
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Size, 28)
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Color, 0xff0000)
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Position, vlc.Position.Bottom)
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Timeout, 0)
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Refresh, 10000)

    def update_content(self, content="%Y-%m-%d %H:%M:%S"):
        """ 设置字幕内容

        :param content: 默认为时间格式，会在屏幕下方显示当前时间，且每一秒刷新一次。
        :return:
        """
        self.media_player.video_set_marquee_string(vlc.VideoMarqueeOption.Text, content)

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
    vlc_widget = VLCWidget()
    vlc_widget.show()
    vlc_widget.play_url()
    sys.exit(app.exec_())
