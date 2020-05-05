# 20200403作业
1. 找一个物体作为指挥棒，通过视频和HSV颜色匹配画一个圆跟踪  
2. 利用找到的物体作为遥控器，遥控我的世界的玩家前后左右跑动。  
3. 跑到部落里不同的房子，显示“welcome to xxxx‘s house” xxx是房子的主人的名字 

# 摄像头是镜像的，出于操作习惯我将左右调换了
![](https://github.com/shiep18/EIS2020/blob/master/students/zengkexiang/20200403/trace.gif)

# 遇到的问题：
1. 摄像头一直出现一个warning,然后一秒钟卡一次，重启电脑后读取摄像头时出现imshow函数的error。
  答：ret,img = cap.read(); while ret: cv.imshow("123",img)
2. from pykeyboard import PyKeyboard错误
  答：要下载pyHook和PyUserInput
3. import pythoncom错误
  答：将D:\python\Lib\site-packages\pywin32_system32中的pythoncom37.dll和pywintypes37.dll放在C:\Windows\System32中
