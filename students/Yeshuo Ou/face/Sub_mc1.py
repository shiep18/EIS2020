import MXMqtt as MXMqtt
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# 初始化MQTT
MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt.MXMqtt(MQTTHOST,MQTTPORT)

# 初始化Minecaft
mc = minecraft.Minecraft.create('47.100.46.95',4781)
entityId= mc.getPlayerEntityId("OYS")
pos=mc.entity.getTilePos(entityId)

# 初始化参数
mqtt.SUB("MC")
print('MC')
act = 0
x0 = pos.x
y0 = pos.y
z0 = pos.z
m = 'CloseDoor'

def doors(x,y,z,L,act):
        
        if act :
                m = block.AIR.id
                mc.postToChat("DoorOpened")
                for y1 in range(3):
                        for z1 in range(2):
                                mc.setBlock(x+int(L/2), y+y1, z+z1,m) #门
                for y1 in range(3):
                        for z1 in range(2):
                                mc.setBlock(x+int(L/2), y+y1, z-z1,m) #门
        else :
                m = block.GLASS.id
                mc.postToChat("DoorClosed")
                for y1 in range(4):
                        for z1 in range(3):
                                mc.setBlock(x+int(L/2), y+y1, z+z1,m) #门
                for y1 in range(4):
                        for z1 in range(3):
                                mc.setBlock(x+int(L/2), y+y1, z-z1,m) #门
    

def isInhouse(x,y,z):
        global act
        pos = mc.player.getTilePos()
        entityId= mc.getPlayerEntityId("OYS")#更改用户时需要改
        pos=mc.entity.getTilePos(entityId)
        x0,y0,z0 = pos.x,pos.y,pos.z
        
        if x-1 <= x0 <= x+10 and y-3 <= y0 <= y+3 and z-2 <= z0 <= z+2:
                mc.postToChat("act=1")
                act = 1
                return True
        else :
                mc.postToChat("act=0")
                act = 0
                return False

               
while True:
   msg = mqtt.returnMsg()
   if msg:
           m = str(msg[0])
           print(m)
           isInhouse(-425,-1,-375)
           if m == 'OpenDoor' and act == 1:
              doors(-425,-1,-375,10,1)
           elif m == 'CloseDoor' or act == 0:
              doors(-425,-1,-375,10,0)
      

     
   
