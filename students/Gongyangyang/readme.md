# EIS2020
Embedded and Intelligent Systems (EIS) course for SHIEP 2020

# 20200323作业
1. 学习M02 M06 ppt
2. students目录下创建自己的文件夹
3. 我的世界造房子myhouse.py上传
## 结果图
![myhouse](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/myhouse/myhouse.png)

# 20200325作业
1. 学习3D建模课件，挑3个ppt学习即可。 3个设计文件上传到自己的文件夹。 可以用123D也可以用fusion360
2. 设计创意一个属于自己的物品。 mylogo.stl 文件上传。
3. 在我的世界里显示自己的物品 mylogo.py 和binvox文件上传。
## 结果图
![mylogo](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/mylogo/mylogo.png)

# 20200327作业
1. 安装并配置git和vscode, 参见知乎的帖子如何配置vscode和git
2. 在我的世界里利用opencv，利用不同方块和颜色显示一幅线条卡通线条图mypic.jpg , 大小为32x32个方块，程序名为showmypic.py
3. 写一个myclan.py,import 调用mylogo和showmypic里面的函数，完成一次性显示一个logo和卡通图
4. 上传最后效果的屏幕拷贝
## 结果图
![myclan](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/myclan/myclan.png)
### 分析：  
          * 把图片以灰度读入后，进行二值化处理，根据两种值分别分配不同颜色的方块，读取矩阵搭建后形成黑白图像。
          * 在myclan里调用两种函数，可对位置进行设定

# 20200330作业
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
          
# 20200401作业
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
          
# 20200403作业
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
          
# 20200408作业
1. 我的世界回到家后点亮arduino的一盏灯，走出家后arduino灯关闭
2. 阿里code团队里面写自己的名字
## 结果图
gif：
![myled](https://github.com/shiep18/EIS2020/blob/master/students/Gongyangyang/myled/myled.gif)
