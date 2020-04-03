import mcpi.minecraft as minecraft
import mcpi.block as block
import pyautogui as auto

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
auto.PAUSE=1

def clean():
    pos = mc.player.getTilePos()
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mc.setBlock(pos.x-1+i,pos.y-1+j,pos.z-1+k,0)

def go_forward():
    for i in range(1):
 #       mc.player.setPos(pos.x+i,pos.y,pos.z)
        auto.keyDown("w")
        auto.keyUp("w")
        clean()
def go_backward():
    for i in range(1):
  #      mc.player.setPos(pos.x-i,pos.y,pos.z)
        auto.keyDown("s")
        auto.keyUp("s")
        clean()
def go_left():
    for i in range(1):
   #     mc.player.setPos(pos.x,pos.y,pos.z-i)
        auto.keyDown("a")
        auto.keyUp("a")
        clean()
def go_right():
    for i in range(1):
  #      mc.player.setPos(pos.x,pos.y,pos.z+i)
        auto.keyDown("d")
        auto.keyUp("d")
        clean()

def build(length=0):
    pos = mc.player.getTilePos()
    for i in range(1,length+1):
        if i%5 == 0:
            mc.setBlock(pos.x,pos.y+i,pos.z,169)
        else:
            mc.setBlock(pos.x,pos.y+i,pos.z,1)

