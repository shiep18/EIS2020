import mcpi.minecraft as minecraft
import mcpi.block as block
import csv

mc = minecraft.Minecraft.create()
#pos = mc.player.getTilePos()

#house function
def house(x0,y0,z0,M,num):

#wall
    for y in range(10):
        for x in range(10):
            mc.setBlock(x0+x, y0+y, z0,M)
            mc.setBlock(x0+x, y0+y, z0+9,M)
        for a in range(8):
            mc.setBlock(x0,y0+y,z0+1+a,M)
            mc.setBlock(x0+9, y0+y, z0+1+a,M)
#floor&ceil
    for x in range(10):
        for z in range(10):
            mc.setBlock(x0+x, y0, z0+z,M)
            mc.setBlock(x0+x, y0+9, z0+z,M)
    for a in range(8):
        mc.setBlock(x0, y0+y, z0+1+a,M)
        mc.setBlock(x0+9, y0+y, z0+1+a,M)
#pattern of ceil
    reader = csv.reader(open(str(1)+'.csv'))
    data=[]
    for r in reader:
        data.append(r)
    for i in range(10):
        for j in range(10):
            if (data[j][i]=='1'):
                mc.setBlock(x0+i,y0+9,z0+j,num)
#windows
    for y in range(2):
          for z in range(2): 
                mc.setBlock(x0+9, y0+y+2, z0+z+4,20)
#door
    mc.setBlock(x0+5, y0+1,z0,0)
    mc.setBlock(x0+5, y0+2,z0,0)


#(main)build 27-pattern house
count = 1
for x in range(3):
    for y in range(3):
        for z in range(3):
            house(10+15*x,10+15*y,10+15*z,219-1+count,219+count)
            count += 1
            
#clear
'''
for x in range(200):
    for y in range(55):
        for z in range(200):
            mc.setBlock(x-100, 10+y,z-100,0)
            
'''
