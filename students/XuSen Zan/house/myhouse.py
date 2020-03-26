import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

def house():
       material = ['1','17','5','41','45','57','80','91','155','133']#10
       ran = random.randint(0,9)
       mc.setBlocks(x,y,z,x+SIZE,y+SIZE-1,z+SIZE,int(material[ran]))#随机方块房子
       mc.setBlocks(x+1,y+1,z+1,x+SIZE-1,y+SIZE-2,z+SIZE-1,0)#空心
       mc.setBlocks(x,y+1,z+3,x,y+3,z+4,0)#开门
       mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,0)#拆屋顶
       for i in range(0,SIZE+1):
              for j in range(0,SIZE+1):
                     roof = random.randint(0,27)
                     mc.setBlock(x+i,y+SIZE-1,z+j,35,roof)#花屋顶
       mc.setBlocks(x,y+5,z+1,x,y+6,z+8,20)#开窗户
       mc.setBlocks(x+SIZE,y+5,z+1,x+SIZE,y+6,z+8,20)#开窗户
       mc.setBlock(x+(SIZE//2),y,z+(SIZE//2),89)


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
       
