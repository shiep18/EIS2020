
## 人员分工
吴子渊：人脸识别+数据库+homeassitant

郭长灏：人机界面+人脸识别+PPT

易耿浩：语音识别+MQTT通信+PPT

## 代码介绍
Mainwindow.py为主文件，运行即可显示界面

My_Speech_end.py文件，用于实现程序执行过程中的语音调用和建立与数据库之间的信息连接

pub_first.py文件，通过串口对homeassistant里面的数据进行初始化

face.rec.py文件，用于程序执行期间的借还球时的人脸录入与人脸识别

MXMqtt.py文件，用于实现mqtt的远端数据通信

## 说明
1、face.rec.py中需修改相应百度人脸识别API（若没有的，需要在https://ai.baidu.com/中申请）

2、MXMqtt.py可更改自己的通道，对应Mainwindow.py中对应发布（借球和还球）

3、My_Speech_end.py语音识别部分，需要更改相应API（若没有的，需要在https://ai.baidu.com/中申请）
