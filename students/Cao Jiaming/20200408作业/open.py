import mcpi.minecraft as minecraft
import csv
import serial.tools.list_ports
import time
#com1
ser = serial.Serial(port='COM1')
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

#我的世界回到家后点亮arduino的一盏灯，走出家后arduino灯关闭

def run(action):
    ser.write(action.encode())

#house类
class House:
    def __init__(self, x, y, z, l, w, h, num):
        self.x = x
        self.y = y
        self.z = z
        self.l = l
        self.w = w
        self.h = h
        self.num = num

    def isInHouse(self, x0, y0, z0):
        if self.x <= x0 <= self.x + self.l and self.y <= y0 <= self.y + self.h and self.z <= z0 <= self.z + self.w:
            return True
        else:
            return False

#zhelishi hopouse.py
readers = csv.reader(open('cjmhouse.csv'))
dataLab = []
for r in readers:
    dataLab.append(r)
for i in range(27):
    for j in range(7):
        dataLab[i][j + 1] = int(dataLab[i][j + 1])
    dataLab[i][0] = House(dataLab[i][1], dataLab[i][2], dataLab[i][3], dataLab[i][4], dataLab[i][5], dataLab[i][6],
                          dataLab[i][7])
    print(dataLab[i][0])
i1 = 0
i2 = 0
i3 = 0
while True:
    pos = mc.player.getTilePos()
    i2 = 0
    for i in range(27):
        if dataLab[i][0].isInHouse(pos.x, pos.y, pos.z):
            i1 = 1
        else:
            i1 = 0
        i2 = i2 + i1
    if i2 != i3:
        if i2 == 0:
            run("1")
            print("1")
        else:
            run("0")
            print("0")
        i3 = i2
