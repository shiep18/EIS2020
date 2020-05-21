import serial

ser = serial.Serial("COM2")
#ser.write("100,100,100\n".encode())
while True:
    c = input("please input speed:")
    print(c)
    if c == "q":
        break
    ser.write(c.encode())
