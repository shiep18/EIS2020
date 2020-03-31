import mylogo as logo
import mypic as pic
from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
pic.showpic()
logo.mylogo()
mc.setBlock(pos.x-50,pos.y+25,pos.z,35,15)
mc.player.setTilePos([pos.x-50,pos.y+26,pos.z])
