
import mcpi.minecraft as minecraft
import mcpi.block as block
import csv

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

#house function
def house(x0,y0,z0,num):

#huose
    for y in range(10):
        for x in range(10):
            mc.setBlock(x0+x, y0+y, z0,2)
            mc.setBlock(x0+x, y0+y, z0+9,2)
        for a in range(8):
            mc.setBlock(x0,y0+y,z0+1+a,2)
            mc.setBlock(x0+9, y0+y, z0+1+a,2)
    for x in range(10):
        for z in range(10):
            mc.setBlock(x0+x, y0, z0+z,2)
            mc.setBlock(x0+x, y0+9, z0+z,2)
    for a in range(8):
        mc.setBlock(x0, y0+y, z0+1+a,2)
        mc.setBlock(x0+9, y0+y, z0+1+a,2)
    mc.setBlock(x0+5, y0+1,z0,0)
    mc.setBlock(x0+5, y0+2,z0,0)
    #windows
    for y in range(2):
          for z in range(2): 
                mc.setBlock(x0+9, y0+y+2, z0+z+5,20)
#pattern of ceil
    reader = csv.reader(open(str(num)+'.csv'))
    data=[]
    for r in reader:
        data.append(r)
    for i in range(10):
        for j in range(10):
            if (data[j][i]=='1'):
                mc.setBlock(x0+i,y0+9,z0+j,79)
count = 1
for x in range(3):
    for y in range(3):
        for z in range(3):
            house(pos.x+15*x,pos.y+15*y,pos.z+15*z,count)
            count += 1



