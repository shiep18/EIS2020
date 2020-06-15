此系统基于mysql数据库，运行前需安装WampServer  
library.sql需在phpadmin内导入  
解压Library.rar后运行lib2.py即可  
运行时提示缺少模块自行pip install即可  
语音识别调用百度api，如需较多次调用，请自己注册应用修改ID,KEY,SCRECTKEY
其中，baidusound内的playsound.py需要修改。在41行后。添加winCommand('close', alias)  
即：  
if block:  
     sleep(float(durationInMS) / 1000.0)  
     winCommand('close', alias)  
  
