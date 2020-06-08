import cv2
import numpy as np


flag = 0
piz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pix = []
img = np.zeros((600, 600, 3), np.uint8)
img[:] = [200, 5, 100]
chess = np.zeros((3, 3), np.int8)
cv2.line(img, (120, 120), (480, 120), (250, 230, 200), 3)
cv2.line(img, (120, 240), (480, 240), (250, 230, 200), 3)
cv2.line(img, (120, 360), (480, 360), (250, 230, 200), 3)
cv2.line(img, (120, 480), (480, 480), (250, 230, 200), 3)
cv2.line(img, (480, 120), (480, 480), (250, 230, 200), 3)
cv2.line(img, (360, 120), (360, 480), (250, 230, 200), 3)
cv2.line(img, (240, 120), (240, 480), (250, 230, 200), 3)
cv2.line(img, (120, 120), (120, 480), (250, 230, 200), 3)


def click(event, x, y, flags, param=0):
    global flag
    global pix
    if event == cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:', x, y)
        for i in range(3):
            for j in range(3):
                if (i + 1) * 120 < x < (i + 2) * 120 and (j + 1) * 120 < y < (j + 2) * 120 and piz[i][j] == 0:
                    if flag % 2 == 0:
                        cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (0, 0, 0), -1)
                        cv2.imshow('result', img)
                        piz[i][j] = 1
                    else:
                        cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (255, 255, 255), -1)
                        cv2.imshow('result', img)
                        piz[i][j] = -1
                        cv2.setMouseCallback('result', click)
                    flag = flag + 1
                    pix = sum(piz, [])
        print(event)
        print(flag)
        print(piz)
        print(pix)


def win_or_lost():
    lines = [pix[0:3], pix[3:6], pix[6:9], pix[0::3], pix[1::3], pix[2::3], pix[0::4], pix[2:7:2]]
    if [1] * 3 in lines:
        return 0
    elif [-1] * 3 in lines:
        return 1
    else:
        return 2


cv2.imshow('result', img)
cv2.namedWindow('result')
cv2.setMouseCallback('result', click)
while True:
    if cv2.waitKey(10) & 0xFF == 27:
        break
    elif win_or_lost() != 2:
        if win_or_lost() == 0:
            print('black wins,white lost!')
            print('the game finish!')
            break
        elif win_or_lost() == 1:
            print('black lost,white wins!')
            print('the game finish!')
            break
    elif win_or_lost() == 2 and flag == 9:
        print('draw!')
        print('the game finish!')
        break

cv2.destroyAllWindows()
