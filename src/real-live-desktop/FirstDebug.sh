#!/usr/bin/env bash

# 首次调试开发脚本，进行项目配置
# 首次調試開發腳本，進行項目配置
# Debug the development script for the first time and configure the project

# 请修改为自己的环境
# 請修改為自己的環境
# Please modify it to your own environment
project_interpreter="/Users/parzulpan/Personal/PythonVenv/3.6/bin/python3.6"
pip_path="/Users/parzulpan/Personal/PythonVenv/3.6/bin/pip"

$pip_path install -r requirements.txt

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

$project_interpreter real_live.py