import socket
s = socket.socket()
s.connect(('127.0.0.1',4711))
print("connected")
msg = "player.getPos()\n"  
s.send(msg.encode("ascii"))
x,y,z = map(int,eval(s.recv(1024)))
msg = f"world.setBlocks({x},{y},{z},{x+2},{y},{z+2},41)\r"
s.send(msg.encode("ascii"))
s.close()
