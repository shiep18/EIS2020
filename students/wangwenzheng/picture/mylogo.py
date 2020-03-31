import binvox_rw
from mcpi.minecraft import Minecraft
import mcpi.block as block


mc=Minecraft.create()
pos=mc.player.getTilePos()

def mylogo():
    with open('mylogo.binvox', 'rb') as f:
        model = binvox_rw.read_as_3d_array(f)
    print(model.dims)
    print(model.scale)
    print(model.translate)
    #print(model.data)

    for y in range(model.dims[1]):
        print("layer y=",y)
        layer_data=model.data[y]
        stringlayer=""
        for x in range(model.dims[0]):
            stringlayer=stringlayer+"\n"
            for z in range(model.dims[2]):
                if model.data[x][y][z] == True:
                    stringlayer=stringlayer+'1'
                    mc.setBlock(pos.x+x,pos.y+y+10,pos.z+z,block.STONE.id)
                else:
                    stringlayer=stringlayer+'0'
                    mc.setBlock(pos.x+x,pos.y+y+10,pos.z+z,block.AIR.id)
        print(stringlayer)

    

   
