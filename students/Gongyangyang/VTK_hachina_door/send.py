import serial

ser = serial.Serial("COM12")

while True:
    c = input("please input state:")
    print(c)
    if c is "q":
        break
    ser.write(c.encode())
