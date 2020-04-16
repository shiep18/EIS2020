import socket

s=socket.socket()
s.connect(("127.0.0.1",4711))
print("connected")
##msg=input(">")
##s.send(msg.encode("ascii"))

msg1 = "player.setPos(120,2,-95)\r"
msg2 = "world.setBlocks(119,1,-94,121,1,-96,41)\r"

s.send(msg1.encode("ascii"))
s.send(msg2.encode("ascii"))
