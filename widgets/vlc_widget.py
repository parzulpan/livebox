# -*- coding: utf-8 -*-
# @Date       : 6/15/2020 
# @Author     : parzulpan
# @Email      : parzulpan@gmail.com
# @Description: 请输入此文件的功能描述
# @Attention  : 

import sys
import vlc
import platform

from PyQt5.QtWidgets import QWidget, QApplication


class VLCWidget(QWidget):
    """

    """
    def __init__(self):
        super(VLCWidget, self).__init__()

        self.media_player = vlc.MediaPlayer()

        if platform.system() == "Windows":
            self.media_player.set_hwnd(self.winId())
        else:
            self.media_player.set_xwindow(self.winId())

        self._init_ui()

    def _init_ui(self):
        """

        :return:
        """
        pass

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
                self.media_player.play()
            else:
                pass
        except Exception as e:
            print('Exception {0}'.format(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vlc_widget = VLCWidget()
    vlc_widget.show()
    vlc_widget.play_url()
    sys.exit(app.exec_())

