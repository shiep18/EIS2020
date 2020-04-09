import serial
import serial.tools.list_ports
import time

print('hello')
ports = list(serial.tools.list_ports.comports())
print(ports)

for p in ports:
    print(p[1])
    if "SERIAL" in p[1]:
        ser=serial.Serial(port=p[0])
    else:
        print("No Arduino Device was found connected to the computer")

ser=serial.Serial(port='COM12')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

def run():
    action = "empty"
    while action != "q":
        print('q for quit,others for command')
        action = input("> ")
        ser.write(action.encode())
        time.sleep(1)
        ser.write("y".encode())
        time.sleep(1)
        ser.write("g".encode())
        time.sleep(1)

run()
