import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
# pos = mc.player.getTilePos()
lens = 10


def mcgo(dir):
    direction = mc.player.getDirection()
    pos = mc.player.getTilePos()
    if dir == "strange":
        x = pos.x + (direction.x * lens)
        z = pos.z + (direction.z * lens)
    elif dir == "back":
        x = pos.x + (direction.x * (-1 * lens))
        z = pos.z + (direction.z * (-1 * lens))
    elif dir == "right":
        x = pos.x + (direction.z * (-1 * lens))
        z = pos.z + (direction.x * lens)
    elif dir == "left":
        x = pos.x + (direction.z * lens)
        z = pos.z + (direction.x * (-1 * lens))
    mc.player.setPos(x, pos.y, z)


def temStone(tem):
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x - 2, pos.y, pos.z + 8, pos.x + 2, pos.y + 30, pos.z + 12, 0)
    for i in range(eval(tem)):
        mc.setBlock(pos.x, pos.y + i, pos.z + 10, 35, 0)
        if i % 5 == 0:
            mc.setBlock(pos.x, pos.y + i, pos.z + 10, 35, 1)
