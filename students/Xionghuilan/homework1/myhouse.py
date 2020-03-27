import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))

def huawen(xo, yo, zo,L,W,H,num):
        if num >= 0 and num <= 27:
            path = "roof" + str(num) + ".csv"
            
            f = open(path,'r',encoding='utf-8')
            lines = f.readlines()
            a = W-1
            b = 0
            for line in lines:
                data = line.split(",")
                for cell in data:
                    if cell == "1" or cell == "1\n":
                        mc.setBlock(xo+a,yo+H-1,zo+b,35)
                    b = b+1
                a = a-1
                b = 0

def house(x0,y0,z0,L,W,H,f,num):	#原点（x0，y0，z0）,材质：f
    
    ##地板
    for x in range(W):
        for z in range(L):
            mc.setBlock(x0+x,y0,z0+z,f)
    # 平行墙
    for y in range(1,H):
        for a in range(1,W):
            mc.setBlock(x0+a, y0+y, z0, f)
        for a in range(1,L):
            mc.setBlock(x0+W-1, y0+y, z0+a, f)
        for a in range(1,W):
            mc.setBlock(x0+W-1-a, y0+y, z0+L-1, f)
        for a in range(1,L):
            mc.setBlock(x0, y0+y, z0+L-1-a, f)
    ##屋顶
    for x in range(W):
        for z in range(L):
            mc.setBlock(x0+x,y0+H-1,z0+z,f)
    ##门
    for y in range(2):
        mc.setBlock(x0+int(W/2),y0+1+y,z0,0)
    ##窗
    for y in range(2):
        for z in range(2):
            mc.setBlock(x0+W-1,y0+int(H/2)+y,z0+int(L/2)+z,160)
		     
    huawen(x0,y0,z0,L,W,H,num)
		     

l = 10
w = 10
h = 10
##x0 = pos.x
##y0 = pos.y
##z0 = pos.z
x0 = 0
y0 = 0+10
z0 = 0
mc.player.setTilePos([x0+50,y0,z0])
i = 220
j = 1
for X in range(3):
    for Y in range(3):
        for Z in range(3):
            house(x0+3*l*X,y0+3*h*Y,z0+3*w*Z,l,w,h,i,j)
            i = i +1
            j = j +1
			


