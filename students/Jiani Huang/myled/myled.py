import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
import csv
import serial
import serial.tools.list_ports
import time
#print("player pos is",pos)     #player pos is Vec3(108,2,-88)
class House:
    def __init__(self,x,y,z,l,w,h,num):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h
        self.num=num

    def house(self):
        mc.setBlocks(self.x,self.y-1,self.z,self.x+self.l,self.y+self.h-1,self.z+self.w,5,4)
        mc.setBlocks(self.x+1,self.y,self.z+1,self.x+self.l-1,self.y+self.h-2,self.z+self.w-1,0)   #建一个火柴盒
        mc.setBlocks(self.x+3,self.y+1,self.z,self.x+4,self.y+2,self.z,block.GLASS.id)#窗
        mc.setBlocks(self.x+6,self.y,self.z,self.x+6,self.y+1,self.z,64)              #门w
        reader = csv.reader(open(str(self.num)+'.csv'))                                      #屋顶
        data=[]
        for r in reader:
            data.append(r)
        for i in range(10):
            for j in range(10):
                if (data[j][i]=='1'):
                    mc.setBlock(self.x+i,self.y+5,self.z+j,79)

    def isInHouse(self,x0,y0,z0):
        if self.x<=x0<=self.x+self.l and self.y<=y0<=self.y+self.h and self.z<=z0<=self.z+self.w:
            return True
        else:
            return False

ports = list(serial.tools.list_ports.comports())
print (ports)

ser=serial.Serial(port='COM2')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

mc = minecraft.Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
stayed_time=0
reader = csv.reader(open('house.csv'))
data=[]
name=[]
for r in reader:
    data.append(r)
for i in range(27):
    name.append(data[i][0])
    for j in range(7):
        data[i][j+1]=int(data[i][j+1])
    data[i][0]=House(data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7])
    #data[i][0].house()
def inwhichhouse():
    pos = mc.player.getTilePos()
    for i in range(27):
        if data[i][0].isInHouse(pos.x,pos.y,pos.z):
            mc.postToChat("welcome to "+name[i]+"'s house")
            return True
            break
        else:
            None
while True:
    time.sleep(0.5)
    pos = mc.player.getTilePos()            #重新获取坐标位置
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if inwhichhouse():
        ser.write("y".encode())
        print("y send")
        time.sleep(1)
    else:
        mc.postToChat("byebye")
        ser.write("g".encode())
        print("g send")
        time.sleep(1)