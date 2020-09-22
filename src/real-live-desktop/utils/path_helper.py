# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 路径帮助工具

@Attention :
"""
import os


class PathHelper:

    @staticmethod
    def get_root_path():
        cur_file_dir_path = os.path.dirname(os.path.abspath(__file__))
        root_path = os.path.abspath(cur_file_dir_path + os.path.sep + '..')
        return root_path

    @staticmethod
    def get_python_vlc_module_path(sys_type):
        sys_type_dict = {"Windows": "vlc_3.0.9.2_windows_64", "Linux": "vlc_3.0.9.2_linux_64",
                         "Darwin": "vlc_3.0.9.2_macos_64"}
        _path = os.path.abspath(
            PathHelper.get_root_path() + os.path.sep + "resources" + os.path.sep + sys_type_dict[sys_type])
        return _path

    @staticmethod
    def get_img_path(img_name):
        _path = os.path.abspath(
            PathHelper.get_root_path() + os.path.sep + "resources" + os.path.sep + "img" + os.path.sep + img_name)
        return _path

    @staticmethod
    def get_qss_path(qss_name):
        _path = os.path.abspath(
            PathHelper.get_root_path() + os.path.sep + "resources" + os.path.sep + "qss" + os.path.sep + qss_name)
        return _path

    @staticmethod
    def get_config_path(file_name="config.ini"):
        _path = os.path.abspath(
            PathHelper.get_root_path() + os.path.sep + "resources" + os.path.sep + file_name)
        return _path

    @staticmethod
    def get_json_path(file_name="config.json"):
        _path = os.path.abspath(
            PathHelper.get_root_path() + os.path.sep + "resources" + os.path.sep + "json" + os.path.sep + file_name)
        return _path


if __name__ == '__main__':
    print(PathHelper.get_root_path())
    print(PathHelper.get_python_vlc_module_path())
    print(PathHelper.get_img_path('about@64x64.png'))
    print(PathHelper.get_qss_path('blue.qss'))
    print(PathHelper.get_config_path())
