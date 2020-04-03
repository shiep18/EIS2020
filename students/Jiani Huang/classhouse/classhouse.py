import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
import csv
import os
import time
#print("player pos is",pos)     #player pos is Vec3(108,2,-88)
class House:
    def __init__(self,x,y,z,l,w,h):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h

    def house(self,num):
        mc.setBlocks(self.x,self.y-1,self.z,self.x+self.l,self.y+self.h-1,self.z+self.w,5,3)
        mc.setBlocks(self.x+1,self.y,self.z+1,self.x+self.l-1,self.y+self.h-2,self.z+self.w-1,0)   #建一个火柴盒
        mc.setBlocks(self.x+3,self.y+1,self.z,self.x+4,self.y+2,self.z,block.GLASS.id)#窗
        mc.setBlocks(self.x+6,self.y,self.z,self.x+6,self.y+1,self.z,64)              #门
        reader = csv.reader(open(str(num)+'.csv'))                                      #屋顶
        data=[]
        for r in reader:
            data.append(r)
        for i in range(10):
            for j in range(10):
                if (data[j][i]=='1'):
                    mc.setBlock(self.x+i,self.y+5,self.z+j,79)

    def isInHouse(self,x0,y0,z0):
        if self.x<=x0<=self.x+self.l and self.y<=y0<=self.y+self.h and self.z<=z0<=self.z+self.w:
            return True
        else:
            return False

myhouse1=House(pos.x+1,pos.y,pos.z,9,9,6)   #坐标和房子大小
myhouse1.house(20)                          #建房子，选择屋顶花纹
while True:
    pos = mc.player.getTilePos()            #重新获取坐标位置
    if myhouse1.isInHouse(pos.x,pos.y,pos.z):#判断在家就播放音频
        os.system("欢迎回家.wav")          
        time.sleep(6)
