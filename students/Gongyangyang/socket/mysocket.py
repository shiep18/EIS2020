import socket
s = socket.socket()
s.connect(('127.0.0.1',4711))
print("connected")

msg = "player.getPos()\n"  
s.send(msg.encode("ascii"))
x,y,z = map(int,eval(s.recv(1024)))

for i in range(-1,2):
    for j in range(-1,2):
        msg = f"world.setBlock({x+i},{y-1},{z+j},41)\n"
        s.send(msg.encode("ascii"))
s.close()

