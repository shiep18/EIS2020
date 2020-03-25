import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
down=[6,8,9,10,11,12,13,18,26,27,20]
def house(x0,y0,z0,L,W,H,M,TXT):
    for ii in down:
        if ii == M:
            M = 56
    for y in range(H):                                     #砌墙   
        for a in range(L):
            mc.setBlock(x0+a, y0+y, z0, M)
            mc.setBlock(x0+a, y0+y, z0+L-1,M)
        for a in range(W-1):
            mc.setBlock(x0, y0+y, z0+1+a, M)
            mc.setBlock(x0+W-1, y0+y, z0+1+a,M)
    for z in range(3):                                      #窗
      for y in range(3): 
            mc.setBlock(x0+L-1, y0+y+2, z0+z+3, 102)
    ggg=csv.reader(open(str(TXT)+'.txt'))                   #屋顶
    r= list(ggg)
    for x in range(L):
        for z in range(W):
            if r[x][z]=="0":
                mc.setBlock(x0+x,y0+H,z+z0, 56)
            else:
                mc.setBlock(x0+x,y0+H,z+z0,41)
i=0
j=0
for a in range(3):
    for b in range(3):
        for c in range(3):
            i+=1
            j+=1
            house(pos.x+20*c, pos.y+20*a, pos.z+20*b, 9, 9, 6, i, j)
