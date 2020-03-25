import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

for y in range(10):
    for a in range(10):
        mc.setBlock(pos.x+a, pos.y+y, pos.z, block.STONE.id)
        mc.setBlock(pos.x+a, pos.y+y, pos.z+9, block.STONE.id)
    for a in range(8):
        mc.setBlock(pos.x, pos.y+y, pos.z+1+a, block.STONE.id)
        mc.setBlock(pos.x+9, pos.y+y, pos.z+1+a, block.STONE.id)





