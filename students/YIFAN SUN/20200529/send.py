import serial

ser=serial.Serial("COM20")

while True:
    c=input("please input side(O or C)")
    print(c)
    if c=="q":
        break
    ser.write(c.encode())
