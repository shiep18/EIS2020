import mcpi.minecraft as minecraft
import mcpi.block as block
from classhouse import House
import serial
import serial.tools.list_ports
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

ports = list(serial.tools.list_ports.comports())
print (ports)
ser=serial.Serial(port='COM1')
time.sleep(2)

myhouse = House("myhouse",pos.x+3,pos.y,pos.z+3,10,10,10)
myhouse.buildhouse()

while True:
    pos = mc.player.getTilePos()
    time.sleep(0.5)
    #mc.postToChat("x:" + str(pos.x) + "y:" + str(pos.y) + "z:" + str(pos.z))
    #print(myhouse.isinhouse(pos.x,pos.y,pos.z))
    if myhouse.isinhouse(pos.x,pos.y,pos.z):
        ser.write("0".encode())
    else :
        ser.write("1".encode())
        print("no")

