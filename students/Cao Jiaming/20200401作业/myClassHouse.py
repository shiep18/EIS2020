import mcpi.minecraft as minecraft
import csv
import os
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


class House:
    def __init__(self, x, y, z, l, w, h, num):
        self.x = x
        self.y = y
        self.z = z
        self.l = l
        self.w = w
        self.h = h
        self.num = num

    def house(self):
        mc.setBlocks(self.x, self.y - 1, self.z, self.x + self.l, self.y + self.h - 1, self.z + self.w, 35, 10)
        mc.setBlocks(self.x + 1, self.y, self.z + 1, self.x + self.l - 1, self.y + self.h - 2, self.z + self.w - 1,
                     0)
        mc.setBlocks(self.x + 3, self.y + 1, self.z, self.x + 4, self.y + 2, self.z, 20)
        mc.setBlocks(self.x, self.y, self.z + 4, self.x, self.y + 1, self.z + 5, 0)
        roof = csv.reader(open('roof' + str(self.num) + '.csv', encoding='UTF-8'))
        count = []
        for ro in roof:
            count.append(lv)
        for a in range(10):
            for b in range(10):
                if count[a][b] == '1':
                    mc.setBlock(self.x + a, self.y + self.h - 1, self.z + b, 35, 3)

    def isInHouse(self, x0, y0, z0):
        if self.x <= x0 <= self.x + self.l and self.y <= y0 <= self.y + self.h and self.z <= z0 <= self.z + self.w:
            return True
        else:
            return False


readers = csv.reader(open('cjmhouse.csv'))
dataLab = []
for r in readers:
    dataLab.append(r)
for i in range(27):
    for j in range(7):
        dataLab[i][j + 1] = int(dataLab[i][j + 1])
    dataLab[i][0] = House(dataLab[i][1], dataLab[i][2], dataLab[i][3], dataLab[i][4], dataLab[i][5], dataLab[i][6],
                          dataLab[i][7])
    dataLab[i][0].house()
while True:
    pos = mc.player.getTilePos()
    for i in range(27):
        if dataLab[i][0].isInHouse(pos.x, pos.y, pos.z):
            print("Welcome back")
            os.system("singsong.mp3")
            time.sleep(6)
