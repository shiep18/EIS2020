from mcpi.minecraft import Minecraft
import mylogo
import showmypic

mc=Minecraft.create()
pos=mc.player.getTilePos()

mylogo.getlogo()
showmypic.getpic()