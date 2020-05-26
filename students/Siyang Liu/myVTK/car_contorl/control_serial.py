import serial

ser=serial.Serial("COM12")
ser.write("100,200,100\n".encode())

while True:
    c = input("please input left&right wheel speed and camera rotation speed: ")
    print(c)
    if c == "q":
        break
    ser.write(c.encode())
