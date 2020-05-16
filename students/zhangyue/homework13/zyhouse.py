# UTF-8
import mcpi.minecraft as minecraft
import random

mc = minecraft.Minecraft.create('47.100.46.95', 4785)

fname = "pos.csv"
f = open(fname, "r")
for line in f.readlines():
    data = line.split(",")
    for cell in data:
        if cell == "clancenter":
            center_x = data[1]
            center_y = data[2]
            center_z = data[3]
        elif cell == "zy":
            offset_x = data[1]
            offset_y = data[2]
            offset_z = data[3]
x1 = int(center_x) + int(offset_x)
y1 = int(center_y) + int(offset_y)
z1 = int(center_z) + int(offset_z)


def house(x0, y0, z0, L, W, H, M):
    mc.setBlocks(x0, y0, z0, x0 + L, y0 + H, z0 + W, 0)
    mc.setBlocks(x0, y0, z0, x0 + L - 1, y0 + H - 1, z0 + W - 1, M)
    mc.setBlocks(x0 + 1, y0 + 1, z0 + 1, x0 + L - 2, y0 + H - 2, z0 + W - 2, 0)
    for z in range(W):  # 天花板、地板
        for x in range(L):
            mc.setBlock(x0 + x, y0 + H - 1, z0 + z, (251, random.randint(0, 35)))
    mc.setBlocks(x0 + 5, y0 + 1, z0, x0 + 5, y0 + 2, z0, 0)
    mc.setBlocks(x0 + 9, y0 + 2, z0 + 5, x0 + 9, y0 + 3, z0 + 6, 20)


house(x1, y1, z1, 10, 10, 10, 251)
