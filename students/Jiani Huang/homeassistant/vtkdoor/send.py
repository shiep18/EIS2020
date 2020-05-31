import serial

ser=serial.Serial("COM2")

while True:
    c=input("please input side(A or B)")
    print(c)
    if c=="q":
        break
    ser.write(c.encode())
