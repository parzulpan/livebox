# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 客户端的中介者，使用中介者模式，解耦组件

@Attention :
"""

from __future__ import annotations
from abc import ABC

from widgets.about_widget import AboutWidget
from widgets.buffer_widget import BufferWidget
from widgets.gif_widget import GifWidget
from widgets.live_widget import LiveWidget
from widgets.main_widget import MainWindow
from widgets.preferences_widget import PreferencesWidget
from widgets.radio_station_widget import RadioStationWidget
from widgets.real_player_widget import RealPlayerWidget
from widgets.screenrecord_widget import ScreenRecordWidget
from widgets.screenshot_widget import ScreenShotWidget
from widgets.search_widget import SearchWidget
from widgets.tv_widget import TvWidget
from widgets.vlc_player_widget import VlcPlayerWidget


class Mediator(ABC):

    def __init__(self, _widgets: dict) -> None:
        self.widgets = _widgets


_widgets = {}


about_widget = AboutWidget()
buffer_widget = BufferWidget()
gif_widget = GifWidget()
live_widget = LiveWidget()
main_window = MainWindow()
preferences_widget = PreferencesWidget()
radio_station_widget = RadioStationWidget()
real_player_widget = RealPlayerWidget()
screenrecord_widget = ScreenRecordWidget()
screenshot_widget = ScreenShotWidget()
search_widget = SearchWidget()
tv_widget = TvWidget()
vlc_player_widget = VlcPlayerWidget()


_widgets["about_widget": about_widget, "buffer_widget": buffer_widget]


mediator = Mediator(_widgets)





