import serial

ser=serial.Serial("COM12")
ser.write("0".encode())

while True:
    c=input("please input p or h")
    print(c)
    if c=="q":
        break
    ser.write(c.encode())
