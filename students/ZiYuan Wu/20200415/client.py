import socket

s = socket.socket()
s.connect(("127.0.0.1",4711))
print("connected")

msg1 = "player.setPos(400,0,400)\r\n"
msg2 = "world.setBlocks(401,-9,401,403,-9,403,41)\r\n"

s.send(msg1.encode("ascii"))
s.send(msg2.encode("ascii"))
