import mcpi.minecraft as minecraft
import mcpi.block as block
import csv

mc = minecraft.Minecraft.create("47.100.46.95",4783)
entityId= mc.getPlayerEntityId("HJN")
pos=mc.entity.getPos(entityId)

def house(x,y,z):
    mc.setBlocks(x,y,z,x+9,y+4,z+9,5,2)
    mc.setBlocks(x+1,y,z+1,x+8,y+4,z+8,0)   #建一个火柴盒
    mc.setBlocks(x+9,y+1,z+5,x+9,y+2,z+4,0)     #门
    mc.setBlocks(x+1,y,z+1,x+8,y,z+8,169)   #地板
    mc.setBlocks(x,y+5,z,x+9,y+5,z+9,17)    #顶
    mc.setBlocks(x-1,y,z+10,x+10,y,z+10,190)
    mc.setBlocks(x-1,y,z-1,x+10,y,z-1,190)
    mc.setBlocks(x+10,y,z-1,x+10,y,z+10,190)
    mc.setBlocks(x-1,y,z-1,x-1,y,z+10,190)  #栅栏
    mc.setBlocks(x+10,y,z+5,x+10,y,z+4,126,2)
    mc.setBlocks(x+9,y+3,z+5,x+9,y+3,z+4,126,2) #台阶
    mc.setBlocks(x,y,z,x,y+4,z,17)
    mc.setBlocks(x+9,y,z,x+9,y+4,z,17)
    mc.setBlocks(x,y,z+9,x,y+4,z+9,17)
    mc.setBlocks(x+9,y,z+9,x+9,y+4,z+9,17)  #柱子
    for i in range(6):
        mc.setBlocks(x-1,y+5+i,z-1+i,x+10,y+5+i,z-1+i,80)
        mc.setBlocks(x-1,y+10-i,z+5+i,x+10,y+10-i,z+5+i,80)
    for i in range(4):
        mc.setBlocks(x,y+6+i,z+1+i,x,y+6+i,z+8-i,5,2)
        mc.setBlocks(x+9,y+6+i,z+1+i,x+9,y+6+i,z+8-i,5,2)#阁楼
    mc.setBlocks(x+9,y+2,z+2,x+9,y+3,z+2,20)
    mc.setBlocks(x+9,y+2,z+7,x+9,y+3,z+7,20)
    mc.setBlocks(x+3,y+2,z,x+6,y+3,z,20)
    mc.setBlocks(x+3,y+2,z+9,x+6,y+3,z+9,20)
    mc.setBlocks(x,y+2,z+3,x,y+3,z+6,20)
    mc.setBlocks(x,y+7,z+4,x,y+7,z+5,20)
    mc.setBlocks(x+9,y+7,z+4,x+9,y+7,z+5,20)#窗

reader = csv.reader(open('house.csv'))
data=[]
for r in reader:
    data.append(r)
for name in data:
    if name[0] == 'clancenter':
        cx=int(name[1])
        cy=int(name[2])
        cz=int(name[3])
    elif name[0] == 'hjn':
        sx=int(name[1])
        sy=int(name[2])
        sz=int(name[3])

house(cx+sx,cy+sy,cz+sz)

#hjn2020.5.11