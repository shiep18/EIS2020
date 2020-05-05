import socket

s=socket.socket()
s.connect(("127.0.0.1",4711))
print("connected")

msg = "player.getPos()\r"
s.send(msg.encode("ascii"))
x,y,z = map(int,eval(s.recv(1024)))
#print(x,y,z)
msg = f"world.setBlocks({x-1},{y-1},{z-1},{x+1},{y-1},{z+1},41)\r"
s.send(msg.encode("ascii"))
s.close()