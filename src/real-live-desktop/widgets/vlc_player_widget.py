# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 开源的 VLC 接口封装的 媒体播放器

@Attention :
"""

import sys
import os

from PyQt5.QtCore import QEvent, pyqtSignal
from PyQt5.QtGui import QPalette, QColor, QKeyEvent, QMouseEvent
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QFrame, QMainWindow, QMenu

from utils.enums import *
from utils.states import PlayerState
from utils.path_helper import PathHelper
from utils.common import *


# # 设置VLC库路径，需在import vlc之前
# if get_system_platform() == CommonEnum.WindowsPlatform:
#     os.environ['PYTHON_VLC_MODULE_PATH'] = PathHelper.get_python_vlc_module_path("Windows")
# elif get_system_platform() == CommonEnum.LinuxPlatform:
#     os.environ['PYTHON_VLC_MODULE_PATH'] = PathHelper.get_python_vlc_module_path("Linux")
# elif get_system_platform() == CommonEnum.DarwinPlatform:
#     os.environ['PYTHON_VLC_MODULE_PATH'] = PathHelper.get_python_vlc_module_path("Darwin")
# else:
#     os.environ['PYTHON_VLC_MODULE_PATH'] = PathHelper.get_python_vlc_module_path("Windows")

import vlc


class VlcPlayerWidget(QMainWindow):
    """

    """
    showFullScreen_signal = pyqtSignal()
    showNormal_signal = pyqtSignal()

    def __init__(self, *args):
        super(VlcPlayerWidget, self).__init__()

        self.media_player_frame = QFrame()
        self.media_player = None
        self.instance = None
        self.set_media_player(args)
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.palette = self.media_player_frame.palette()
        self.palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.media_player_frame.setPalette(self.palette)
        self.media_player_frame.setAutoFillBackground(True)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.current_url = None
        self.current_url_type = None

        self._init_ui()
        self.init_cfg()

    def _init_ui(self):
        """

        :return:
        """
        self.main_layout.addWidget(self.media_player_frame)
        self.widget.setLayout(self.main_layout)
        self.widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.widget.customContextMenuRequested.connect(self.custom_right_menu)
        self.setCentralWidget(self.widget)
        self.setStyleSheet(f"border-image:url({PathHelper.get_img_path('live_null.png')}); ")

    def init_cfg(self):
        """

        :return:
        """
        self.vlc_set_volume(20)

    def set_media_player(self, *args):
        """ 获得并设置媒体播放器

        :param args:
        :return:
        """
        if args:
            self.instance = vlc.Instance(*args)
            self.media_player = self.instance.media_player_new()
        else:
            self.media_player = vlc.MediaPlayer()

        if get_system_platform() == CommonEnum.WindowsPlatform:
            self.media_player_frame = QFrame()
            # self.media_player.set_hwnd(int(self.media_player_frame.winId()))
        elif get_system_platform() == CommonEnum.LinuxPlatform:
            self.media_player_frame = QFrame()
            # self.media_player.set_xwindow(int(self.media_player_frame.winId()))
        elif get_system_platform() == CommonEnum.DarwinPlatform:
            from PyQt5.QtWidgets import QMacCocoaViewContainer
            self.media_player_frame = QMacCocoaViewContainer(0)
            # self.media_player.set_nsobject(int(self.media_player_frame.winId()))
        else:
            self.media_player_frame = QFrame()
            # self.media_player.set_hwnd(int(self.media_player_frame.winId()))

    def custom_right_menu(self, pos):
        """

        :param pos:
        :return:
        """
        if not (PlayerState.Load == PlayerEnum.LoadStopped or PlayerState.Load == PlayerEnum.LoadNothingSpecial):
            menu = QMenu()

            if PlayerState.Load == PlayerEnum.LoadPlaying:
                play_pause_opt = menu.addAction("暂停")
            elif PlayerState.Load == PlayerEnum.LoadPaused:
                play_pause_opt = menu.addAction("播放")
            else:
                play_pause_opt = menu.addAction("暂停")

            refresh_opt = menu.addAction("刷新")

            stop_opt = menu.addAction("停止")

            menu.addSeparator()

            if PlayerState.Size == PlayerEnum.SizeMax:
                fullscreen_opt = menu.addAction("复原")
            else:
                fullscreen_opt = menu.addAction("全屏")

            menu.addSeparator()

            mute_opt = menu.addAction("静音")

            action = menu.exec_(self.widget.mapToGlobal(pos))
            if action == play_pause_opt:
                if PlayerState.Load == PlayerEnum.LoadPlaying:
                    self.vlc_pause()
                else:
                    self.vlc_resume()
            elif action == refresh_opt:
                self.vlc_stop()
                self.vlc_play(self.current_url, self.current_url_type)
            elif action == stop_opt:
                self.vlc_stop()
            elif action == fullscreen_opt:
                if PlayerState.Size == PlayerEnum.SizeMax:
                    self.vlc_set_size(False)
                else:
                    self.vlc_set_size(True)
            elif action == mute_opt:
                self.vlc_set_volume(-self.vlc_get_volume())

    def enterEvent(self, event: QEvent) -> None:
        """

        :param event:
        :return:
        """
        if not (PlayerState.Load == PlayerEnum.LoadStopped or PlayerState.Load == PlayerEnum.LoadNothingSpecial):
            # print("enterEvent")
            self.grabKeyboard()

    def leaveEvent(self, event: QEvent) -> None:
        """

        :param event:
        :return:
        """
        if not (PlayerState.Load == PlayerEnum.LoadStopped or PlayerState.Load == PlayerEnum.LoadNothingSpecial):
            # print("leaveEvent")
            self.releaseKeyboard()

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        """

        :param event:
        :return:
        """
        pass
        # if not (PlayerState.Load == PlayerEnum.LoadStopped or PlayerState.Load == PlayerEnum.LoadNothingSpecial):
        #     # print("mouseDoubleClickEvent")
        #     if PlayerState.Size == PlayerEnum.SizeMax:
        #         self.vlc_set_size(False)
        #     else:
        #         self.vlc_set_size(True)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """ 重写键盘按下事件

        :param event:
        :return:
        """
        if not (PlayerState.Load == PlayerEnum.LoadStopped or PlayerState.Load == PlayerEnum.LoadNothingSpecial):
            # print("keyPressEvent", event)
            if event.key() == Qt.Key_Escape:
                self.vlc_set_size(False)
            elif event.key() == Qt.Key_Left:
                if PlayerState.MrlType == PlayerEnum.MrlTypeLocal:
                    self.vlc_set_time(PlayerState.EachDecreaseTime)
            elif event.key() == Qt.Key_Right:
                if PlayerState.MrlType == PlayerEnum.MrlTypeLocal:
                    self.vlc_set_time(PlayerState.EachIncreaseTime)
            elif event.key() == Qt.Key_Up:
                self.vlc_set_volume(PlayerState.EachIncreaseVolume)
            elif event.key() == Qt.Key_Down:
                self.vlc_set_volume(PlayerState.EachDecreaseVolume)
            elif event.key() == Qt.Key_Space:
                if PlayerState.Load == PlayerEnum.LoadPlaying:
                    self.vlc_pause()
                else:
                    self.vlc_resume()
            else:
                pass

    def vlc_release(self):
        """ 释放资源

        :return:
        """
        return self.media_player.release()

    def vlc_play(self, url: str, url_type: PlayerEnum):
        """ 播放

        :param url:
        :param url_type:
        :return:
        """
        try:
            if url:
                # self.instance = vlc.Instance("--audio-visual=visual", "--effect-list=spectrometer",
                #                              "--effect-fft-window=flattop")
                # self.media_player = self.instance.media_player_new()

                if get_system_platform() == CommonEnum.WindowsPlatform:
                    self.media_player.set_hwnd(int(self.media_player_frame.winId()))
                elif get_system_platform() == CommonEnum.LinuxPlatform:
                    self.media_player.set_xwindow(int(self.media_player_frame.winId()))
                elif get_system_platform() == CommonEnum.DarwinPlatform:
                    self.media_player.set_nsobject(int(self.media_player_frame.winId()))
                else:
                    self.media_player.set_hwnd(int(self.media_player_frame.winId()))

                self.current_url = url
                self.current_url_type = url_type
                self.media_player.set_mrl(url)
                self.media_player.play()
                while True:
                    if self.vlc_get_state() == vlc.State.Playing:
                        self.media_player_frame.show()
                        PlayerState.MrlType = url_type
                        PlayerState.Load = PlayerEnum.LoadPlaying
                        # self.vlc_set_size(True)
                        return True
            else:
                pass
        except Exception as e:
            print(f'[real-live-desktop]  play_url exception {e}')
            return False

    def vlc_pause(self):
        """ 暂停

        :return:
        """
        self.media_player.pause()
        PlayerState.Load = PlayerEnum.LoadPaused

    def vlc_resume(self):
        """ 恢复

        :return:
        """
        self.media_player.set_pause(0)
        PlayerState.Load = PlayerEnum.LoadPlaying

    def vlc_stop(self):
        """ 停止

        :return:
        """
        self.media_player_frame.hide()
        self.media_player.stop()
        PlayerState.Load = PlayerEnum.LoadStopped

        self.vlc_set_size(False)

    def vlc_get_time(self):
        """ 已播放时间，返回毫秒值

        :return:
        """
        return self.media_player.get_time()

    def vlc_get_length_or_all_time(self):
        """ 音视频总长度，返回毫秒值

        :return:
        """
        return self.media_player.get_length()

    def vlc_set_time(self, ms):
        """ 拖动指定的毫秒值处播放。成功返回0，失败返回-1 (需要注意，只有当前多媒体格式或流媒体协议支持才会生效)

        :param ms:
        :return:
        """
        _time = self.vlc_get_time() + ms
        _all_time = self.vlc_get_length_or_all_time()
        if _time <= 0:
            return self.media_player.set_time(0)
        elif _time >= _all_time:
            return self.media_player.set_time(_all_time)
        else:
            return self.media_player.set_time(_time)

    def vlc_get_volume(self):
        """ 获取当前音量（0~100）

        :return:
        """
        return self.media_player.audio_get_volume()

    def vlc_set_volume(self, volume):
        """ 设置当前音量

        :param volume:
        :return:
        """
        _volume = self.vlc_get_volume() + volume
        if _volume <= 0:
            PlayerState.Volume = PlayerEnum.VolumeMuted
            return self.media_player.audio_set_volume(0)
        elif _volume >= 100:
            PlayerState.Volume = PlayerEnum.VolumeUnmuted
            self.media_player.audio_set_volume(100)
        else:
            PlayerState.Volume = PlayerEnum.VolumeUnmuted
            self.media_player.audio_set_volume(_volume)

    def vlc_set_size(self, b_fullscreen: bool):
        """ 设置窗口大小

        :return:
        """
        if b_fullscreen:
            self.showFullScreen_signal.emit()
            # self.showFullScreen()
            self.media_player.set_fullscreen(True)
            PlayerState.Size = PlayerEnum.SizeMax
        else:
            self.showNormal_signal.emit()
            # self.showNormal()
            self.media_player.set_fullscreen(False)
            PlayerState.Size = PlayerEnum.SizeInitial

    def vlc_get_state(self):
        """ 返回当前状态

        :return:
        """
        # 0: 'NothingSpecial', 处于空闲状态，等待发出命令
        # 1: 'Opening', 正在打开媒体资源定位器（MRL）
        # 2: 'Buffering', 正在缓冲
        # 3: 'Playing', 正在播放媒体
        # 4: 'Paused', 处于暂停状态
        # 5: 'Stopped', 处于停止状态，此时关闭播放器
        # 6: 'Ended', 已到达当前播放列表的末尾
        # 7: 'Error', 遇到错误，无法继续
        return self.media_player.get_state()

    def vlc_set_position(self, float_val):
        """ 拖动当前进度，传入0.0~1.0之间的浮点数(需要注意，只有当前多媒体格式或流媒体协议支持才会生效)

        :param float_val:
        :return:
        """
        return self.media_player.set_position(float_val)

    def vlc_get_rate(self):
        """ 获取当前文件播放速率

        :return:
        """
        return self.media_player.get_rate()

    def vlc_set_rate(self, rate):
        """ 设置播放速率（如：1.2，表示加速1.2倍播放）

        :param rate:
        :return:
        """
        return self.media_player.set_rate(rate)

    def vlc_set_ratio(self, ratio):
        """ 设置宽高比率（如"16:9","4:3"）

        :param ratio:
        :return:
        """
        # 必须设置为0，否则无法修改屏幕宽高
        self.media_player.video_set_scale(0)
        self.media_player.video_set_aspect_ratio(ratio)

    def vlc_add_callback(self, event_type, callback):
        """ 注册监听器

        :param event_type: VLC的监听器类型
        :param callback:
        :return:
        """
        self.media_player.event_manager().event_attach(event_type, callback)

    def vlc_remove_callback(self, event_type, callback):
        """ 移除监听器

        :param event_type:
        :param callback:
        :return:
        """
        self.media_player.event_manager().event_detach(event_type, callback)

    def vlc_set_marquee(self):
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

    def vlc_update_marquee(self, content="%Y-%m-%d %H:%M:%S"):
        """ 设置字幕内容

        :param content: 默认为时间格式，会在屏幕下方显示当前时间，且每一秒刷新一次。
        :return:
        """
        self.media_player.video_set_marquee_string(vlc.VideoMarqueeOption.Text, content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # vlc_widget = VlcPlayerWidget()
    vlc_widget = VlcPlayerWidget()
    vlc_widget.show()
    vlc_widget.vlc_play("http://tx2play1.douyucdn.cn/live/288016rlols5.flv?uuid=", PlayerEnum.MrlTypeLive)
    # vlc_widget.vlc_play("http://live.xmcdn.com/live/45/64.m3u8", PlayerEnum.MrlTypeRS)
    sys.exit(app.exec_())
