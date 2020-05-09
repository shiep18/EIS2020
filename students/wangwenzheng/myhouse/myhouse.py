import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

x=pos.x
y=pos.y
z=pos.z
size=8
num=1


def build():
    material = ['1','5','41','42','45','80','98','133']#8
    a = random.randint(0,7)
    mc.setBlocks(x,y,z,x+size,y+size,z+size,int(material[a]))
    mc.setBlocks(x+1,y+1,z+1,x+size-1,y+size-1,z+size-1,0)#房子
    mc.setBlocks(x+2,y,z,x+4,y+5,z,0)#门
    mc.setBlocks(x+3,y+4,z+8,x+5,y+6,z+8,20)#窗户
    fname=str(num)+".csv"
    f=open(fname, "r")
    b=c=0
    for line in f.readlines():
        data = line.split(",")
        for cell in data:
            if cell=="1" or cell=="1\n":
                mc.setBlock(x+b,y+8,z+c,52)
            b=b+1
            if b==9 :
                b=0
        c=c+1       
    mc.setBlock(x+4,y,z+4,89)#灯
    mc.setBlock(x+4,y+8,z+4,89)#灯

for height in range(3):
    x=pos.x
    z=pos.z
    for width in range(3):
        x=pos.x
        for length in range(3):
            x=x+15
            build()
            num=num+1
        z=z+15
    y=y+15
        




