from MyLogo import *
from ShowMyPic import *
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
pos=mc.player.getTilePos()

SetPic(pos.x-5,pos.y-10, pos.z-5)
SetSans(pos.x+50,pos.y-20, pos.z+50)
