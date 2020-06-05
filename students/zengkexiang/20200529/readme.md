# 20200529作业 
1. 在vtk里面仿真门的开、关
2. ha里和vtk里同步实时显示门的开、关状态
3. ha里和vtk里同步实时显示门的开、关状态。同时ha另加一个卡片上面显示 on/off
4. 效果屏幕拷贝/代码上传自己的目录

# 效果
![](https://github.com/shiep18/EIS2020/blob/master/students/zengkexiang/20200529/door.gif)

# 遇到的问题：
* Q:hachina50和hachin3联动自动化有问题。
  A:hachina50中读取网页中的数据时用的是readline,赋给状态时会多一个小尾巴，所以赋给状态之前要先strip一下。
* vtk的旋转中心真是要人命。
