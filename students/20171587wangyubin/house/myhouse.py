import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
#流动、掉落的方块
ban=[6,8,9,10,11,12,13,18,26,27]

def shoufig(xo=pos.x, yo=pos.y, zo=pos.z, L=10, W=10, H=10, num=1):
    if num >= 0 and num <= 27:
        fname = "fig" + str(num) + ".csv"
        f = open(fname, "r")
        offsetX = 4
        offsetZ = 0
        for line in f.readlines():
            data = line.split(",")
            for cell in data:
                if cell == "1" or cell == "1\n":
                    mc.setBlock(xo + offsetX, yo + H - 1, zo + offsetZ, 35, 1)
                offsetZ = offsetZ + 1
            offsetX = offsetX - 1
            offsetZ = 0


def build(xo=pos.x, yo=pos.y, zo=pos.z, L=10, W=10, H=10, M=1, fig=1):
    for i in ban:
        if i == M:
            M = 169 
#墙
    for y in range(H):
        for x in range(L):
            mc.setBlock(xo + x, yo + y, zo, M)
            mc.setBlock(xo + x, yo + y, zo + W - 1, M)
        for z in range(W - 2):
            mc.setBlock(xo, yo + y, zo + 1 + z, M)
            mc.setBlock(xo + L - 1, yo + y, zo + 1 + z, M)
#屋顶地板
    for x in range(L):
        for z in range(W):
            mc.setBlock(xo + x, yo, zo + z, M)
            mc.setBlock(xo + x, yo + H - 1, zo + z, 35, 0)
#照明（海晶灯）
    for x in range(2):
        for z in range(2):
            mc.setBlock(xo + x + (L - 2) / 2, yo,
                        zo + (W - 2) / 2 + z, 169)
            mc.setBlock(xo + x + (L - 2) / 2, yo + H - 2,
                        zo + (W - 2) / 2 + z, 169)
            mc.setBlock(xo, yo + 4 + x, zo + (W - 2) / 2 + z, 169)

#门
    mc.setBlock(xo + L / 2, yo + 1, zo, 0)
    mc.setBlock(xo + L / 2, yo + 2, zo, 0)
    #玻璃
    for z in range(2):
        for y in range(2):
            mc.setBlock(xo + L - 1, yo + y + 2, zo + (W - 2) / 2 + z,
                        20)


#屋顶花纹
    shoufig(xo + (L - 5) / 2,yo, zo + (W - 6) / 2,L, W, H,  num=fig)

i=0
for a in range(3):
    for b in range(3):
        for c in range(3):
            i+=1
            build(pos.x+20*c, pos.y+20*a, pos.z+20*b, 10+2*c, 10+2*b, 10+2*a, i, i)
