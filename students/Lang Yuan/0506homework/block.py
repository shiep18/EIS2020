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
def build(xo=0, yo=0, zo=0, L=27, W=27, H=1, M=0):

    for y in range(H):
        for x in range(L):
            for z in range (W):
                 mc.setBlock(xo +x-1, yo + y, zo-z-1, M)




build(x, y, z)

