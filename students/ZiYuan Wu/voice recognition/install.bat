@echo off
set "thispath=C:\cmdplayer_hj\madplay-0.15.2b;C:\GnuWin32\bin"
set mypath=%path%
echo %mypath% > temp.txt

find "%thispath%" temp.txt
if %errorlevel% == 0 (
	echo 程序返回码:%errorlevel%
) else (
	echo 程序返回码:%errorlevel%
	setx /m "path" "%thispath%;%path%"
)	

del temp.txt

xcopy cmdplayer_hj C:\cmdplayer_hj /e /i /y
xcopy GnuWin32 C:\GnuWin32 /e /i /y
rmdir /s/q cmdplayer_hj
rmdir /s/q GnuWin32

pip3 install Lib\PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
pip3 install pyaudio
pip3 install baidu-aip
pip3 install xpinyin
pip3 install paho-mqtt


echo 安装成功，3秒后关闭
TIMEOUT /T 3

