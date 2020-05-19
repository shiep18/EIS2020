import binvox_rw
from mcpi.minecraft import Minecraft
import mcpi.block as block

def SetSans(X,Y,Z):
    with open('Sans.binvox', 'rb') as f:
        model = binvox_rw.read_as_3d_array(f)

    for y in range(model.dims[1]):
        layer_data=model.data[y]
        stringlayer=""
        for x in range(model.dims[0]):
            stringlayer=stringlayer+"\n"
            for z in range(model.dims[2]):
                if model.data[x][y][z] == True:
                    stringlayer=stringlayer+'1'
                    mc.setBlock(X+x,Y+y,Z+z,49)
                else:
                    stringlayer=stringlayer+'0'
                    mc.setBlock(X+x,Y+y,Z+z,0)

mc=Minecraft.create()
pos=mc.player.getTilePos()
