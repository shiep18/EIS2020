import serial

ser = serial.Serial("COM12")

while True:

    c = input("PLease enter the instruction: ")
    print(c)
    if c is "q":
        break
    
    ser.write(c.encode())
