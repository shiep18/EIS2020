import serial

ser = serial.Serial("COM12")
ser.write("100,100,100\n".encode())

while True:
    c = input("please input left and right speed")
    print(c)
    if c is "q":
        break
    ser.write(c.encode())
