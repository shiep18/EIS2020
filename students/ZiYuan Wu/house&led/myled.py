from mcpi.minecraft import Minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
print (ports)

ser=serial.Serial(port='COM3')
time.sleep(2)
mc=Minecraft.create()
pos = mc.player.getTilePos()
stayed_time=0


def buildhouse(x0,y0,z0,L,W,H,M):
    for y in range(H):
        for x in range(L):
            mc.setBlock(x0+x,y0+y,z0,M)
            mc.setBlock(x0+x,y0+y,z0+W-1,M)
        for z in range(W):
            mc.setBlock(x0,y0+y,z0+z,M)
            mc.setBlock(x0+L-1,y0+y,z0+z,M)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x, y0+H-1, z0+z,block.TNT.id)
            mc.setBlock(x0+x, y0, z0+z,block.TNT.id)   #建地板

    mc.setBlock(x0+int(L/2), y0+1, z0,block.DOOR_WOOD.id) #门
    mc.setBlock(x0+int(L/2), y0+2, z0,block.DOOR_WOOD.id)

    for z in range(2):
        for y in range(2): 
            mc.setBlock(x0+L-1,y0+y+2,z0+z+4,20) #窗


def isInhouse(x,y,z,L,W,H):
        pos = mc.player.getTilePos()
        x0,y0,z0 = pos.x,pos.y,pos.z
        if x <= x0 <= x+L and y <= y0 <= y+H and z <= z0 <= z+W:
            return True
        else:
            return False


buildhouse(72,-2,43,10,10,6,1)
#print(pos.x,pos.y,pos.z)
k = 0
while True:
    time.sleep(0.5)
    #pos=mc.player.getTilePos()
    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if isInhouse(72,-2,43,10,10,6):
        if k == 1:
            mc.postToChat("Welcome home")
            ser.write("0".encode())
            print("0 SEND")
        k = 0
 
    else :
        if k == 0:
            mc.postToChat("goodbye")
            ser.write("1".encode())
            print("1 SEND")
        k = 1