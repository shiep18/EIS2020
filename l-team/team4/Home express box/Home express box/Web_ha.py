import socket

p=1
BUFSIZE = 4096
tcpServerSocket = socket.socket()  # 1.创建
hostip = '192.168.1.4'
port = 12345
tcpServerSocket.bind((hostip, port))  # 2.bind
tcpServerSocket.listen(5)  # 监听，设置等待队列最大数目


while True:
    print("等待连接")
    clientSocket, addr = tcpServerSocket.accept()  # 3.接收连接请求，并获得ip和端口号
    while True:
        if p:
            print("已连接")
            p=0
        data = clientSocket.recv(BUFSIZE).decode()  # 4.接收数据
        print(data)
        if not data:
            break
        f = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\check.txt", 'r')
        s = f.read()
        if s=='':
            s='无'
        clientSocket.send(s.encode())  # 5.发送数据
    p=1
    clientSocket.close()




