import binvox_rw
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc=Minecraft.create()

with open('mylogo.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)

print(model.dims)
print(model.scale)
print(model.translate)
#print(model.data)

while True:
    pos=mc.player.getTilePos()    
    for y in range(model.dims[1]):
        print("layer y=",y)
        layer_data=model.data[y]
        stringlayer=""
        for x in range(model.dims[0]):
            stringlayer=stringlayer+"\n"
            for z in range(model.dims[2]):
          #      print("s")
                if model.data[x][y][z] == True:
                    stringlayer=stringlayer+'1'
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.GLOWSTONE_BLOCK.id)
                    time.sleep(0.1)
                else:
                    stringlayer=stringlayer+'0'
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.AIR.id)
    for y in range(model.dims[1]):
        print("layer y=",y)
        layer_data=model.data[y]
        stringlayer=""
        for x in range(model.dims[0]):
            stringlayer=stringlayer+"\n"
            for z in range(model.dims[2]):
           #     print("c")
                if model.data[x][y][z] == True:
                    stringlayer=stringlayer+'1'
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.AIR.id)
                    time.sleep(0.1)
                else:
                    stringlayer=stringlayer+'0'
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.AIR.id)

