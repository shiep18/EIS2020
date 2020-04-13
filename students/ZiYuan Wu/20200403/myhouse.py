import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
from RecMan import *
import threading
import time


mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
class House:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.l = 8
        self.w = 8
        self.h = 8

    def house(self,x,y,z,L,w,h):
        #print("i will build a house here.",self.x,self.y,self.z,self.l,self.h) 
        mc.setBlocks(x,y-1,z,x+L,y+h,z+w,5,block.TNT.id)
        mc.setBlocks(x+1,y,z+1,x+L-1,y+4,z+w-1,0)   #建一个火柴盒
        mc.setBlocks(x+3,y+1,z,x+4,y+2,z,block.GLASS.id)#窗
        mc.setBlocks(x+6,y,z,x+6,y+1,z,64)              #门

    def roof(self,x,y,z,w,L,wordn):
        reader = csv.reader(open('e:/2020class/QianRuShi/4.1/CSV/'+wordn+'.csv'))
        data=[]
        for r in reader:
            data.append(r)
        for i in range(w):
            for j in range(L):
                if (data[j][i]=='1'):
                    mc.setBlock(x+i,y+5,z+j,158)
                else:
                    mc.setBlock(x+i,y+5,z+j,169)
                    mc.setBlock(x+i,y+6,z+j,50)

    def readhouse(self):
        reader = csv.reader(open('house.csv'))
        data=[]
        for r in reader:
            data.append(r)
        return data

    def Buildh(self,location,datan):
        #mc.setBlocks(x0,y0-10,z0,x0+200,y0+50,z0+200,0)
        #wordy = words.split(".")
        #numi = len(wordy)  #列数
        #L0=9
        for i in range(len(location)):                 
            House.house(self,int(location[i][1]),int(location[i][2]),int(location[i][3]),int(location[i][4]),int(location[i][5]),int(location[i][6]))#xyzlwh
            House.roof(self,int(location[i][1]),int(location[i][2]),int(location[i][3]),int(location[i][4]),int(location[i][5]),datan[i])


    def isInHouse(self):
        mark = "ABCDEFGHIJKLMNOPQRSTUVWXYZ["
        location = House.readhouse(0)
        while(1):
            pos = mc.player.getTilePos()
            x0 = pos.x
            y0 = pos.y
            z0 = pos.z
            for i in range(len(location)):
                x = int(location[i][1])
                y = int(location[i][2])
                z = int(location[i][3])
                
                if(x<x0<x+5 and y-5< y0 < y+10 and z < z0 < z0+5):
                    print("You are in a house "+mark[i])
                else:
                    pass
            time.sleep(0.1)

#mc.setBlocks(90,5,90,200,9,200,5)
mc.player.setPos(100,10,100)
mc.setBlocks(pos.x,pos.y-10,pos.z,pos.x+300,pos.y+100,pos.z+300,0)
proof = "ABCDEFGHIJKLMNOPQRSTUVWXYZ["       
houseloc = House.readhouse(0)
House.Buildh(0,houseloc,proof)  #建房子
House.isInHouse(0)  #判断在哪个房子里;死循环






