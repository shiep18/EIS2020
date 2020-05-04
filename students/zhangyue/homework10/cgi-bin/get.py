#!D:\Program Files\Python37\python.exe
# coding=utf-8
import cgi
import csv

import mcpi.minecraft as minecraft

# 创建 FieldStorage 实例化
form = cgi.FieldStorage()
mc = minecraft.Minecraft.create()


# 移动位置
def mcgo(dir, lens):
    direction = mc.player.getDirection()
    pos = mc.player.getTilePos()
    x = pos.x
    z = pos.z
    if dir == "strange":
        x = pos.x + (direction.x * lens)
        z = pos.z + (direction.z * lens)
    elif dir == "back":
        x = pos.x + (direction.x * (-1 * lens))
        z = pos.z + (direction.z * (-1 * lens))
    elif dir == "right":
        x = pos.x + (direction.z * (-1 * lens))
        z = pos.z + (direction.x * lens)
    elif dir == "left":
        x = pos.x + (direction.z * lens)
        z = pos.z + (direction.x * (-1 * lens))
    mc.player.setPos(x, pos.y, z)


# 获取数据
mc_strange = form.getvalue('mc_strange')
mc_back = form.getvalue('mc_back')
mc_right = form.getvalue('mc_right')
mc_left = form.getvalue('mc_left')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>Minecraft move</title>")
print("<body>")
print("<h2>%s:%s</h2>" % ('w', mc_strange))
print("<h2>%s:%s</h2>" % ('a', mc_left))
print("<h2>%s:%s</h2>" % ('s', mc_back))
print("<h2>%s:%s</h2>" % ('d', mc_right))
print("</body>")
print("</html>")

with open('move.csv', "r+") as f:
    read_data = f.read()
    f.seek(0)
    f.truncate()  # 清空文件

with open('move.csv', 'w', newline='') as f:
    csvWriter = csv.writer(f, dialect="excel")
    csvWriter.writerow(['w', mc_strange])
    csvWriter.writerow(['a', mc_left])
    csvWriter.writerow(['s', mc_back])
    csvWriter.writerow(['d', mc_right])

mcgo('strange', int(mc_strange)*2)
mcgo('left', int(mc_left)*2)
mcgo('right', int(mc_right)*2)
mcgo('back', int(mc_back)*2)
