import mcpi.minecraft as minecraft
import random
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()


def house(x0,y0,z0,L,W,H,M):
    for x in range(L):# 清空房子内部
        for y in range(H):
            for z in range(W):
                mc.setBlock(x0+x, y0+y, z0+z, 0)
    for  y in range(H):# 墙面
        for x in range(L):
            mc.setBlock(x0 + x, y0 + y, z0, M)
            mc.setBlock(x0 + x, y0 + y, z0 + W - 1, M)
    for y in range(H):# 墙面
        for z in range(W):
            mc.setBlock(x0, y0 + y, z0 + z, M)
            mc.setBlock(x0 + L - 1, y0 + y, z0 + z, M)
    for z in range(W):# 天花板、地板
        for x in range(L):
            mc.setBlock(x0 + x, y0 + H - 1, z0 + z, (251, random.randint(0, 35)))
            mc.setBlock(x0 + x, y0, z0 + z, M)
    mc.setBlock(x0 + 5, y0 + 1, z0, 0)
    mc.setBlock(x0 + 5, y0 + 2, z0, 0)
    for z in range(2):
        for y in range(2):
            mc.setBlock(x0+10-1, y0+y+2, z0+z+4, 20)

d = 0#控制颜色
e = 35# 羊毛
for a in range(3):
    for b in range(3):
        for c in range(3):
            d = d + 1
            house(0+a*20, 0+b*20, 0+c*20, 10, 10, 5, (e, d))
            if  d == 15:
                e = 251#切换为混凝土
                d = 0

