import serial
global leftspeed,rightspeed
ser=serial.Serial('COM3',timeout=1) #阻塞式读
leftspeed=0
rightspeed=0
def jieshou():
    global leftspeed,rightspeed
    resp=ser.readline()
    if resp != b"":
        resp=resp.decode() #解码
        b=resp.strip()
        c=b.split(',')
        d=list(map(int,c))
        leftspeed=d[0]
        rightspeed=d[1]
    print('car wheel speed is: ',leftspeed,rightspeed)
    return leftspeed,rightspeed
