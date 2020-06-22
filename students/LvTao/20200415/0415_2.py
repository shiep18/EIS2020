import socket

s=socket.socket()
s.connect(("127.0.0.1",25566))

print("connected")
msg=input(">")
s.send(msg.encode("ascii"))
