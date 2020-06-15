# 项目成员

黎祖林，田浩冬，周宇涛

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
