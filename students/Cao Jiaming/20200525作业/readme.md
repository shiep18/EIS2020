# 20200525 operation

1. The car model can use serial port to control the left and right wheels to rotate at different speeds.

2. The third parameter of the car model serial port indicates the car camera angle. Camera pole and indicator can change direction with parameters as a whole

3. In ha, use script to control hachina3 to switch on / off

4. In ha, use automatic control to switch hachina3 status on / off

# 20200525作业 
1. 车子模型可以用串口控制左右轮子分别以不同速度转动。
2. 车子模型串口第3个参数表示车子摄像头角度。摄像头pole和indicator整体可随参数改变方向
3. Ha中， 使用脚本 控制hachina3切换状态ON/OFF
4. Ha中，使用自动化控制切换hachina3状态ON/OFF

# 如何在 GitHub.com 上删除某个文件夹？
删除文件夹:
删除文件夹非常简单，删除或者移动里面文件即可，空文件夹Github自动删除。

或者Git命令（需要保持被操作Github项目已在本地下拉并为最新版本）：

git rm -r --cached flashview                   //--cached不会把本地的flashview文件夹删除
git commit -m '我删除了flashview文件夹'         //单引号里为Commit时需要提交的说明
git push -u origin master                      //若需要对其他分支进行操作，则把master换为对应分支，如:git push -u origin dev
至于Github重命名文件夹和删除类似，移动文件后自动删除旧文件夹，然后创建新文件夹。或者本地修改了文件夹名称，然后提交到Github。

# 如何在 GitHub.com 上删除某个 Repository 中的某个文件夹？
如果是需要在远程仓库中忽略已纳入版本管理中的文件或文件夹，可以这样操作：1，删除本地git缓存git rm -r --cached <filename>2，在.gitignore中加入需要忽略的文件夹或文件3，重新track文件git add -A
git commit -m "remove files"4，推送到远程仓库git push origin master

