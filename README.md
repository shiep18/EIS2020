# EIS2020
Embedded and Intelligent Systems (EIS) course for SHIEP 2020

# 20200323作业
1. 学习M02 M06 ppt  
2. students目录下创建自己的文件夹  
3. 我的世界造房子myhouse.py上传  

# 20200325作业
1. 学习3D建模课件，挑3个ppt学习即可。 3个设计文件上传到自己的文件夹。 可以用123D也可以用fusion360  
2. 设计创意一个属于自己的物品。 mylogo.stl 文件上传。  
3. 在我的世界里显示自己的物品  mylogo.py 和binvox文件上传。 

# 20200327作业
1. 安装并配置git和vscode, 参见知乎的帖子[如何配置vscode和git](https://zhuanlan.zhihu.com/p/31417255)
2. 在我的世界里利用opencv，利用不同方块和颜色显示一幅线条卡通线条图mypic.jpg , 大小为32x32个方块，程序名为showmypic.py
3. 写一个myclan.py,import 调用mylogo和showmypic里面的函数，完成一次性显示一个logo和卡通图
4. 上传最后效果的屏幕拷贝

# 20200330作业  
1. 跑通倍塔狗语音识别代码
2. 能够用前进，后退，往左，往右指挥我的世界中的角色前后左右移动
3. 在我的世界中竖一个石柱，上海气温20度则高度为20块
4. 效果屏幕拷贝上传自己的目录

# 20200401作业
1. 将造房子的代码改造为类名字为House  类里面需要有isInHouse()函数判断是否在房子里。
2. 利用House类生成27个实例，每个房子的位置在csv文件中定义，csv文件格式举例如下
   housename,x,y,z,l,w,h  
   xknbighouse1,100,10,100,10,10,6  
   xknsmallhouse2,100,10,200,6,6,6  
3. 摄像头监视有运动物体进入画面时唱歌

# 20200403作业
1. 找一个物体作为指挥棒，通过视频和HSV颜色匹配画一个圆跟踪  
2. 利用找到的物体作为遥控器，遥控我的世界的玩家前后左右跑动。  
3. 跑到部落里不同的房子，显示“welcome to xxxx‘s house” xxx是房子的主人的名字  

# 20200408作业
1. 我的世界回到家后点亮arduino的一盏灯，走出家后arduino灯关闭
2. 阿里code团队里面写自己的名字 

# 20200410作业
1. 跑通人脸识别代码
2. 训练3个人脸，自己，家人，其他（比如猫).  
3. 利用人脸检测获得脸部图像保存到文件face.jpg里面
4. 我的世界用玻璃做门。如果是自己，则门变成空气，可以进去。arduino点亮1~4号灯
5. 我的世界用玻璃做门。如果是家人，则门变成空气，可以进去。arduino点亮5~8号灯
6. 其他人不开门（可以用自己带口罩充当）
7. 离开屋子灯熄灭
8. 演示效果用动图gif上传

# 20200415作业
1. 用socket接口编程在我的世界玩家脚下摆3x3的黄金块
2. mcpi协议参考https://github.com/brooksc/mcpipy/blob/master/mcpi/mcpi_protocol_spec.txt
3. 在A4纸大小厚2毫米的板子上设计一个arduino盒子，要求
   * 6个面，露出排针可供扩展
   * 露出USB口可插USB线
   * 一个竖杆插在arduino座上
   * 竖杆上留3个LED灯的位置作为红绿灯

# 20200417作业
1. 用web接口指挥我的世界人物前后左右后退
2. 通过网页在我的世界里建房子

# 20200422作业
1. 利用图像匹配找到minecraft窗口
2. 利用图像匹配找到mineraft窗口的4个角
3. 计算出minecraft窗口的大小
4. 点击进入我的世界连接好的服务
5. 如果已连接，点击回到世界
6. 修建环形跑道（可以用导入图片方式）

# FAQ 
* Q:我的世界游戏启动失败咋办？  
  * A:下载更新的版本。  
* Q:我的世界多人游戏选择了localhost,一直连不进去？  
  * A:确保start.bat已启动，下载游戏勾选下载forge,再不行更新java。  
* Q:在将3D模型导入我的世界程序运行时出现no moudle binvox_rw？  
  * A:要将.py文件与binvox文件放在一起  
 
# Markdown 基本语法
![markdown cheat sheet](https://github.com/shiep18/EIS2020/blob/master/markdowncheatsheet.JPG)

# 解决Github无法显示图片问题
参见 [如何修改host文件添加github](http://blog.csdn.net/weixin_42128813/article/details/102915578)

如果发现图片还是打不开，可以先清空浏览器的缓存图片。具体操作是：浏览器设置 -> 更多工具 -> 清除浏览数据，在弹窗中，时间范围选择“时间不限”，清除“缓存的图片和文件”。清除缓存后，再刷新页面试试。

# VSCODE 本地目录作为默认目录

![](https://github.com/kq2019/G9_2019/blob/master/vscfix_01.JPG)  
![](https://github.com/kq2019/G9_2019/blob/master/vscfix_02.JPG)
