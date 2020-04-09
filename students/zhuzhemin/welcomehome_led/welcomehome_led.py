from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
print (ports)

ser=serial.Serial(port='COM12')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
case=0
case1=0
case2=0
case3=0
case4=0
stayed_time=0

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if (pos.x==-22 and pos.y==19 and pos.z==-35)&(case==0):
        case1=1
    elif (pos.x==-22 and pos.y==19 and pos.z==-34)&(case==0):
        case2=1
    elif (pos.x==-22 and pos.y==19 and pos.z==-36)&(case==0):
        case3=1 
    elif (pos.x==-22 and pos.y==19 and pos.z==-37)&(case==0):
        case5=1 
    elif ((pos.x==-22 and pos.y==19 and pos.z==-35)|(pos.x==-22 and pos.y==19 and pos.z==-34)|(pos.x==-22 and pos.y==19 and pos.z==-36)|(pos.x==-22 and pos.y==19 and pos.z==-37))&((case==1)):
        case1=0
        case2=0
        case3=0
        case4=0
        case5=0
        case=0
        #回到家给串口送一个8，arduino收到串口关led0
        ser.write("8".encode())
        print("8 send")
        time.sleep(1)
    if ((pos.x==-22 and pos.y==19 and pos.z==-33)|(pos.x==-22 and pos.y==19 and pos.z==-32))&(case==0)&((case1==1)|(case2==1)|(case3==1)):
        case=1
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        #回到家给串口送一个1，arduino收到串口点亮led0
        ser.write("0".encode())
        print("0 send")
        time.sleep(1)       
    else:
        stayed_time=0
        
     
