import socket

s=socket.socket()
s.bind(("127.0.0.1",25566))
s.listen(5)



while True:
    c,addr=s.accept()
    print(f"address{addr}connected")
    msg=c.recv(1024)
    print(msg)
