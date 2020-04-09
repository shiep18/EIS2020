import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import os
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

class House:
    def __init__(self,x,y,z,l,w,h,i):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h
        self.i=i

    def isInHouse(self,x0,y0,z0):#判断人物是否在房间内部
        if self.x<=x0<=self.x+self.l and self.y<=y0<=self.y+self.h and self.z<=z0<=self.z+self.w:
            return True
        else:
            return False

    def house(self):
        mc.setBlocks(self.x,self.y-1,self.z,self.x+self.l,self.y+self.h-1,self.z+self.w,5,1)#建立房子
        mc.setBlocks(self.x+1,self.y,self.z+1,self.x+self.l-1,self.y+self.h-2,self.z+self.w-1,0)#挖出空间
        mc.setBlocks(self.x+3,self.y+1,self.z,self.x+4,self.y+2,self.z,block.GLASS.id)#窗
        mc.setBlocks(self.x+6,self.y,self.z,self.x+6,self.y+1,self.z,64)#建一个门
        house = csv.reader(open(str(self.i)+'.csv'))#读取花纹的csv文件
        data=[]
        for read in house:
            data.append(read)
        for i in range(10):
            for j in range(10):
                if (data[j][i]=='1'):
                    mc.setBlock(self.x+i,self.y+9,self.z+j,49)

reader = csv.reader(open('house.csv'))#读取房间的csv文件
data=[]
for r in reader:
    data.append(r)
for i in range(27):
    for j in range(7):
        data[i][j+1]=int(data[i][j+1])
    data[i][0]=House(data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7])
    data[i][0].house()

while True:
    pos = mc.player.getTilePos()#获取人物坐标            
    for i in range(27):
        if data[i][0].isInHouse(pos.x,pos.y,pos.z):
            print("您现在处于房间内")
