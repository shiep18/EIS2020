import mcpi.minecraft as minecraftimport mcpi.block as blockimport csvfrom time import *mc = minecraft.Minecraft.create()pos = mc.player.getTilePos()def move(dir):    if dir == "left":        mc.player.setPos(pos.x-5,pos.y,pos.z)    elif dir == "right":        mc.player.setPos(pos.x+5,pos.y,pos.z)    elif dir == "front":        mc.player.setPos(pos.x,pos.y,pos.z+5)    elif dir == "back":        mc.player.setPos(pos.x,pos.y,pos.z-5)    elif dir == "up":        mc.player.setPos(pos.x,pos.y+5,pos.z)    else :        mc.player.setPos(pos.x,pos.y-5,pos.z)