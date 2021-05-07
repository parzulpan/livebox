#!/usr/bin/env bash

# 请修改为自己的环境
# 請修改為自己的環境
# Please modify it to your own environment
pyinstaller_path="C:\parzulpan\App\Python3.6.8\Scripts\pyinstaller.exe"

rm -rf build dist
rm -rf release
mkdir release

sysOS=$(uname -s)
if [ "$sysOS" == "Darwin" ];then
  echo "System is MacOS"
	$pyinstaller_path --windowed --clean --noconfirm real_live_macos.spec
	mv -f dist/RealLive.app release
	echo "realease successful！"
elif [ "$sysOS" == "Linux" ];then
	echo "System is Linux"
	$pyinstaller_path real_live_linux.spec --clean -y
	mv -f dist/RealLive release
	echo "realease successful！"
elif [ "$sysOS" == "Windows" ];then
	echo "System is Windows"
	$pyinstaller_path real_live_windows.spec --clean -y
	mv -f dist/RealLive release
	echo "realease successful！"
else
  echo "System is Windows"
	$pyinstaller_path real_live_windows.spec --clean -y
#	mv -f dist/RealLive release
	echo "realease successful！"
#	echo "realease error: Other OS $sysOS"
fi

#rm -rf build dist