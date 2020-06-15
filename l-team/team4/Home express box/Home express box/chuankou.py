import serial

ser=serial.Serial("COM2")
ser.write("100,200,100\n".encode())

while True:
    c=input("请确定是否开启保险箱:")
    print(c)
    if c=="q":
        break
    ser.write(c.encode())


