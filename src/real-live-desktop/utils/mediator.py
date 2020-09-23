# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 客户端的中介者，使用中介者模式，解耦组件

@Attention :
"""

from __future__ import annotations
from abc import ABC


class Mediator(ABC):

    def __init__(self, _widgets: dict) -> None:
        self.widgets = _widgets










