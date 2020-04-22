
import socket
import mcpi.minecraft as minecraft
import mcpi.block as block

s=socket.socket()
s.connect(('127.0.0.1',4711))
mc = minecraft.Minecraft.create()

print('connected')
while True :
    print('输入q退出，输入其他则在人物脚下放置3*3黄金方块')
    msg=input('>')
    pos = mc.player.getTilePos()
    if msg=='q':
        break
    for a in range(-1,2):
        for b in range(-1,2):
            cmd='world.setBlock('+str(pos.x+a)+','+str(pos.y-1)+','+str(pos.z+b)+',41)\r'
            s.send(cmd.encode("gbk"))
            
s.close()
