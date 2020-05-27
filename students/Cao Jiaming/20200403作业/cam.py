import cv2
import numpy as np
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
lens = 10
xCenter = 0
yCenter = 0


# 移动位置
def mcgo(dir):
    direction = mc.player.getDirection()
    pos = mc.player.getTilePos()
    x = pos.x
    z = pos.z
    if dir == "strange":
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


# 读取视频
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width = 640  # 定义摄像头获取图像宽度
height = 480  # 定义摄像头获取图像长度
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # 设置宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # 设置长度
# 设定蓝色阈值
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
while cap is not None:
    # 读获取每一帧
    ret, frame = cap.read()
    # 转换成HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)  # 该函数计算一幅图像中目标的轮廓
    res = cv2.bitwise_and(frame, frame, mask=mask)
    xCenter = 0
    yCenter = 0
    for c in contours:
        if cv2.contourArea(c) < 1600:  # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
            continue
        (x1, y1, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
        xCenter = x1 + w / 2
        yCenter = y1 + h / 2
        cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
        cv2.rectangle(res, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
    # 判断掩模中白色的位置
    if 100 < xCenter < 540 and yCenter < 100:
        print("strange")
        mcgo("strange")
    elif 100 < xCenter < 540 and yCenter > 380:
        print("back")
        mcgo("back")
    elif xCenter < 100 and 100 < yCenter < 380:
        print("right")
        mcgo("right")
    elif xCenter > 540 and 100 < yCenter < 380:
        print("left")
        mcgo("left")
    # 显示图层
    cv2.imshow('res', res)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
