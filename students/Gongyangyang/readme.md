# EIS2020
Embedded and Intelligent Systems (EIS) course for SHIEP 2020

# 20200323作业([myhouse](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/myhouse))
1. 学习M02 M06 ppt
2. students目录下创建自己的文件夹
3. 我的世界造房子myhouse.py上传
## 结果图
![myhouse](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/myhouse/myhouse.png)

# 20200325作业([mylogo](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/mylogo))
1. 学习3D建模课件，挑3个ppt学习即可。 3个设计文件上传到自己的文件夹。 可以用123D也可以用fusion360
2. 设计创意一个属于自己的物品。 mylogo.stl 文件上传。
3. 在我的世界里显示自己的物品 mylogo.py 和binvox文件上传。
## 结果图
![mylogo](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/mylogo/mylogo.png)

# 20200327作业([myclan](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/myclan))
1. 安装并配置git和vscode, 参见知乎的帖子如何配置vscode和git
2. 在我的世界里利用opencv，利用不同方块和颜色显示一幅线条卡通线条图mypic.jpg , 大小为32x32个方块，程序名为showmypic.py
3. 写一个myclan.py,import 调用mylogo和showmypic里面的函数，完成一次性显示一个logo和卡通图
4. 上传最后效果的屏幕拷贝
## 结果图
![myclan](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/myclan/myclan.png)
### 分析：  
          * 把图片以灰度读入后，进行二值化处理，根据两种值分别分配不同颜色的方块，读取矩阵搭建后形成黑白图像。
          * 在myclan里调用两种函数，可对位置进行设定

# 20200330作业([mydog](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/mydog))
1. 跑通倍塔狗语音识别代码
2. 能够用前进，后退，往左，往右指挥我的世界中的角色前后左右移动
3. 在我的世界中竖一个石柱，上海气温20度则高度为20块
4. 效果屏幕拷贝上传自己的目录
## 结果图
![mydog](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/mydog/mydog.png)
gif:
![mydoggif](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/mydog/mydog.gif)

### 分析：
          * 因为原本代码中的shenjian api返回的都是502，所以我换成了百度的自然语言处理api来提取出句子中的地名。
          * 移动则是用了pynput来实现键盘输入。
          
# 20200401作业([mycamera](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/mycamera))
1. 将造房子的代码改造为类名字为House 类里面需要有isInHouse()函数判断是否在房子里。
2. 利用House类生成27个实例，每个房子的位置在csv文件中定义，csv文件格式举例如下 housename,x,y,z,l,w,h
   xknbighouse1,100,10,100,10,10,6
   xknsmallhouse2,100,10,200,6,6,6
3. 摄像头监视有运动物体进入画面时唱歌
## 结果图
gif:
![mycamrea](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/mycamera/mycamera.gif)

### 分析：
          * 检测出当前所在的房子，并将相应信息打印到终端，如不在则显示not in。
          * 运动物体的检测是根据方框数来确定，当有物体进入背景时，方框数会增加，视为检测到运动物体，两个阈值需根据具体背景情况调整。
          * 没有在库里找到播歌相关的函数，所以在终端打印playsound来代替。
          * 使用多线程处理，让两个检测循环同时进行。
          * 从csv读入的房名为str格式，无法直接作为变量名使用，未能找到合适的方法来转变，最后还是用了字典来储存。
          
# 20200403作业([mycontroller](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/mycontroller))
1. 找一个物体作为指挥棒，通过视频和HSV颜色匹配画一个圆跟踪
2. 利用找到的物体作为遥控器，遥控我的世界的玩家前后左右跑动。
3. 跑到部落里不同的房子，显示“welcome to xxxx‘s house” xxx是房子的主人的名字
## 结果图
gif：
![mycontroller](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/mycontroller/mycontroller.gif)
### 分析：
          * 黄色控制视角，绿色控制移动。
          * 通过模拟鼠标键盘的方式来实现控制。
          * 操作不太灵敏，容易跑偏。
          
# 20200408作业([myled](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/myled))
1. 我的世界回到家后点亮arduino的一盏灯，走出家后arduino灯关闭
2. 阿里code团队里面写自己的名字
## 结果图
gif：
![myled](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/myled/myled.gif)

