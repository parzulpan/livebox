#!/usr/bin/env bash

echo "Log: real_live app start..."

# 运行发布的应用
sysOS=$(uname -s)
if [ "$sysOS" == "Darwin" ];then
	./real_live
elif [ "$sysOS" == "Linux" ];then
	./real_live
elif [ "$sysOS" == "Windows" ];then
	./real_live.exe
else
	echo "Error: Other OS $sysOS"
fi

echo "Log: real_live app end..."