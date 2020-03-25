import mcpi.minecraft as minecraft
import mcpi.block as block
import random
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
#流动、掉落的方块
num=0
def shoufig(xo=pos.x, yo=pos.y, zo=pos.z, L=10, W=10, H=10):
    global num
    num+=1
    if num > 0 and num <= 27:
        fname = "fig" + str(num) + ".csv"
        f = open(fname, "r")
#显示5*7的图案，因为读数据是从上至下，所以offsetX为4，先扫Z轴，再扫X轴，Y轴不变
        offsetX = 4
        offsetZ = 0
        for line in f.readlines():
            data = line.split(",")
            for cell in data:
                if cell == "1" or cell == "1\n":
                    mc.setBlock(xo + offsetX, yo + H - 1, zo + offsetZ,block.GOLD_BLOCK.id)
                offsetZ = offsetZ + 1
            offsetX = offsetX-1
            offsetZ = 0
def build(xo=pos.x, yo=pos.y, zo=pos.z, L=10, W=10, H=10, M=0, fig=1):
    M=random.randint(1,5)
#墙
    for y in range(H):
        for x in range(L):
            mc.setBlock(xo + x, yo + y, zo, M)
            mc.setBlock(xo + x, yo + y, zo + W - 1, M)#XY轴的两面墙
        for z in range(W - 2):
            mc.setBlock(xo, yo + y, zo + 1 + z, M)
            mc.setBlock(xo + L - 1, yo + y, zo + 1 + z, M)#YZ轴两面墙
#屋顶地板
    for x in range(L):
        for z in range(W):
            mc.setBlock(xo + x, yo, zo + z, M)#XZ轴的底--地板
            mc.setBlock(xo + x, yo + H - 1, zo + z, 35, 0)#XZ的顶--没有花纹的屋顶
#照明（海晶灯）
    for x in range(2):
        for z in range(2):
            mc.setBlock(xo + x + (L - 2) / 2, yo, zo + (W - 2) / 2 + z, 169)
            mc.setBlock(xo + x + (L - 2) / 2, yo + H - 2, zo + (W - 2) / 2 + z, 169)
            mc.setBlock(xo, yo + 4 + x, zo + (W - 2) / 2 + z, 169)#三个2*2的照明
#门
    mc.setBlock(xo + L / 2, yo + 1, zo, 0)
    mc.setBlock(xo + L / 2, yo + 2, zo, 0)#一个1*2的门
#玻璃
    for z in range(2):
        for y in range(2):
            mc.setBlock(xo + L - 1, yo + y + 2, zo + (W - 2) / 2 + z,20)#一个2*2的玻璃
#屋顶花纹
    shoufig(xo + (L - 5) / 2,yo, zo + (W - 6) / 2)
#主函数，造3*3*3共27栋房子
i=0
x=pos.x
y=pos.y
z=pos.z
for a in range(3):
    for b in range(3):
        for c in range(3):
            i+=1
            build(x+20*(3-b), y+20*a, z+20*c)