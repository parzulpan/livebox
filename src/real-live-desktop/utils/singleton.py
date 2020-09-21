# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 线程安全的单例模式，多种版本

@Attention :
"""

from threading import Lock


# 函数装饰器版本
def SingletonFunctionVersion(cls):

    _instance = {}
    _lock: Lock = Lock()

    def inner():
        with _lock:
            if cls not in _instance:
                _instance[cls] = cls()
        return _instance[cls]
    return inner


# 类装饰器版本
class SingletonClassVersion(object):

    _lock: Lock = Lock()

    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        with self._lock:
            if self._cls not in self._instance:
                self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


# new 关键字版本
class SingleNewVersion(object):

    _instance = None
    _lock: Lock = Lock()

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        pass


# metaclass 版本
class SingletonMateClassVersion(type):

    _instance = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kw):
        with cls._lock:
            if cls not in cls._instance:
                instance = super().__call__(*args, **kw)
                cls._instance[cls] = instance
        return cls._instance[cls]