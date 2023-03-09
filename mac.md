# mac

## 软件

### 常用

- [Snipaste 截图软件](https://www.snipaste.com/)
- [Logitech Options 罗技客户端](https://www.logitech.com.cn/zh-cn/software/options.html)
- [Homebrew 安装软件](https://brew.sh)
- [alfred 搜索和集成](https://www.alfredapp.com/)
- [numi 计算器](https://github.com/nikolaeu/numi/wiki)
- [QBlocker 防止误触退出](https://github.com/steve228uk/QBlocker)
- [Microsoft Remote Desktop Beta 远程连接Windows](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/all-users-of-microsoft-remote-desktop-for-mac)
- [app-cleaner 清理软件](https://nektony.com/mac-app-cleaner)
- [draw.io 画图软件](https://app.diagrams.net/)

### 开发

- [mac的系统服务管理](https://www.launchd.info/)
- [iterm2 终端](https://iterm2.com/)
- [AppleScript文档 可以操作app的脚本语言](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [idea toolbox](https://www.jetbrains.com/toolbox-app/)
- [oh my zsh zsh的工具](https://ohmyz.sh/)

#### ohmyzsh 插件

[插件集合](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)

- extract 解压缩 `x a.zip`
- z 跳转目录 `z code`
- [zsh-syntax-highlighting 语法高亮](https://github.com/zsh-users/zsh-syntax-highlighting)
- [zsh-autosuggestions 自动补全](https://github.com/zsh-users/zsh-autosuggestions)
- vscode `vsc a.java` `vsc code`

#### ohmyzsh 主题

- [p10k](https://github.com/romkatv/powerlevel10k)

## 操作

### Finder and Terminal

- terminal 打开 finder

```shell
# 打开当前目录
open .
# 打开特定目录
open /tmp
# 打开app
open -a WeChat
# 打开app和参数
open -a LibreOffice 日常函件浏览器指标10.10\(1\).xlsx
```

- finder 打开 terminal 使用 AppleScript

```osascript
tell application "Finder"
	set dir_path to quoted form of (POSIX path of (folder of the front window as alias))
end tell
CD_to(dir_path)
on CD_to(theDir)
	tell application "iTerm"
		activate
		set win to (create window with default profile)
		set sesh to (current session of win)
		tell sesh to write text "cd " & theDir & ";clear"
	end tell
end CD_to
```

## launchd

- [文档](https://www.launchd.info/)

### 编写xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.liubin.app</string>
        <key>Program</key>
        <string>/Users/liubin/app-mac/app</string>
        <key>StandardOutPath</key>
        <string>/tmp/app.stdout</string>
        <key>StandardErrorPath</key>
        <string>/tmp/app.stderr</string>
        <!--     <key>KeepAlive</key>
            <true/> -->
    </dict>
</plist>
```

### load服务

```shell
launchctl load ~/Library/LaunchAgents/com.liubin.app.plist
launchctl unload ~/Library/LaunchAgents/com.example.app.plist
```

### 启动服务

```shell
launchctl start com.example.app
launchctl stop com.example.app
```

## homebrew

