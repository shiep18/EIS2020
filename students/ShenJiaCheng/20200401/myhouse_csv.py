import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
import csv
import time
import threading


class House:
    def __init__(self,x,y,z,l,w,h,num):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h
        self.num=num
        
    def house(self):
        mc.setBlocks(self.x,self.y-1,self.z,self.x+self.l,self.y+self.h-1,self.z+self.w,5,1)
        mc.setBlocks(self.x+1,self.y,self.z+1,self.x+self.l-1,self.y+self.h-2,self.z+self.w-1,0)   #建一个火柴盒
        mc.setBlocks(self.x+3,self.y+1,self.z,self.x+4,self.y+2,self.z,block.GLASS.id)#窗
        mc.setBlocks(self.x+6,self.y,self.z,self.x+6,self.y+1,self.z,64)              #门w
        

    def isInHouse(self,x0,y0,z0):
        if self.x<=x0<=self.x+self.l and self.y<=y0<=self.y+self.h and self.z<=z0<=self.z+self.w:
            return True
        else:
            return False

def whileinhouse():
    reader = csv.reader(open('house.csv'))
    data=[]
    name=[]
    for r in reader:
        data.append(r)
    for i in range(27):
        name.append(data[i][0])
        for j in range(7):
            data[i][j+1]=int(data[i][j+1])
        data[i][0]=House(data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7])
        data[i][0].house()
    while True:
        pos = mc.player.getTilePos()            #重新获取坐标位置
        for i in range(27):
            if data[i][0].isInHouse(pos.x,pos.y,pos.z):#判断在家就播放音频
                print("欢迎来到"+name[i]+"的家")

threads = []

t1 = threading.Thread(target=whileinhouse) # 使用多线程，使得两个检测循环同时进行
threads.append(t1)

if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
print ("退出")
