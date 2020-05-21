import serial

ser = serial.Serial("COM20")
#ser.write("100,100,100\n".encode())

while True:
    c = input("please input speed: ")
    print(c)
    ser.write(c.encode())
    if c == "q":
        break
