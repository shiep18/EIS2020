1. python执行Gui_Check。
2. 其中用到了mc，根据自身情况更改相应代码。mc = mx.initMinecraft("47.100.46.95", 4785)
可以更改为自己使用的服务器，如果本地运行可删去括号中的内容。
其中也有关于mc的判断，可以自己更改。
3. Gui_Check代码中有部分注释。
4. 运行代码不报错但需要下载的库：pip install echarts-countries-pypkg
5. 可能会用到的库：我压缩了一个叫site-packages的压缩包，里面有些库是pip不到但需要用到的，
其他库也可以直接复制到python中的site-packages中。本人环境使用的是python3.7.7，可能会出
现库不能使用的情况。
6. 更改对应的数据库配置。因为表中有个人隐私，就不给sql了，新建数据库external_personnel，
在其中新建数据表external_personnel，新建：日期,时间,姓名,电话,体温,目的 6项内容。
再新建数据库 internal_personnel，在其中新建数据表 internal_personnel，新建：
日期,时间,姓名,体温 4项内容。在同一个数据库下，新建information_upload，新建：
姓名,学院,专业,班级,学号,性别,电话,年龄,政治面貌,出生年月日 10项内容。
7. 人脸识别模块是事先训练好的，可以识别已经识别好的人脸，可以识别的人脸具有隐私就不上传
了，大家可以自己训练对应的yml文件并更改。trainer中的yml太大了传不上来，大家自己训练
yml吧~
8. 未完待续。2020/7/8 14:24