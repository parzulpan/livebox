# real-live 网络直播观看平台

## 简介
real-live是一个网络直播观看平台，它支持当前几十种主流的直播平台，通过选择直播平台和输入查询信息即可获取直播平台的直播源，可以选择在本平台上在线观看，或者将直播源复制到PotPlayer、VLC等播放器中观看。

## 特色
* [x] 支持多种主流直播平台
* [x] 无需登录，高清晰度低延迟
* [x] 简洁易用，勿扰模式看直播涨姿势
* [x] 支持直播房间号和主播名搜索(支持模糊搜索)
* [ ] 多窗口模式
* [ ] 多语言和换肤功能
* [ ] 历史查询记录和偏好设置(关注)
* [ ] 智能字幕匹配

## 使用
### Debug
**技术选型：**

Cpp、Python、Qt、PyQt5、NLP

**开发环境：**

Pycharm 2020、Python 3、PyQt 5.12

**编译调试：**

配置好Python开发环境后，点击[requirements.txt](./requirements.txt)文件安装依赖包，然后运行[real_live.py](./real_live.py)即可。

**打包安装：**

推荐使用Pyinstaller打包，NSIS制作安装包。


### Release
直接下载最新的 [release](https://github.com/parzulpan/real-live/releases) 安装包安装使用即可。

## 反馈
有任何疑问和建议<br/>
欢迎提 [issue](https://github.com/parzulpan/real-live/issues) <br>
或者加入Telegram群组 [RealLive讨论群](https://t.me/GitHubRealLive)

## 致谢
参考和借鉴以下开源项目和资源：
* [wbt5/real-url](https://github.com/wbt5/real-url)  ( 提供多种直播平台的真实流媒体地址/直播源接口 )
* [iconfont](https://www.iconfont.cn) ( 项目的资源文件均来自该网站 )

感谢以上开源项目和资源！

## 许可
[GPL-3.0](./LICENSE)

本项目遵循GNU General Public License v3.0，如果要修改源码进行二次开发需要遵守以下协议：
1. 如果要在网络上分发，那么必须开源
2. 不能以盈利为目的，不能插入任何形式的广告
3. 注明原项目出处
4. 继承相同协议