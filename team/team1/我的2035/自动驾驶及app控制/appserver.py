from mcpi.minecraft import Minecraft
import time
import socket
import re
import numpy as np



mc=Minecraft.create("47.100.46.95",4781)
entityId= mc.getPlayerEntityId("wzy")

def getipaddrs(hostname):  # 只是为了显示IP，仅仅测试一下
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]

host = ''  # 为空代表为本地host
hostname = socket.gethostname()
hostip = getipaddrs(hostname)
print('host ip', hostip)  # 应该显示为：127.0.1.1
port = 9999  # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(4)
data = ''
homeRange = (-465,-485,-443,-448)
villageRange = (-412,-420,-462,-470)
companyRange = (-304,-310,-410,-420)
shopRange = (-370,-380,-338,-342)



pos=mc.entity.getTilePos(entityId)
lastx = pos.x
lastz = pos.z
key = 0
if __name__=='__main__':
    while True:
        conn, addr = s.accept()
        #s.connect((192.168.0.101))
        print('Connected by', addr)
        data = conn.recv(1024)
        #print(data)
        pos=mc.entity.getTilePos(entityId)
        if data:
            mode = str(data.decode('utf-8'))   
            
            if mode == "home":
                if ((pos.x <= homeRange[0]) & (pos.x >= homeRange[1])) & ((pos.z <= homeRange[2]) & (pos.z >= homeRange[3])): #注意小括号一定要打完
                    mc.postToChat("Welcome "+mode)
                    key=key+1
                    
            elif mode=="village":
                if ((pos.x <= villageRange[0]) & (pos.x >= villageRange[1])) & ((pos.z <= villageRange[2]) &(pos.z >= villageRange[3])):
                    mc.postToChat("Welcome "+mode)
                    key=key+1
                    
            elif mode=="company":
                if ((pos.x <= companyRange[0]) & (pos.x >= companyRange[1])) & ((pos.z <= companyRange[2]) &(pos.z >= companyRange[3])):
                    mc.postToChat("Welcome "+mode)
                    key=key+1
                    
            elif mode=="shop":
                if ((pos.x <= shopRange[0]) & (pos.x >= shopRange[1])) & ((pos.z <= shopRange[2]) &(pos.z >= shopRange[3])):
                    mc.postToChat("Welcome "+mode)
                    key=key+1
                    
            elif mode == "start":
                f1 = open('relate.txt','r+')
                f1.write('2')
                f1.close()
                pass
            
        else:
            pass
        if key < 2:
                f1 = open('relate.txt','r+')
                f1.write('1')
                f1.close()
        else:
            key = 3
        dx = int((pos.x - lastx)*(-4.7))
        dz = int((pos.z - lastz)*(-5.0))
        data = str(dx)+","+str(dz)
        conn.sendall(data.encode('utf-8'))  # 把接收到数据原封不动的发送回去
        lastx = pos.x 
        lastz = pos.z 
        conn.close()
        print(pos.x,pos.z)
        #time.sleep(1)

        # mc.setBlock(x1-2,y1,z1,84)
        # time.sleep(1)
        # mc.setBlock(x1 - 2, y1, z1, 0)
        # time.sleep(0.1)
