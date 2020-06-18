import serial

ser=serial.Serial("COM12")
ser.write("100,100,100\n".encode())
