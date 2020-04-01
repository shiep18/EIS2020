import mcpi.minecraft as minecraft
import random

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

x0 = pos.x
y0 = pos.y
z0 = pos.z
SIZE = 10

def house(x0,y0,z0,L,W,H,M):
    # 清空房子内部
    for x in range(L):
        for y in range(H):
            for z in range(W):
                mc.setBlock(x0+x,y0+y, z0+z,0)
    #建造墙面
    for  y in range(H):
        for x in range(L):
            mc.setBlock(x0+x,y0+y,z0,M)
            mc.setBlock(x0+x,y0+y,z0+W-1,M)
    for y in range(H):
        for z in range(W):
            mc.setBlock(x0,y0+y,z0+z,M)
            mc.setBlock(x0+L-1,y0+y,z0+z,M)
    #建造天花板
    for z in range(W):
        for x in range(L):
            mc.setBlock(x0+x,y0+H-1,z0+z,(251, random.randint(0,27)))
    #建造地板
    for z in range(W):
        for x in range(L):
            mc.setBlock(x0+x,y0,z0+z,M)
    #创造门（空气）
    mc.setBlock(x0+5,y0+1,z0,0)
    mc.setBlock(x0+5,y0+2,z0,0)
    for z in range(2):
        for y in range(2):
            mc.setBlock(x0+10-1,y0+y+2,z0+z+4,20)

d = 0#控制颜色
e = 35# 羊毛
for h in range(3):
    y0+=2*SIZE
    x0 = pos.x+2
    z0 = pos.z
    for s in range(3):
        z0+=2*SIZE
        x0 = pos.x+2
        for t in range(3):
            d = d + 1
            house(x0,y0,z0,10,10,5,(e,d))
            x0+=2*SIZE
            if d == 15:
                e = 251#切换为混凝土
                d = 0
