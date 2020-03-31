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
