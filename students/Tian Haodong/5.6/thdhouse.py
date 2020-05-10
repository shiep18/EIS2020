import mcpi.minecraft as minecraft
import csv
import os
import time



site = csv.reader(open('info.csv'))#读取房间的csv文件

data=[]
for read in site:
    data.append(read)

print(data)
print(data[0])
print(data[5])
x0=int(data[0][1])+int(data[5][1])
y0=int(data[0][2])+int(data[5][2])
z0=int(data[0][3])+int(data[5][3])
print(x0)
print(y0)
print(z0)


mc = minecraft.Minecraft.create('47.100.46.95',4784)

pos = mc.player.getTilePos()

mc.setBlocks(x0,y0,z0,x0+10,y0+10,z0+10,79)#建立房子

mc.setBlocks(x0+1,y0+1,z0+1,x0+9,y0+9,z0+9,0)#挖出空隙

mc.setBlocks(x0+4,y0+4,z0,x0+6,y0+6,z0,20)#窗

mc.setBlocks(x0,y0+1,z0+4,x0,y0+3,z0+5,0)#门


mc.setBlocks(x0,y0+10,z0,x0+10,y0+10,z0+10,21)#屋顶

'''
'47.100.46.95',4784
for i in range(10):
    for j in range(10):
        for o in range(10):
            mc.setBlock(x0+i,z0+j,y0+o,1)#建立房子
            
for i in range(9):
    for j in range(9):
        for o in range(9):
            mc.setBlock(x0+1+i,z0+1+j,y0+o+1,0)#挖出空隙
for i in range(3):
    for j in range(3):
        mc.setBlock(x0+4+i,y0,z0+4+j,block.GLASS.id)#窗
for i in range(4):
    mc.setBlock(x0,y0+4,z0+i,64)#门
for i in range(10):
    for j in range(10):
        mc.setBlock(x0+i,y0+j,z0+10,3)#屋顶
'''
