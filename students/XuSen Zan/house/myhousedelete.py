import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
def house():
       mc.setBlocks(x,y,z,x+SIZE,y+SIZE-1,z+SIZE,0)#删除方块房子


y = pos.y - 45 
SIZE = 9
for height in range(3):
       y = y + 20
       z = pos.z - 45
       x = pos.x - 45
       for row in range(3):
              z = z + 20
              x = pos.x
              for line in range(3):
                     x = x + 20
                     house()
-593 157 -528
