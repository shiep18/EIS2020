import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

lens = 10
def Set(tem):
    pos = mc.player.getTilePos()
    # direction = mc.player.getDirection()
    for i in range(tem):
        mc.setBlock(pos.x, pos.y + i, pos.z + 10, 35, 0)

def Move(dir):
    direction = mc.player.getDirection()
    pos = mc.player.getTilePos()
    if dir == "Strange":
        x = pos.x + (direction.x * lens)
        z = pos.z + (direction.z * lens)
    elif dir == "Backword":
        x = pos.x + (direction.x * (-1 * lens))
        z = pos.z + (direction.z * (-1 * lens))
    elif dir == "Right":
        x = pos.x + (direction.z * (-1 * lens))
        z = pos.z + (direction.x * lens)
    elif dir == "Left":
        x = pos.x + (direction.z * lens)
        z = pos.z + (direction.x * (-1 * lens))
    mc.player.setPos(x, pos.y, z)
