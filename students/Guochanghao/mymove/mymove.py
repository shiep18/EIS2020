import cv2
import numpy as np
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

# 读取视频
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width = 300  # 定义摄像头获取图像宽度
height = 300  # 定义摄像头获取图像长度
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # 设置宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # 设置长度

# 设定绿色阈值BGR
lower_green = np.array([36,25,25])
upper_green = np.array([86,255,255])

while cap is not None:
    # 读获取每一帧
    ret, frame = cap.read()
    # 转换成HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_green, upper_green)
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  # 该函数计算一幅图像中目标的轮廓
    res = cv2.bitwise_and(frame, frame, mask=mask)
    xCenter = 0
    yCenter = 0
    for c in contours:
        if cv2.contourArea(c) < 1600:  # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
            continue
        (x1, y1, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
        xCenter = x1+w/2
        yCenter = y1+h/2
        cv2.rectangle(frame,(x1,y1),(x1+w,y1+h), (0,255,0),2)
        cv2.rectangle(res,(x1,y1), (x1+w,y1+h), (0,255,0),2)

    # 判断掩模中白色的位置
    pos = mc.player.getTilePos()
    x = pos.x
    z = pos.z
    if 100 < xCenter < 540 and yCenter < 100:
        print("stright")
        x = pos.x+5
    elif 100 < xCenter < 540 and yCenter > 380:
        print("back")
        x = pos.x5
    elif xCenter < 100 and 100 < yCenter < 380:
        print("right")
        z = pos.z+5
    elif xCenter > 540 and 100 < yCenter < 380:
        print("left")
        z = pos.z-5
    mc.player.setPos(x, pos.y, z)

    # 显示图层
    cv2.imshow('res', res)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF

    # 按'q'键退出循环
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
