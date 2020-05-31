import serial

ser=serial.Serial("COM12")
ser.write(" ".encode())

while True:
    c=input("a:开门 b:关门 您的选项是：")
    print(c)
    if c=="q":
        break
    ser.write(c.encode())
