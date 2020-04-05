import mcpi.minecraft as minecraft
import mcpi.block as block
import numpy as np
import os 
import csv
from functools import reduce
import time


def traverse_dir(current_dir):          #遍历目录下文件，读取csv
    file_list = os.listdir(current_dir)
    csv_file = []
    for file in file_list:
        path = os.path.join(current_dir, file)
        if os.path.isdir(path):
            pass
        if os.path.isfile(path):
            f1=open(path,"rb")
            case_train=np.loadtxt(f1,delimiter=',')
            f1.close()
            csv_file.append(np.array(case_train))
    return csv_file

def csv_read(name):
    with open(name, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    return result

class house():
    def __init__(self,data):
        self.data = data

    def roof(self,count):           #建屋顶和地板
        houseposs,M,roofs,floors,count = self.data
        pat = roofs[count]
        mh,x0,y0,z0,L,W,H = houseposs
        x0,y0,z0,L,W,H = list(map(eval,[x0,y0,z0,L,W,H]))
        for x in range(L):
            for z in range(W):
                if pat[x][z] == 0:
                    mc.setBlock(x0+L-x-1, y0+H-1, z0+z,block.GLASS.id)
                elif pat[x][z] == 2:
                    mc.setBlock(x0+L-x-1, y0+H-1, z0+z,block.DIAMOND_BLOCK.id)
                elif pat[x][z] == 3:
                    mc.setBlock(x0+L-x-1, y0+H-1, z0+z,block.REDSTONE_ORE.id)
                
                else:
                    mc.setBlock(x0+L-x-1, y0+H-1, z0+z,block.GOLD_BLOCK.id)
                
                mc.setBlock(x0+x, y0, z0+z,floors[count])   #建地板

    def buildhouse(self):
        houseposs,M,roofs,floors,count = self.data
        mh,x0,y0,z0,L,W,H = houseposs
        x0,y0,z0,L,W,H = list(map(eval,[x0,y0,z0,L,W,H]))
        for y in range(H):
            for x in range(L):
                mc.setBlock(x0+x,y0+y,z0,M)
                mc.setBlock(x0+x,y0+y,z0+W-1,M)
            for z in range(W):
                mc.setBlock(x0,y0+y,z0+z,M)
                mc.setBlock(x0+L-1,y0+y,z0+z,M)

        hndic[mh].roof(count) #屋顶地板

        mc.setBlock(x0+int(L/2), y0+1, z0,block.DOOR_WOOD.id) #门
        mc.setBlock(x0+int(L/2), y0+2, z0,block.DOOR_WOOD.id)

        for z in range(2):
            for y in range(2): 
                mc.setBlock(x0+L-1,y0+y+2,z0+z+4,20) #窗

    def buildall(self):
        mh = self.data[0][0]
        hndic[mh].buildhouse()
    
    def isInhouse(self):
        houseposs = self.data[0]
        mh,x,y,z,L,W,H = houseposs
        x,y,z,L,W,H = list(map(eval,[x,y,z,L,W,H]))
        pos = mc.player.getTilePos()
        x0,y0,z0 = pos.x,pos.y,pos.z
        if x <= x0 <= x+L and y <= y0 <= y+H and z <= z0 <= z+W:
            return True
        else :
            return False
    
def Inwhichhouse():
    ion_all = 0
    while True:       
        ion = 0
        for i in mhs:
            if hndic[i].isInhouse() :
                ion = 1
                if ion_all == 0 :
                    # print("Is in ",i)
                    mc.postToChat("Welcome to " + i + "'s home")
                    ion_all = 1
                    break
        if ion == 0:
            ion_all = 0



mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

roofs = traverse_dir("roofs")
houseposs = csv_read('housepos.csv')

M = 1
floors = [1,2,3,
          4,5,35,
          7,8,10,
        29,30,45,
        46,14,15,
        16,17,18,
        19,20,21,
        22,23,24,
        33,42,43] #地板样式

hnp = np.array(houseposs)
mhs = list(hnp[:,0])

hndic = {} # 房名字典

for i in range(27):
    hndic[mhs[i]] = house([houseposs[i],M,roofs,floors,i])
    hndic[mhs[i]].buildall()
