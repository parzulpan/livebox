echo "desktop app install start"

# 配置项目开发环境
pip install -r requirements.txt

# 复制/移动所需插件
sysOS=$(uname -s)
if [ "$sysOS" == "Darwin" ];then
	echo "I'm MacOS"
    # echo  "$(ls ../../plugins/vlc_3.0.9.2_macos_64)"
	cp -r ../../plugins/vlc_3.0.9.2_macos_64 resources/vlc
elif [ "$sysOS" == "Linux" ];then
	echo "I'm Linux"
    # echo  "$(ls ../../plugins/vlc_3.0.9.2_linux_64)"
	cp -r ../../plugins/vlc_3.0.9.2_linux_64 resources/vlc
elif [ "$sysOS" == "Windows" ];then
	echo "I'm Windows"
    # echo  "$(ls ../../plugins/vlc_3.0.9.2_windows_64)"
	cp -r ../../plugins/vlc_3.0.9.2_windows_64 resources/lvc
else
	echo "Error: Other OS $sysOS"
fi

echo "$(ls resources/vlc)"

echo "desktop app install end"