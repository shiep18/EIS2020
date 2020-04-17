import mcpi.minecraft as minecraft
import mcpi.block as block
import pyautogui as auto

mc = minecraft.Minecraft.create()
auto.PAUSE=1

def clean():
    pos = mc.player.getTilePos()
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                mc.setBlock(pos.x-1+i, pos.y+j, pos.z-1+k,0)
                mc.setBlock(pos.x-1+i, pos.y+2, pos.z-1+k,1)
                mc.setBlock(pos.x-1+i, pos.y-1, pos.z-1+k,1)
def go_forward():
    auto.keyDown("w")
    auto.keyUp("w")
    clean()
def go_backward():
    auto.keyDown("s")
    auto.keyUp("s")
    clean()
def go_left():
    auto.keyDown("a")
    auto.keyUp("a")
    clean()
def go_right():
    auto.keyDown("d")
    auto.keyUp("d")
    clean()
    

def MoveIt(dx,dy,X,Y):
    if X / 3 < dx < X*2/3 and dy < Y/3:
        go_forward()
    elif X / 3 < dx < X*2/3 and dy > Y*2/3:
        go_backward()
    elif Y / 3 < dy < Y*2/3 and dx < X/3:
        go_left()
    elif Y / 3 < dy < Y * 2 / 3 and dx > X*2/3:
        go_right()
if __name__=='__main__':
    for i in range(5):
        go_forward()

























