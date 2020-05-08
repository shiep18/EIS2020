from mcpi.minecraft import Minecraft
import time
import csv

mc =Minecraft.create('47.100.46.95',4782)

with open('site.csv',"r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows=[row for row in reader]
    for a in range(6):
        if rows[a]["name"] == "center":
            x = rows[a]["x"]
            print(x)
            y = rows[a]["y"]
            print(y)
            z = rows[a]["z"]
            print(z)
        if rows[a]["name"] == "zkx":
            xx = rows[a]["x"]
            yy = rows[a]["y"]
            zz = rows[a]["z"]
    x = int(x) + int(xx)
    y = int(y) + int(yy)
    z = int(z) + int(zz)


mc.setBlocks(x, y, z, x + 10, y + 7, z + 10, 79)
mc.setBlocks(x + 1, y + 1, z + 1, x + 6, y + 9, z + 9, 0)

