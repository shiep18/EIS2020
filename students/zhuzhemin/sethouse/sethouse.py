import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
jilu=0
jilux=[]
jiluy=[]
jiluz=[]
jilul=[]
jiluh=[]
jiluw=[]
class House:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.l=8
        self.w=8
        self.h=8

    def setbuild(self,x,y,z,l,w,h):
        global pos
        global jilu
        global jilux
        global jiluy
        global jiluz
        global jilul
        global jiluh
        global jiluw

        self.x=x+pos.x
        self.y=y+pos.y
        self.z=z+pos.z
        self.l=l
        self.w=w
        self.h=h
        jilux.append(self.x)
        jiluy.append(self.y)
        jiluz.append(self.z)
        jilul.append(self.l)
        jiluw.append(self.w)
        jiluh.append(self.h)
        jilu+=1
        for i in range(l):
            for j in range(w):
                for k in range(h-1):
                    mc.setBlock(self.x+i,self.y+k,self.z+j,block.GLASS.id)
        for i in range(l-2):
            for j in range(w-2):
                for k in range(h-2):
                    mc.setBlock(self.x+i+1,self.y+k+1,self.z+j+1,block.AIR.id)
        for i in range(l):
            for j in range(w):
                mc.setBlock(self.x+i,self.y+h-1,self.z+j,block.GOLD_BLOCK.id)
        for i in range(l):
            for j in range(w):
                mc.setBlock(self.x+i,self.y+h,self.z+j,block.AIR.id)
        print("I will build a house here,x y z l w h is ",self.x,self.y,self.z,self.l,self.w,self.h)

    def isInHouse(self,x0,y0,z0):
        global pos
        global jilux
        global jiluy
        global jiluz
        global jilul
        global jiluh
        global jiluw
        self.x0=pos.x
        self.y0=pos.y
        self.z0=pos.z

        for i in range(27):
            print(jilux[i],jiluy[i],jiluz[i],jilul[i],jiluh[i],jiluw[i])
            if jilux[i]<=self.x0<=jilux[i]+jilul[i] and jiluy[i]<=self.y0<=jiluy[i]+jiluh[i] and jiluz[i]<=self.z0<=jiluz[i]+jiluw[i]:
                return True
        return False
        

    def set(self,num):
        self.num=num
        if num > 0 and num <= 27:
            fname = "t" + str(num) + ".csv"
            f = open(fname, "r")  
            ff=csv.reader(f)      
            for lines in ff:
                f1=lines
            return f1

    def showfig(self,num0):
        global jilux
        global jiluy
        global jiluz
        global jilul
        global jiluh
        global jiluw
        self.num0=num0
        if num0 > 0 and num0 <= 27:
            fname = "fig" + str(num0) + ".csv"
            f = open(fname, "r")
#显示5*7的图案，因为读数据是从上至下，所以offsetX为4，先扫Z轴，再扫X轴，Y轴不变
            offsetX = 4
            offsetZ = 0
            for line in f.readlines():
                data = line.split(",")
                for cell in data:
                    if cell == "1" or cell == "1\n":
                        mc.setBlock(jilux[self.num0-1] + offsetX+2, jiluy[self.num0-1]+jiluh[self.num0-1]-1, jiluz[self.num0-1] + offsetZ+1,block.DIAMOND_BLOCK.id)
                    offsetZ = offsetZ + 1
                offsetX = offsetX-1
                offsetZ = 0


myhouse=House(10,10,10)
a=[]
for p in range(27):
    print(myhouse.set(p+1))
    for i in range(6):
        a.append(int(myhouse.set(p+1)[i+1]))
    print(a)
    myhouse.setbuild(a[0],a[1],a[2],a[3],a[4],a[5])
    myhouse.showfig(p+1)
    a.clear()
while True:
    b=input("想知道你在房子里嘛？按1\n退出。按2\n")
    if b=="1":
        pos = mc.player.getTilePos()
        print(pos.x,pos.y,pos.z)
        print(myhouse.isInHouse(pos.x,pos.y,pos.z))
        b=""
    elif b=="2":
        break
