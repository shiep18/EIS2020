from mylogo import mylogo
from showmypic import mcsimg
from mcpi.minecraft import Minecraft

mc=Minecraft.create()
pos=mc.player.getTilePos()

mylogo(pos.x,pos.y,pos.z)
mcsimg(pos.x,pos.y,pos.z+32,'github.jpg',32,32)