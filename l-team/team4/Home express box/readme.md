# 项目成员及项目分工

黎祖林： APP制作，APP与Python的网络通信

田浩冬： 二维码扫描功能，vtk应用和Home Assistant的连接

周宇涛： APP布局设计、快递箱模型制作、PPT制作、主讲人

# Home express box

1.model.123d快递箱模型，由此模型导出box.stl以及door.stl两个文件。

2.二维码_makedemo.py为二维码生成程序，本次模拟使用的二维码为该程序生成。

3.二维码_recognition.py使用摄像头进行二维码扫描。

3.box.py VTK控制模型程序

4.chuankou.py 模拟手动关门，此次项目使用串口进行模拟。

5.Web_ha.py局域网络连接APP的程序。

注：hello.png为错误二维码，相当于不属于该用户的快递；verify.png以及verify_new.png均为该用户所购买的快递件上的二维码。

# Homeassistion config

1.hachina6_package.py为homeassistion中位于custom_components内的配置文件。

注意：需要在该文件夹下创建package_send.txt，open.txt，check.txt三个空白文件以便python文件的读取及写入。

# 代码运行须知

1.将Homeassistion config中的文件复制到自己电脑中的custom_components文件夹中，并在该文件夹下创建package_send.txt，open.txt，check.txt三个空白文件。注意在configuration.yaml文件中添加(hachina6_package:)。添加脚本载入hachina6_package，添加实体显示hachina6_package。

2.下载APP到自己的手机中。用户名：20171600 密码：20171600

3.运行box.py，Web_ha.py，二维码_recognition.py以及chuankou.py四个python程序。二维码_recognition.py用来扫描二维码，Web_ha.py运行后用来连接手机APP，box.py为快递箱模型。

4.步骤：扫描二维码，箱门打开，使用串口关闭箱门，Homeassistion内部显示改变，用户使用脚本开箱门，同时使用串口关闭箱门。APP输入密码后查询若快递箱内有快递显示数量为1，若没有显示为无。
