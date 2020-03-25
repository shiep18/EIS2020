import mcpi.minecraft as minecraft
import mcpi.block as block
import numpy as np
import os 


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


class house():
    def __init__(self,data):
        self.data = data

    def roof(self,count):           #建屋顶和地板
        x0,y0,z0,L,W,H,M,roofs,floors = self.data
        pat = roofs[count]
        for x in range(L):
            for z in range(W):
                if pat[x][z] == 0:
                    mc.setBlock(x0+x, y0+H-1, z0+z,block.GLASS.id)
                elif pat[x][z] == 2:
                    mc.setBlock(x0+x, y0+H-1, z0+z,block.DIAMOND_BLOCK.id)
                elif pat[x][z] == 3:
                    mc.setBlock(x0+x, y0+H-1, z0+z,block.REDSTONE_ORE.id)
                
                else:
                    mc.setBlock(x0+x, y0+H-1, z0+z,block.GOLD_BLOCK.id)
                
                mc.setBlock(x0+x, y0, z0+z,floors[count])   #建地板

    def buildhouse(self,count):
        x0,y0,z0,L,W,H,M,roofs,floors = self.data
        for y in range(H):
            for x in range(L):
                mc.setBlock(x0+x,y0+y,z0,M)
                mc.setBlock(x0+x,y0+y,z0+W-1,M)
            for z in range(W):
                mc.setBlock(x0,y0+y,z0+z,M)
                mc.setBlock(x0+L-1,y0+y,z0+z,M)

        mh.roof(count) #屋顶地板

        mc.setBlock(x0+int(L/2), y0+1, z0,block.DOOR_WOOD.id) #门
        mc.setBlock(x0+int(L/2), y0+2, z0,block.DOOR_WOOD.id)

        for z in range(2):
            for y in range(2): 
                mc.setBlock(x0+L-1,y0+y+2,z0+z+4,20) #窗

    def buildall(self):
        count = 0
        x0s = [0,2*self.data[3],4*self.data[3]]
        y0s = [0,4*self.data[5],8*self.data[5]]
        z0s = [0,2*self.data[4],4*self.data[4]] # 房子间隔
        for y in y0s:
            for x in x0s:           
                for z in z0s:
                    self.data[0] = pos.x + x
                    self.data[1] = pos.y + y
                    self.data[2] = pos.z + z
                    mh.buildhouse(count)
                    count += 1

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

roofs = traverse_dir("roofs")
floors = [1]   #屋顶样式

L = 10
W = 10
H = 6
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

mh = house([pos.x,pos.y,pos.z,L,W,H,M,roofs,floors])  #新加地板，实现27种地板
mh.buildall()

