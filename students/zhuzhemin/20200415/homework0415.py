import socket
s = socket.socket()
s.connect(("127.0.0.1",4711))
print("connected")
msg1 = "player.setPos(402,50,402)\r\n"
msg2 = "world.setBlocks(401,45,401,403,45,403,41)\r\n"
s.send(msg1.encode("ascii"))
s.send(msg2.encode("ascii"))
