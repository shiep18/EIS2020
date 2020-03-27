import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import random

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def cratcsv(a):
    for i in range(1,a+1):
        with open('%d.csv'%i, "w", newline='') as f:
            csv_writer = csv.writer(f)
            for j in range(10):
                l = []
                for m in range(10):
                    a = random.randint(0,1)
                    l.append(str(a))
                csv_writer.writerow(l)
            f.close()

def rooftop(xo=pos.x, yo=pos.y, zo=pos.z, num=1):
    fname =  str(num) + ".csv"
    f = open(fname, "r")
    offsetX = 0
    offsetZ = 0
    for line in f.readlines():
        data = line.split(",")
        for cell in data:
            if cell == "1" or cell == "1\n":
                mc.setBlock(xo + offsetX, yo + 9, zo + offsetZ,133)
            offsetZ = offsetZ + 1
        offsetX = offsetX + 1
        offsetZ = 0

def ahouse(x,y,z,l):
    for y0 in range(10):  #wall
        for a in range(10):
            mc.setBlock(x+a, y+y0, z, 79)
            mc.setBlock(x+a, y+y0, z+9, 79)
        for a in range(8):
            mc.setBlock(x, y+y0, z+1+a, 79)
            mc.setBlock(x+9, y+y0,z+1+a, 79)
    for x0 in range(10):   #floor
        for z0  in range(10):
            mc.setBlock(x+x0, y, z+z0, 80)
    for x0 in range(10):   #ceiling
        for z0  in range(10):
            mc.setBlock(x+x0, y+9, z+z0, 42)
    mc.setBlock(x+5, y+1, z,0)  #door
    mc.setBlock(x+5, y+2, z,0)
    mc.setBlock(x + 4, y + 1, z, 0)  # door
    mc.setBlock(x + 4, y + 2, z, 0)
    for z0 in range(2):    #windows
        for y0 in range(2):
            mc.setBlock(x+9, y+y0+2,z+z0+4, 20)
    for z0 in range(2):    #windows
        for y0 in range(2):
            mc.setBlock(x, y+y0+2,z+z0+4, 20)
    for x0 in range(2):    #windows
        for y0 in range(2):
            mc.setBlock(x+x0+2, y+y0+6,z, 20)
    for x0 in range(2):    #windows
        for y0 in range(2):
            mc.setBlock(x+x0+6, y+y0+6,z, 20)
    rooftop(x,y,z,l)


i=0
cratcsv(27)
for a in range(3):
    for b in range(3):
        for c in range(3):
            i+=1
            ahouse(pos.x+20*c, pos.y+20*a, pos.z+20*b,i)