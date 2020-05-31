import serial

ser=serial.Serial("COM2")
ser.write("100,200,100\n".encode())

while True:
    c=input("please input O(open) OR C(close)")
    print(c)
    if c=="q":
        break
    ser.write(c.encode())
