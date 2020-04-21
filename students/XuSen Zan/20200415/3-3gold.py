import socket

s = socket.socket()
s.connect(("127.0.0.1",4711))
print("connected")

msg1 = "player.setPos(300,48,300)\r"
msg2 = "world.setBlocks(299,48,299,301,48,301,41)\r"

s.send(msg1.encode("ascii"))
s.send(msg2.encode("ascii"))
