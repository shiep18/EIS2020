import cv2
import numpy as np
def mopcatch():
    cap = cv2.VideoCapture(0)
    background = None
    temp = 0
    while True:
        ret, frame= cap.read()
        gray_lwpCV = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if background is None:
            background = gray_lwpCV
            continue
    diff = cv2.absdiff(background, gray_lwpCV)
    diff = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)[1]

    contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    for c in contours:
        if cv2.contourArea(c) < 2000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count += 1
        if temp != 0:
            if count > temp :     # 方框变多视为运动物体进入
                print("playsound")
        temp = count
        cv2.imshow('contours', frame)
        cv2.imshow('dis', diff)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

