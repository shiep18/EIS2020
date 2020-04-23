import socket
import sys
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
def sock_client_data():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 4711))  #服务器和客户端在不同的系统或不同的主机下时使用的ip和端口，首先要查看服务器所在的系统网卡的ip
        # s.connect(('127.0.0.1', 6666))  #服务器和客户端都在一个系统下时使用的ip和端口
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))
    time.sleep(3)
    #data = input("input data:")   #输入要传输的数据
    #s.send(data.encode())  #将要传输的数据编码发送，如果是字符数据就必须要编码发送
    mc.postToChat("The Code is Running ......")
    time.sleep(3)
    pos = mc.player.getTilePos()
    for i in range(3):
        for j in range(3):
            mc.setBlock(pos.x-1+i,pos.y-1,pos.z-1+j,41)
    mc.postToChat("The Gold had been Setted Surcessfully!")
    s.close()
if __name__ == '__main__':
    sock_client_data()