import cv2
import numpy as np
import mcpi.minecraft as minecraft
cap = cv2.VideoCapture(0)  # 打开摄像头
lower_red = np.array([1, 150, 100])
upper_red = np.array([8, 255, 255])
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
lens = 10
xCenter = 0
yCenter = 0

# 移动位置
def mcgo(dir):
    direction = mc.player.getDirection()
    pos = mc.player.getTilePos()
    x = pos.x
    z = pos.z
    if dir == "go":
        x = pos.x + (direction.x * lens)
        z = pos.z + (direction.z * lens)
    elif dir == "back":
        x = pos.x + (direction.x * (-1 * lens))
        z = pos.z + (direction.z * (-1 * lens))
    elif dir == "right":
        x = pos.x + (direction.z * (-1 * lens))
        z = pos.z + (direction.x * lens)
    elif dir == "left":
        x = pos.x + (direction.z * lens)
        z = pos.z + (direction.x * (-1 * lens))
    mc.player.setPos(x, pos.y, z)

while True:
    ret, pic = cap.read()  # 截取一帧图片
    y, x, l = pic.shape
    # print(x,y)
    pichsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)  # 选择相应的截取图片转换为hsv格式
    red = cv2.inRange(pichsv, lower_red, upper_red)  # 将选择的图片进行设阈值，去除背景部分
    # cv2.imshow("red",red)
    conter, hierarchy = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 找轮廓
    pic = cv2.drawContours(pic, conter, -1, (0, 255, 0), 3)  # 画轮廓
    pos = mc.player.getTilePos()
    biggest = []
    for i in conter:
        area = cv2.contourArea(i)  # 计算轮廓面积
        # print(area)
        if area > 10:
            biggest.append(i)
            # print(biggest)
        for cnt in biggest:
            # print("aaa")
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            print(cx, cy)
            cv2.circle(pic, (cx, cy), 50, (0, 0, 255), 5)
    # 判断位置
            xCenter = cx
            yCenter = cy
            if 100 < xCenter < 540 and yCenter < 160:
                print("go")
                mcgo("go")
            elif 100 < xCenter < 540 and yCenter > 350:
                print("back")
                mcgo("back")
            elif xCenter < 160 and 100 < yCenter < 380:
                print("right")
                mcgo("right")
            elif xCenter > 480 and 100 < yCenter < 380:
                print("left")
                mcgo("left")
    # 显示图层
    cv2.imshow('res', pic)
##    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
