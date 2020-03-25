import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
import random
SIZE=10
pos = mc.player.getTilePos()
for k in range(3):
    x = pos.x+k*20+2
    y = pos.y
    z = pos.z
    midx = x+SIZE/2
    midy = y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
    for i in range(10):#使用随机数生成随机花纹
        for j in range(10):
            num=random.randint(0,5)
            if num==0:
                mc.setBlock(x+i,y+10, z+j,2)
            elif num==1:
                mc.setBlock(x+i,y+10, z+j,35.5)
            elif num==2:
                mc.setBlock(x+i,y+10, z+j,35.2)
            elif num==3:
                mc.setBlock(x+i,y+10,z+j,19)
            elif num==4:
                mc.setBlock(x+i,y+10,z+j,35.1)
for k in range(3):
    x = pos.x+k*20+2
    y = pos.y
    z = pos.z+20
    midx = x+SIZE/2
    midy = y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
    for i in range(10):#使用随机数生成随机花纹
        for j in range(10):
            num=random.randint(0,5)
            if num==0:
                mc.setBlock(x+i,y+10, z+j,2)
            elif num==1:
                mc.setBlock(x+i,y+10, z+j,35.5)
            elif num==2:
                mc.setBlock(x+i,y+10, z+j,35.2)
            elif num==3:
                mc.setBlock(x+i,y+10,z+j,19)
            elif num==4:
                mc.setBlock(x+i,y+10,z+j,35.1)
for k in range(3):
    x = pos.x+k*20+2
    y = pos.y
    z = pos.z+40
    midx = x+SIZE/2
    midy = y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
    for i in range(10):#使用随机数生成随机花纹
        for j in range(10):
            num=random.randint(0,5)
            if num==0:
                mc.setBlock(x+i,y+10, z+j,2)
            elif num==1:
                mc.setBlock(x+i,y+10, z+j,35.5)
            elif num==2:
                mc.setBlock(x+i,y+10, z+j,35.2)
            elif num==3:
                mc.setBlock(x+i,y+10,z+j,19)
            elif num==4:
                mc.setBlock(x+i,y+10,z+j,35.1)
for k in range(3):
    x = pos.x+k*20+2
    y = pos.y+20
    z = pos.z
    midx = x+SIZE/2
    midy = y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
    for i in range(10):#使用随机数生成随机花纹
        for j in range(10):
            num=random.randint(0,5)
            if num==0:
                mc.setBlock(x+i,y+10, z+j,2)
            elif num==1:
                mc.setBlock(x+i,y+10, z+j,35.5)
            elif num==2:
                mc.setBlock(x+i,y+10, z+j,35.2)
            elif num==3:
                mc.setBlock(x+i,y+10,z+j,19)
            elif num==4:
                mc.setBlock(x+i,y+10,z+j,35.1)
for k in range(3):
    x = pos.x+k*20+2
    y = pos.y+20
    z = pos.z+20
    midx = x+SIZE/2
    midy = y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
    for i in range(10):#使用随机数生成随机花纹
        for j in range(10):
            num=random.randint(0,5)
            if num==0:
                mc.setBlock(x+i,y+10, z+j,2)
            elif num==1:
                mc.setBlock(x+i,y+10, z+j,35.5)
            elif num==2:
                mc.setBlock(x+i,y+10, z+j,35.2)
            elif num==3:
                mc.setBlock(x+i,y+10,z+j,19)
            elif num==4:
                mc.setBlock(x+i,y+10,z+j,35.1)
for k in range(3):
    x = pos.x+k*20+2
    y = pos.y+20
    z = pos.z+40
    midx = x+SIZE/2
    midy = y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
    for i in range(10):#使用随机数生成随机花纹
        for j in range(10):
            num=random.randint(0,5)
            if num==0:
                mc.setBlock(x+i,y+10, z+j,2)
            elif num==1:
                mc.setBlock(x+i,y+10, z+j,35.5)
            elif num==2:
                mc.setBlock(x+i,y+10, z+j,35.2)
            elif num==3:
                mc.setBlock(x+i,y+10,z+j,19)
            elif num==4:
                mc.setBlock(x+i,y+10,z+j,35.1)
for k in range(3):
    x = pos.x+k*20+2
    y = pos.y+40
    z = pos.z
    midx = x+SIZE/2
    midy = y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
    for i in range(10):#使用随机数生成随机花纹
        for j in range(10):
            num=random.randint(0,5)
            if num==0:
                mc.setBlock(x+i,y+10, z+j,2)
            elif num==1:
                mc.setBlock(x+i,y+10, z+j,35.5)
            elif num==2:
                mc.setBlock(x+i,y+10, z+j,35.2)
            elif num==3:
                mc.setBlock(x+i,y+10,z+j,19)
            elif num==4:
                mc.setBlock(x+i,y+10,z+j,35.1)
for k in range(3):
    x = pos.x+k*20+2
    y = pos.y+40
    z = pos.z+20
    midx = x+SIZE/2
    midy = y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
    for i in range(10):#使用随机数生成随机花纹
        for j in range(10):
            num=random.randint(0,5)
            if num==0:
                mc.setBlock(x+i,y+10, z+j,2)
            elif num==1:
                mc.setBlock(x+i,y+10, z+j,35.5)
            elif num==2:
                mc.setBlock(x+i,y+10, z+j,35.2)
            elif num==3:
                mc.setBlock(x+i,y+10,z+j,19)
            elif num==4:
                mc.setBlock(x+i,y+10,z+j,35.1)
for k in range(3):
    x = pos.x+k*20+2
    y = pos.y+40
    z = pos.z+40
    midx = x+SIZE/2
    midy = y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
    for i in range(10):#使用随机数生成随机花纹
        for j in range(10):
            num=random.randint(0,5)
            if num==0:
                mc.setBlock(x+i,y+10, z+j,2)
            elif num==1:
                mc.setBlock(x+i,y+10, z+j,35.5)
            elif num==2:
                mc.setBlock(x+i,y+10, z+j,35.2)
            elif num==3:
                mc.setBlock(x+i,y+10,z+j,19)
            elif num==4:
                mc.setBlock(x+i,y+10,z+j,35.1)
