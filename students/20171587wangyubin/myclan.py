import mylogo as logo
import shoumypic as pic
from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
pic.showmypic("mypic.jpg")
logo.logo("mylogo.binvox")