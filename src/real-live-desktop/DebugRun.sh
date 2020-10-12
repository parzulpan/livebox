#!/usr/bin/env bash

# # 设置解释器路径，需要根据自己的环境来更改
project_interpreter="/home/parzulpan/App/venv_py373/bin/python3.7"
pip_path="/home/parzulpan/App/venv_py373/bin/pip"

# 配置项目开发环境
# $pip_path list
$pip_path install -r requirements.txt

# 复制/移动所需插件
sysOS=$(uname -s)
if [ "$sysOS" == "Darwin" ];then
	echo "I'm MacOS"
#	cp -r ../../plugins/vlc_3.0.9.2_macos_64 resources/vlc
#	echo  "$(ls ../../plugins/vlc_3.0.9.2_macos_64)"
elif [ "$sysOS" == "Linux" ];then
	echo "I'm Linux"
#	cp -r ../../plugins/vlc_3.0.9.2_linux_64 resources/vlc
#	echo  "$(ls ../../plugins/vlc_3.0.9.2_linux_64)"
elif [ "$sysOS" == "Windows" ];then
	echo "I'm Windows"
#	cp -r ../../plugins/vlc_3.0.9.2_windows_64 resources/vlc
#	echo  "$(ls ../../plugins/vlc_3.0.9.2_windows_64)"
else
	echo "Error: Other OS $sysOS"
fi

# 运行桌面端应用主程序
$project_interpreter real_live.py