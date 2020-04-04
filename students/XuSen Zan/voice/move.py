import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
from time import *
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def move(dir):
    if dir == "left":
        for i in range(6):
            mc.player.setPos(pos.x+i,pos.y,pos.z)
            sleep(0.1)
    elif dir == "right":
        for i in range(6):
            mc.player.setPos(pos.x-i,pos.y,pos.z)
            sleep(0.1)
    elif dir == "front":
        for i in range(6):
            mc.player.setPos(pos.x,pos.y,pos.z+i)
            sleep(0.1)
    elif dir == "back":
        for i in range(6):
            mc.player.setPos(pos.x,pos.y,pos.z-i)
            sleep(0.1)
    elif dir == "up":
        for i in range(6):
            mc.player.setPos(pos.x,pos.y+i,pos.z)
            sleep(0.1)
    else :
        for i in range(6):
            mc.player.setPos(pos.x,pos.y-i,pos.z)
            sleep(0.1)