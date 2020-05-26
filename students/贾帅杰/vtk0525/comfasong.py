import serial

ser=serial.Serial('COM2')
s=ser.write('100,100,100\n'.encode())

while True:
    c=input('please input left and right speed:')
    print(c)
    if c=='q':
        break
    ser.write(c.encode())
