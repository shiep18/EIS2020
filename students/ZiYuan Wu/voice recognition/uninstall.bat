@echo off
set "thispath=%~dp0"

xcopy C:\cmdplayer_hj %thispath%cmdplayer_hj  /e /i /y
xcopy C:\GnuWin32 %thispath%GnuWin32  /e /i /y

rmdir /s/q C:\cmdplayer_hj
rmdir /s/q C:\GnuWin32

pip3 uninstall pyaudio -y
pip3 uninstall baidu-aip -y
pip3 uninstall xpinyin -y
pip3 uninstall paho-mqtt -y

echo 卸载成功，3秒后关闭
TIMEOUT /T 3
