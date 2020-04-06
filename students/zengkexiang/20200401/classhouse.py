import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import random

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def cratcsv(x,y,z,l,h,w):
    f = open('houses.csv', "w", newline='')
    csv_writer = csv.writer(f)
    # 构建列表头
    csv_writer.writerow(["housename", "x", "y","z","l","h","w"])
    i = 0
    for a in range(3):   #做27个
        for b in range(3):
            for c in range(3):
                i += 1
                csv_writer.writerow(["housename%s"%i, x + 20 * c, y + 20 * a, z + 20 * b, l, h, w])
    f.close()

class House:
    def __init__(self,name,x,y,z,l,h,w):
        self.x = x
        self.y = y
        self.z = z
        self.l = l
        self.h = h
        self.w = w
        self.name = name
    def housesetting(self): #打印房子属性
        print(self.name,self.x,self.y,self.z,self.l,self.h,self.w)
    def buildhouse(self):
        for y0 in range(self.h):  # wall
            for a in range(self.l):
                mc.setBlock(self.x + a, self.y + y0, self.z, 79)
                mc.setBlock(self.x + a, self.y + y0, self.z + 9, 79)
            for a in range(self.w-2):
                mc.setBlock(self.x, self.y + y0, self.z + 1 + a, 79)
                mc.setBlock(self.x + 9, self.y + y0, self.z + 1 + a, 79)
        for x0 in range(self.l):  # floor
            for z0 in range(self.w):
                mc.setBlock(self.x + x0, self.y, self.z + z0, 80)
        for x0 in range(self.l):  # ceiling
            for z0 in range(self.w):
                mc.setBlock(self.x + x0, self.y + self.h - 1, self.z + z0, 42)
        mc.setBlock(self.x + 5, self.y + 1, self.z, 0)  # door
        mc.setBlock(self.x + 5, self.y + 2, self.z, 0)
        mc.setBlock(self.x + 4, self.y + 1, self.z, 0)  # door
        mc.setBlock(self.x + 4, self.y + 2, self.z, 0)
        for z0 in range(2):  # windows
            for y0 in range(2):
                mc.setBlock(self.x + 9, self.y + y0 + 2, self.z + z0 + 4, 20)
        for z0 in range(2):  # windows
            for y0 in range(2):
                mc.setBlock(self.x, self.y + y0 + 2, self.z + z0 + 4, 20)
        for x0 in range(2):  # windows
            for y0 in range(2):
                mc.setBlock(self.x + x0 + 2, self.y + y0 + 6, self.z, 20)
        for x0 in range(2):  # windows
            for y0 in range(2):
                mc.setBlock(self.x + x0 + 6, self.y + y0 + 6, self.z, 20)




    def isinhouse(self,x0,y0,z0):
        if  self.x < x0 <(self.x+self.l) and  self.y < y0 <(self.y+self.h) and  self.z < z0 <(self.z+self.w):
            return True
        else :
            return False

cratcsv(351,8,644,10,10,10)
mc.player.setTilePos(340,8,644)
with open('houses.csv',"r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows=[row for row in reader]
    for a in range(27):
        myhouse = House(rows[a]["housename"],int(rows[a]["x"]),int(rows[a]["y"]),int(rows[a]["z"]),int(rows[a]["l"]),int(rows[a]["h"]),int(rows[a]["w"]))
        myhouse.housesetting()
        myhouse.buildhouse()
