#! python3
import pyautogui, sys
import time
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\n')
        time.sleep(0.5)
except KeyboardInterrupt:
    print('\n')
