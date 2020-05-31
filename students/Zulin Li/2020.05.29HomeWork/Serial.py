import serial

ser=serial.Serial("COM12")

while True:
    c=input("please input A or B:")
    print(c)
    if c=="q":
        break
    ser.write(c.encode())