# 20200410作业([myface](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/myface))
1. 跑通人脸识别代码
2. 训练3个人脸，自己，家人，其他（比如猫).
3. 利用人脸检测获得脸部图像保存到文件face.jpg里面
4. 我的世界用玻璃做门。如果是自己，则门变成空气，可以进去。arduino点亮1~4号灯
5. 我的世界用玻璃做门。如果是家人，则门变成空气，可以进去。arduino点亮5~8号灯
6. 其他人不开门（可以用自己带口罩充当）
7. 离开屋子灯熄灭
8. 演示效果用动图gif上传
## 结果图
gif:
![myface](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/myface/myface.gif)
### 分析：
          * 识别为chenweiting 和 Morgan Freeman 时开门，识别为 Leonardo DiCaprio 时关门。
          * 离开房子一定距离时，所有LED灯熄灭。
          * 训练时需要收集清晰的图片，否则可能会截不出人脸，有效图片至少要10张左右，且为不同背景。
          * 训练所得数据可以保存在yml文件中。
          * 发送串口数据时最好有一定的时间间隔。
          
# 20200415作业([socket](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/socket))
1. 用socket接口编程在我的世界玩家脚下摆3x3的黄金块
2. mcpi协议参考https://github.com/brooksc/mcpipy/blob/master/mcpi/mcpi_protocol_spec.txt
3. 在A4纸大小厚2毫米的板子上设计一个arduino盒子，要求
   * 6个面，露出排针可供扩展
   * 露出USB口可插USB线
   * 一个竖杆插在arduino座上
   * 竖杆上留3个LED灯的位置作为红绿灯
## 结果图
![mysocket](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/socket/mysocket.png)
   
# 20200417作业([apache](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/apache))
1. 通过网页控制我的世界角色移动
2. 通过网页在我的世界里建房子
## 结果图
gif:
![apache](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/apache/apache.gif)
### 分析：
          * move输入移动方向和距离，输入b回家。
          * home输入与角色的相对距离，建造房子。
          
# 20200513作业([login](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/login) & [vote](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/vote) & [BBS](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/BBS))
1. 为登录界面APP的第二个界面添加一个返回点击事件：实现点击可返回登录界面
2. 完成课上投票应用剩余部分
3. 完善博客应用，应有最基础的查看与发表文章功能
4. 效果屏幕拷贝上传自己的目录
## 结果图
login:
![login](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/login/login.gif)
vote:
![vote](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/vote/vote.gif)
BBS:
![BBS](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/BBS/BBS.gif)

# 20200515作业([auto_test](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/auto_test))
1. 使用pyautogui完成截取全屏并保存（需要加入弹框进行判定）
2. 完成课上pyautogui打开网页搜索功能
3. 爬取豆瓣上selenium的相关书籍
4. 效果屏幕拷贝上传自己的目录
## 结果图
### screenshot:
![screenshot](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/auto_test/screenshot.gif)
### baidu_search:
![baidu_search](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/auto_test/chrome_baidu.gif)
### douban:
![douban](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/auto_test/douban.gif)

# 20200518作业([VTK](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/homeass%26VTK_v0518/vtk) & [homeassistant](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/homeass%26VTK_v0518/homeassistant))
1. 让棱锥和轮子同时显示，轮子绕圆心旋转
2. Homeassistant中添加家庭和杨校区位置图标（要求杨浦校区位置需要真是坐标） 
3. 在手机或者虚拟机里面安装IP摄像头，实现局域网实时查看视频 
4. 效果屏幕拷贝上传自己的目录
## 结果图
### wheel:
![wheel](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/homeass%26VTK_v0518/wheel.gif)
### homeassistant:
![homeassistant](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/homeass%26VTK_v0518/homeassistant.png)
### webcam:
![webcam](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/homeass%26VTK_v0518/webcam.png) 

# 20200520作业 ([VTK](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/VTK_v0520) & [video](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/video))
1. 利用串口程序，结合vtk，可以控制vtk物体的转动速度。
2. AS结合登录界面、音视频界面、计时器界面。通过按钮事件实现跳转。
3. 效果屏幕拷贝上传自己的目录
## 结果图
### wheel_speed:
![wheel](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/VTK_v0520/wheel_speed.gif)
### video:
![video](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/video/video.gif)

