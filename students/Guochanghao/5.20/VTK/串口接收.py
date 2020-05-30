import serial
ser=serial.Serial("COM2",timeout=1)
while True:
    c = input("Please input speed:")
    print(c)
    if c == "q":
        break
    ser.write(c.encode())
