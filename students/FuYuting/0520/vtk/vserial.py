import serial


##
ser=serial.Serial("COM12")
ser.write("100,100,100\n".encode()) #com12发

while True:
    c=input("please input the speed:")
    print(c)
    if c=="q":
        break
    ser.write(c.encode())