# 20200522作业([carsimple](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/carsimple_v0522) & [weather_report](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/homeassistant_v0522(weather_report)))
1. 安装照片上的车尺寸和形状重新设计车
2. Homeassistant完成调通第一个脚本和自动化
3. 结合语音，设计自动化，每天定时播放天气预报
4. 效果屏幕拷贝上传自己的目录
## 结果图
### carsimple:
![carsimple](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/carsimple_v0522/carsimple.png)
### weather_report:
![weather_report](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/homeassistant_v0522(weather_report)/weather_report.gif)

# 20200525作业([car_animate](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/car_animate) & [hachina](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/hachina))
1. 车子模型可以用串口控制左右轮子分别以不同速度转动。
2. 车子模型串口第3个参数表示车子摄像头角度。摄像头pole和indicator整体可随参数改变方向
3. Ha中， 使用脚本 控制hachina3切换状态ON/OFF
4. Ha中，使用自动化控制切换hachina3状态ON/OFF
## 结果图
### car_animate:
![carsimple](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/car_animate/car_animate.gif)
### hachina:
![hachina](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/hachina/hachina3.gif)

# 20200527作业([hachina_door](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/hachina_door))
1. python显示门的三种状态：ON,OFF，LOCK。
2. 把三种状态实时更新到apache的网页中
3. Ha中是实时更新 ON,OFF，LOCK三种状态。
4. 效果屏幕拷贝/代码上传自己的目录
## 结果图
### door:
![door](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/hachina_door/door.gif)

# 20200529作业([vtk_door](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/VTK_hachina_door))
1. 在vtk里面仿真门的开、关
2. ha里和vtk里同步实时显示门的开、关状态
3. ha里和vtk里同步实时显示门的开、关状态。同时ha另加一个卡片上面显示 on/off
4. 效果屏幕拷贝/代码上传自己的目录
### vtk_door:
![vtk_door](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/VTK_hachina_door/vtk_door.gif)

# 20200601作业([clothes](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/clothes%26consumer/clothes) & [consumer](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/clothes%26consumer))
1. 完成chat/consumers.py的代码
2. 查阅资料，了解生产者消费者模式
3. 自动截取人脸并合成到语音换衣服的程序上。
4. 效果屏幕拷贝/代码上传自己的目录
### clothes:
![clothes](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/clothes%26consumer/clothes/clothes.gif)

# 20200603作业([井字棋](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/%E4%BA%95%E5%AD%97%E6%A3%8B%26Tensorflow/%E4%BA%95%E5%AD%97%E6%A3%8B) & [tensorflow](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/%E4%BA%95%E5%AD%97%E6%A3%8B%26Tensorflow/))
1. 完成语音九宫格下棋的程序，完善并提高识别率
2. 开始思考自己的个人项目方向
3.
4. 效果屏幕拷贝/代码上传自己的目录
### 井字棋:
![井字棋](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/%E4%BA%95%E5%AD%97%E6%A3%8B%26Tensorflow/%E4%BA%95%E5%AD%97%E6%A3%8B/chess.gif)

# 20200610作业([chatroom](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/chatroom))
1. 个人小项目制作6月15日答辩
2. 徐老师周一作业：使用异步方法优化代码
3. 更新代码到个人小项目文件夹的目录里
### chatroom:
![chatroom](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/chatroom/chatroom.gif)

# 20200622作业([Excel](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/Excel) & [REST_react](https://github.com/shiep18/EIS2020/tree/master/students/Gongyangyang/REST%20%26%20react) & [covid](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/covid))
1. 完成数据分析，获取表格中的特定行并生成新表格
2. 完成大项目分工
3. 更新代码到github个人小项目文件夹的目录里
### Excel:
![Excel](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/Excel/Excel.png)
### REST_react:
![Api](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/REST%20%26%20react/Api.png)
![react](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/REST%20%26%20react/react.png)
### covid:
![covid](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/covid/covid.png)

