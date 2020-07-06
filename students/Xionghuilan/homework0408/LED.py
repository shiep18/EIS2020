import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import serial.tools.list_ports
import time

ser = serial.Serial(port='COM2')
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.player.setTilePos([0,0,50])

def run(action):
    ser.write(action.encode())


class House:
    def __init__(self, x, y, z, l, w, h, num):
        self.x = x
        self.y = y
        self.z = z
        self.l = l
        self.w = w
        self.h = h
        self.num = num
        
    def buildhouse(self):
        mc.setBlocks(self.x, self.y - 1, self.z, self.x + self.l, self.y + self.h - 1, self.z + self.w, 35,6)
        mc.setBlocks(self.x + 1, self.y, self.z + 1, self.x + self.l - 1, self.y + self.h - 2, self.z + self.w - 1,0)
        mc.setBlocks(self.x + 3, self.y + 1, self.z, self.x + 4, self.y + 2, self.z, 57)
        mc.setBlocks(self.x, self.y, self.z + 4, self.x, self.y + 1, self.z + 5, 0)
        roof = csv.reader(open('roof' + str(self.num) + '.csv', encoding='UTF-8'))
        count = []
        for ro in roof:
            count.append(ro)
        for a in range(10):
            for b in range(10):
                if count[a][b] == '1':
                    mc.setBlock(self.x + a, self.y + self.h - 1, self.z + b, 35, 3)

    def isInHouse(self, x0, y0, z0):
        if self.x <= x0 <= self.x + self.l and self.y <= y0 <= self.y + self.h and self.z <= z0 <= self.z + self.w:
            return True
        else:
            return False


readers = csv.reader(open('house.csv'))
dataLab = []
name=[]
for r in readers:
    dataLab.append(r)
for i in range(27):
    name.append(dataLab[i][0])
    for j in range(7):
        dataLab[i][j + 1] = int(dataLab[i][j + 1])
    dataLab[i][0] = House(dataLab[i][1], dataLab[i][2], dataLab[i][3], dataLab[i][4], dataLab[i][5], dataLab[i][6],
                          dataLab[i][7])
    dataLab[i][0].buildhouse()
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
            mc.postToChat("welcome to "+name[i]+"'s house")
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
