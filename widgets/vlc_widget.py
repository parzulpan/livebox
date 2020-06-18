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

from PyQt5.QtWidgets import QWidget, QApplication

# 设置VLC库路径，需在import vlc之前
os.environ['PYTHON_VLC_MODULE_PATH'] = "./bin/vlc_3.0.9.2"
# os.environ['PYTHON_VLC_LIB_PATH'] = "./bin/vlc_3.0.9.2/libvlc.dll"
import vlc


class VLCWidget(QWidget):
    """

    """

    def __init__(self, *args):
        super(VLCWidget, self).__init__()

        self.media_player = None
        self.instance = None
        self.get_player(args)
        self._init_ui()

    def _init_ui(self):
        """

        :return:
        """
        pass

    def get_player(self, *args):
        """

        :param args:
        :return:
        """
        if args:
            self.instance = vlc.Instance(*args)
            self.media_player = self.instance.media_player_new()
        else:
            self.media_player = vlc.MediaPlayer()

        if platform.system() == "Windows":
            self.media_player.set_hwnd(self.winId())
        else:
            self.media_player.set_xwindow(self.winId())

    def release_player(self):
        """ 释放资源

        :return:
        """
        return self.media_player.release_player()

    def play_url(self, url=None):
        """

        :param url:
        :return:
        """
        try:
            print("url {0}".format(url))
            # url = "http://tx2play1.douyucdn.cn/live/288016rlols5.flv?uuid="
            if url:
                self.media_player.set_mrl(url)
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
        self.media_player.stop()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vlc_widget = VLCWidget()
    vlc_widget.show()
    vlc_widget.play_url()
    sys.exit(app.exec_())
