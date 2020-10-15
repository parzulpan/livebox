<h1 align="center">RealLive</h1>

简体中文  |  [繁体中文](README-th_CN.md)  |  [English](README-en.md)

> 一个跨平台的网络媒体聚合应用，支持直播视频，高清电视和广播电台的在线观看或收听。

**桌面端：**

[使用视频](./assets/desktop/Use.mp4)

![Main](./assets/desktop/Main.png)

|  | | |
| --- | --- | --- |
| ![Features](./assets/desktop/Features.gif) | ![Setup](./assets/desktop/Setup.gif) |  ![Live](./assets/desktop/Live.gif) |
| ![TV](./assets/desktop/TV.gif) | ![RS](./assets/desktop/RS.gif) | ![LOL](./assets/desktop/LOL.gif) |

## 为什么是它

**它解决了什么？**

* 怀念电视和电台吗？它就能满足你的要求；
* 多种资源设备携带？它让你随时随地观看和收听；
* 多个平台往返切换？它即能支持多个平台和频道。

**它有什么特性？**

* 多端支持，包括 Linux、MacOS、Windows 等桌面端，Android、iOS 等移动端，Web 端，后端等；
* 多平台和频道支持，只要能得到流媒体的数据均可以观看或收听，不断拓展更新中；
* 支持查看热门直播、数据备份和恢复、笔记功能和各种偏好设置；

**它未来会如何？**

* 打通各端数据，支持数据缓存和搜索引擎；
* 持续更新各种平台或平台；
* 支持机器翻译和智能字幕；
* 更多功能和特性等待发掘。

## 快速开始

### 下载使用

**桌面端：**

...

### 调试开发

**分支说明：**

* **master** 为保留分支
* **stable** 为 Release 发布分支
* **dev** 为一直开发的分支，欢迎大家 Fork 该分支

**桌面端调试运行：**

1. 配置好 Python 开发环境，推荐 Python3.6、Python3.7，其他版本未测试。

2. 首次使用时，Fork 后 Clone 该项目，进入 src/real-live-desktop 桌面端项目文件夹，配置 [FirstDebug.sh](./src/real-live-desktop/FirstDebug.sh)后，然后运行 `FirstDebug.sh`。

    ```shell
    git clone -b dev https://github.com/parzulpan/real-live.git
    ./FirstDebug.sh
    ```

3. 非首次使用时，即配置好环境后，直接运行 real-live.py 即可。

   ```shell
   python real-live.py
   ```

**桌面端打包发布：**

1. 确保项目能运行成功后，进入 _build文件夹 配置 [ReleaseBuild.sh](./src/real-live-desktop/_build/ReleaseBuild.sh)后，然后运行 `ReleaseBuild.sh`。

    ```shell
    ./ReleaseBuild.sh
    ```

[详细可查看项目网站](https://real-live.parzulpan.cn)

## 加入项目

该项目目前桌面端基本已经完成，后端正在开发，移动端和 Web 待开发。这个项目将长期开发维护，欢迎大家参与进来，做些贡献，或者提点建议。

**项目规划：**

|  |  |
| --- | --- |
|  ![项目规划1](./assets/desktop/项目规划1.png) | ![项目规划2](./assets/desktop/项目规划2.png) |
| ![项目规划3](./assets/desktop/项目规划3.png) | ![项目规划4](./assets/desktop/项目规划4.png) |

**你的收获：**

* 正如项目规划所示，你将体验到真实的团队协作方式和项目开发流程；
* 增强自己的硬实力，学习更多的技术，不管是前端还是后端，甚至是测试；
* 增强自己的软实力，开源精神、协调沟通能力、项目推动能力、执行力等都将得到提升。

**反馈渠道：**

持续更新中，有任何疑问和建议，欢迎加入 QQ 群 [RealLive项目讨论群：893364757](./assets/img/QQ群.jpg) 讨论，或者提 [issue](https://github.com/parzulpan/real-live/issues) 。

## 开源协议

本项目遵循 [GNU General Public License v3.0](./LICENSE)，如果要修改源码进行二次开发需要遵守以下协议：

1. 如果要在网络上分发，那么必须开源；
2. 不能以盈利为目的，不能插入任何形式的广告；
3. 注明原项目出处；
4. 继承相同协议。

## 免责声明

该项目仅能用于计算机技术的学习交流和在法律允许范围内的使用，任何个人或集体不得使用该项目进行任何违反相关法律法规的活动。任何尝试下载或下载该项目任意分支或发行版的，即代表您同意本项目作者及贡献者不承担任何由于您违反以上准则所带来的任何法律责任。
