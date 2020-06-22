from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create("47.100.46.95",4783)
entityId= mc.getPlayerEntityId("LT")
pos=mc.entity.getPos(entityId)
print("player pos is",pos)

while True:
    time.sleep(2)
    pos=mc.entity.getTilePos(entityId)
    mc.postToChat("LT:"+"x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

     
