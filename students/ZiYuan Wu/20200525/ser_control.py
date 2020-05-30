import serial

ser=serial.Serial("COM2")
ser.write("100,100,0\n".encode())

while True:
    c=input("please input left and right speed")
    print(c)
    if c=='q':
        break
    ser.write(c.encode())
