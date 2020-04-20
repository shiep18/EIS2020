import cv2
import numpy as np
from pykeyboard import PyKeyboard
from pymouse import PyMouse

def key_con(cx, cy, xmax, ymax, k):
    if cx < int(xmax / 3):
        k.press_key("a")
    else:
        k.release_key("a")

    if cx > int((xmax / 3) * 2):
        k.press_key("d")
    else:
        k.release_key("d")

    if cy > int((ymax / 3) * 2):
        k.press_key("s")
    else:
        k.release_key("s")

    if cy < int(ymax / 3):
        k.press_key("w")
    else:
        k.release_key("w")


def mouse_con(cx, cy, xmax, ymax, m):
    px, py = m.position()
    dx = cx - int(xmax / 2)
    dy = cy - int(ymax / 2)
    nx = int(dx / 10) + px
    ny = int(dy / 10) + py
    m.move(nx, ny)

cap = cv2.VideoCapture(0)
lower_green = np.array([40, 80, 45])
upper_green = np.array([80, 255, 255])
lower_yellow = np.array([15, 210, 100])
upper_yellow = np.array([25, 255, 140])

k = PyKeyboard()
m = PyMouse()

def camera_det():
    while True:
        ret, img = cap.read()
        ymax, xmax, leni = img.shape
        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        greenobj = cv2.inRange(imghsv, lower_green, upper_green)
        yellowobj = cv2.inRange(imghsv, lower_yellow, upper_yellow)
        gconts, hrc = cv2.findContours(greenobj, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        yconts, hrc = cv2.findContours(yellowobj, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        bigyconts = []
        for ycont in yconts:
            area = cv2.contourArea(ycont)
            if area > 200:
                bigyconts.append(ycont)
        biggconts = []
        for gcont in gconts:
            area = cv2.contourArea(gcont)
            if area > 1200:
                biggconts.append(gcont)
        cx = int(xmax / 2)
        cy = int(ymax / 2)
        for bigycnt in bigyconts:
            M = cv2.moments(bigycnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(img, (cx, cy), 50, (0, 0, 255), 5)
            break
        mouse_con(cx, cy, xmax, ymax, m)
        cx = int(xmax / 2)
        cy = int(ymax / 2)
        for biggcnt in biggconts:
            M = cv2.moments(biggcnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(img, (cx, cy), 50, (0, 0, 255), 5)
            break
        key_con(cx, cy, xmax, ymax, k)
        cv2.imshow("greenobj", greenobj)
        cv2.imshow("yellowobj", yellowobj)
        cv2.imshow("myshowwindwos", img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break