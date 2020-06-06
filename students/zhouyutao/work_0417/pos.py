from mcpi.minecraft import Minecraft
import mcpi.block as block
mc=Minecraft.create()
#mc=Minecraft.create("172.25.71.1",4711)
import time
while True:
    pos=mc.player.getTilePos()
    with open('pos.html', 'w') as f:
            f.write(f'<div>{pos.x},{pos.z}</div><title>{pos.x},{pos.z}</title>')
    time.sleep(0.5)
