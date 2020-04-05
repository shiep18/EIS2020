import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
class House:
    def __init__(self,x0,y0,z0,L,W,H,M):
        self.x0=x0
        self.y0=y0
        self.z0=z0
        self.L=L
        self.W=W
        self.H=H
        self.M=M
    def house(self):
        for y in range(self.H):                                     #砌墙   
            for a in range(self.L):
                mc.setBlock(self.x0+a, self.y0+y, self.z0, self.M)
                mc.setBlock(self.x0+a, self.y0+y, self.z0+self.L-1,self.M)
            for a in range(self.W-1):
                mc.setBlock(self.x0,self. y0+y, self.z0+1+a, self.M)
                mc.setBlock(self.x0+self.W-1, self.y0+y, self.z0+1+a,self.M)
        a=self.L//8                                                     #根据房屋大小开窗
        while a>0:
            for c in range(a):
                for cc in range(a):
                    for z in range(3):
                        for y in range(3):
                            mc.setBlock(self.x0+self.L-1, self.y0+y+3+c*7, self.z0+z+3+cc*7, 102)
            a-=1                   
        for x in range(self.L):                                     #屋顶
            for z in range(self.W):
                mc.setBlock(self.x0+x,self.y0+self.H,z+self.z0, self.M)
    def where(self):                                                 #位置判断
            if self.L>=pos.x-self.x0 and self.W>=pos.z-self.z0 and self.H>=pos.y-self.y0:
                return True
            else:
                return False
            
c=csv.reader(open('houses.csv'))               
r= list(c)
for x in range(10):
    built=House(pos.x+int(r[x][1]),pos.y+int(r[x][2]),pos.z+int(r[x][3]),int(r[x][4]),int(r[x][5]),int(r[x][6]),int(r[x][7]))
    built.house()

    
    


