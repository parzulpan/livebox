
import os


class PathHelper:

    @staticmethod
    def get_root_path():
        cur_file_dir_path = os.path.dirname(os.path.abspath(__file__))
        root_path = os.path.abspath(cur_file_dir_path + os.path.sep + '..')
        return root_path

    @staticmethod
    def get_python_vlc_module_path():
        _path = os.path.abspath(
            PathHelper.get_root_path() + os.path.sep + "core" + os.path.sep + "vlc_3.0.9.2")
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
    def get_config_path():
        _path = os.path.abspath(
            PathHelper.get_root_path() + os.path.sep + "resources" + os.path.sep + "config.ini")
        return _path


if __name__ == '__main__':
    print(PathHelper.get_root_path())
    print(PathHelper.get_python_vlc_module_path())
    print(PathHelper.get_img_path('about@64x64.png'))
    print(PathHelper.get_qss_path('blue.qss'))
    print(PathHelper.get_config_path())
