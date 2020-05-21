import serial

ser=serial.Serial("COM13",timeout=1)

cnt=0
while True:
    resp=ser.readline()
    cnt+=1
    print("moving remote car",cnt)
    print(resp)
    if resp !=b"":
        resp=resp.decode()
        b=resp.strip()
        c=b.split(",")
        print(c)
        d=list(map(int,c))
        print(d)
        leftspeed=d[0]
        rightspeed=d[1]
        print("car wheel speed is",d)
