print("hello")
import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create('47.100.46.95',4785)

fname = "pos.csv"
f = open(fname, "r")
for line in f.readlines():
    data = line.split(",")
    for cell in data:
        if cell == "clancenter":
            center_x=data[1]
            center_y=data[2]
            center_z=data[3]
        elif cell == "ly":
            offset_x=data[1]
            offset_y=data[2]
            offset_z=data[3]
x=int(center_x)+int(offset_x)
y=int(center_y)+int(offset_y)
z=int(center_z)+int(offset_z)
def build(xo=0, yo=0, zo=0, L=41, W=41, H=2, M=155):

    for y in range(H):
        for x in range(L):
            mc.setBlock(xo + x, yo + y, zo, M)
            mc.setBlock(xo + x, yo + y, zo + W - 1, M)
        for z in range(W - 2):
            mc.setBlock(xo, yo + y, zo + 1 + z,M)
            mc.setBlock(xo + L - 1, yo + y, zo + 1 + z, M)
#....
    for x in range(L):
        for z in range(W):
            mc.setBlock(xo + x, yo, zo + z, M)
            mc.setBlock(xo + x, yo + H - 1, zo + z, 0, 49)
#.......
    for x in range(2):
        for z in range(2):
            mc.setBlock(xo + x + (L - 2) / 2, yo,zo + (W - 2) / 2 + z, 0)
            mc.setBlock(xo, yo + 4 + x, zo + (W - 2) / 2 + z,0)

#.
    mc.setBlock(xo + L / 2, yo + 1, zo,0)
    mc.setBlock(xo + L / 2, yo + 2, zo, 0)
    #..
    for z in range(2):
        for y in range(2):
            mc.setBlock(xo + L - 1, yo + y + 2, zo + (W - 2) / 2 + z,0)




build(x, y, z)

