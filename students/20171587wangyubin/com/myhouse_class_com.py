import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import time
import serial
import serial.tools.list_ports
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
ser=serial.Serial(port='COM3')
def shoufig(xo=pos.x, yo=pos.y, zo=pos.z, L=10, W=10, H=10, num=1):
    if num >= 0 and num <= 1:
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

class House:
    def __init__(self,xo,yo,zo,L=10,W=10,H=10,M=1,fig=1):
        self.xo=xo
        self.yo=yo
        self.zo=zo
        self.L=L
        self.W=W
        self.H=H
        self.M=M
        self.fig=fig
    def buildhouse(self):
        #流动、掉落的方块
        for i in [6,8,9,10,11,12,13,18,26,1]:
            if i == self.M:
                self.M = 169 
    #墙
        for y in range(self.H):
            for x in range(self.L):
                mc.setBlock(self.xo + x, self.yo + y, self.zo, self.M)
                mc.setBlock(self.xo + x, self.yo + y, self.zo + self.W - 1, self.M)
            for z in range(self.W - 2):
                mc.setBlock(self.xo, self.yo + y, self.zo + 1 + z, self.M)
                mc.setBlock(self.xo + self.L - 1, self.yo + y, self.zo + 1 + z, self.M)
    #屋顶地板
        for x in range(self.L):
            for z in range(self.W):
                mc.setBlock(self.xo + x, self.yo, self.zo + z,self. M)
                mc.setBlock(self.xo + x, self.yo + self.H - 1, self.zo + z, 35, 0)
    #照明（海晶灯）
        for x in range(2):
            for z in range(2):
                mc.setBlock(self.xo + x + (self.L - 2) / 2, self.yo,
                            self.zo + (self.W - 2) / 2 + z, 169)
                mc.setBlock(self.xo + x + (self.L - 2) / 2, self.yo + self.H - 2,
                            self.zo + (self.W - 2) / 2 + z, 169)
                mc.setBlock(self.xo, self.yo + 4 + x, self.zo + (self.W - 2) / 2 + z, 169)

    #门
        mc.setBlock(self.xo + self.L / 2, self.yo + 1, self.zo, 0)
        mc.setBlock(self.xo + self.L / 2, self.yo + 2, self.zo, 0)
        #玻璃
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.xo + self.L - 1, self.yo + y + 2, self.zo + (self.W - 2) / 2 + z,
                            20)
    #屋顶花纹
        shoufig(self.xo + (self.L - 5) / 2,self.yo, self.zo + (self.W - 6) / 2,self.L, self.W, self.H,  num=int(self.fig))
        
    def isinhouse(self,x0,y0,z0):
        if x0>=self.xo and y0>=self.yo and z0>=self.zo and x0<=self.xo+self.L and y0<=self.yo+self.H and z0<=self.zo+self.H:
            return 1
        else:
            return 0  

reader = csv.reader(open('info.csv'))              #读取csv房屋坐标等信息
data=[]
for r in reader:
    data.append(r)
for i in range(1):#只建一个房子就够
    for j in range(7):
        data[i][j+1]=int(data[i][j+1])
    data[i][0]=House(pos.x+data[i][1],pos.y+data[i][2],pos.z+data[i][3],data[i][4],data[i][5],data[i][6],data[i][7],data[i][8])
    data[i][0].buildhouse()


while True:
    pos = mc.player.getTilePos()            #重新获取坐标位置
    for i in range(1):
        ser.write(str(data[i][0].isinhouse(pos.x,pos.y,pos.z)).encode()) #返回0则全灭，返回1则全亮         
        time.sleep(1)#在家亮灯

