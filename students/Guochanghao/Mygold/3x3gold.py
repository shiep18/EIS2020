import socket
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

s=socket.socket()
s.connect(('127.0.0.1',4711))

print('connected')
while True :
    print('输入q退出,输入e则在人物脚下放置3*3黄金方块')
    msg=input('>')
    pos = mc.player.getTilePos()
    if msg=='q':
        break
    if msg=='e':
        msg = "player.getPos()\r"
        s.send(msg.encode("ascii"))
        x,y,z = map(int,eval(s.recv(1024)))

        for a in range(-1,2):
            for b in range(-1,2):
                s.send(bytes('world.setBlock('+str(x+a)+','+str(x-1)+','+str(z+b)+',41)\r\n','gbk'))
    s.close()
