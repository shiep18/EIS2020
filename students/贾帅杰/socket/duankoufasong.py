import socket


s=socket.socket()

s.connect(('127.0.0.1',4711))

print('connected')
print('输入a在脚下铺设黄金块')
while True :
    print('输入q退出，输入其他则在人物脚下放置3*3黄金方块')
    msg=input('>')
    
    if msg=='q':
        break
    if msg=='a':
        msg = "player.getPos()\r"
        s.send(msg.encode("ascii"))
        x,y,z = map(int,eval(s.recv(1024)))

        for a in range(-1,2):
            for b in range(-1,2):
                s.send(bytes('world.setBlock('+str(x+a)+','+str(y-1)+','+str(z+b)+',41)\r\n','gbk'))
            
s.close()
