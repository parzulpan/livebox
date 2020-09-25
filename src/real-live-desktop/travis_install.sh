# 配置项目开发环境
pip install -r requirements.txt

# 复制/移动所需插件
sysOS=$(uname -s)
if [ "$sysOS" == "Darwin" ];then
	echo "I'm MacOS"
	cp -r ../../plugins/vlc_3.0.9.2_macos_64 resources/vlc
#	echo  "$(ls ../../plugins/vlc_3.0.9.2_macos_64)"
elif [ "$sysOS" == "Linux" ];then
	echo "I'm Linux"
	cp -r ../../plugins/vlc_3.0.9.2_linux_64 resources/vlc
#	echo  "$(ls ../../plugins/vlc_3.0.9.2_linux_64)"
elif [ "$sysOS" == "Windows" ];then
	echo "I'm Windows"
	cp -r ../../plugins/vlc_3.0.9.2_windows_64 resources/lvc
#	echo  "$(ls ../../plugins/vlc_3.0.9.2_windows_64)"
else
	echo "Error: Other OS $sysOS"
fi