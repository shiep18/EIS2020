import cv2
import pyzbar.pyzbar as pyzbar
from mcpi.minecraft import Minecraft
import time
import expressboxinfo
import os
from os import system
import win32com.client
def detectpos():
    mc=Minecraft.create("47.100.46.95",4784)
    entityId= mc.getPlayerEntityId("W")
    pos=mc.entity.getTilePos(entityId)
    if 1287<=pos.x<=1288 and pos.y==5 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1287<=pos.x<=1288 and pos.y==5 and 1185<=pos.z<=1187:
            return 1
        else:
            return 0
        
    pos=mc.entity.getTilePos(entityId)
    if 1282<=pos.x<=1283 and pos.y==5 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1282<=pos.x<=1283 and pos.y==5 and 1185<=pos.z<=1187:
            return 2
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1287<=pos.x<=1288 and pos.y==11 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1287<=pos.x<=1288 and pos.y==11 and 1185<=pos.z<=1187:
            return 3
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1282<=pos.x<=1283 and pos.y==11 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1282<=pos.x<=1283 and pos.y==11 and 1185<=pos.z<=1187:
            return 4
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1287<=pos.x<=1288 and pos.y==17 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1287<=pos.x<=1288 and pos.y==17 and 1185<=pos.z<=1187:
            return 5
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1282<=pos.x<=1283 and pos.y==17 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1282<=pos.x<=1283 and pos.y==17 and 1185<=pos.z<=1187:
            return 6
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1211<=pos.x<=1212 and pos.y==5 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1211<=pos.x<=1212 and pos.y==5 and 1185<=pos.z<=1187:
            return 7
        else:
            return 0
        
    pos=mc.entity.getTilePos(entityId)
    if 1206<=pos.x<=1207 and pos.y==5 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1206<=pos.x<=1207 and pos.y==5 and 1185<=pos.z<=1187:
            return 8
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1211<=pos.x<=1212 and pos.y==11 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1211<=pos.x<=1212 and pos.y==11 and 1185<=pos.z<=1187:
            return 9
        else:
            return 0
        
    pos=mc.entity.getTilePos(entityId)
    if 1206<=pos.x<=1207 and pos.y==11 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1206<=pos.x<=1207 and pos.y==11 and 1185<=pos.z<=1187:
            return 10
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1211<=pos.x<=1212 and pos.y==17 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1211<=pos.x<=1212 and pos.y==17 and 1185<=pos.z<=1187:
            return 11
        else:
            return 0
        
    pos=mc.entity.getTilePos(entityId)
    if 1206<=pos.x<=1207 and pos.y==17 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1206<=pos.x<=1207 and pos.y==17 and 1185<=pos.z<=1187:
            return 12
        else:
            return 0

def decodeDisplay(image,room):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        # 提取二维码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (225, 225, 225), 2)
        # 提取二维码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, .5, (225, 225, 225), 2)
        # 向终端打印条形码数据和条形码类型
        #print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        #f = open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\package_send.txt",'r+')
        #if f.read()=="":
        print("二维码包含内容: {}".format(barcodeData))
        time.sleep(1)
        m=expressboxinfo.express_info(str(room))
        print(m)
        
        if m[1]==format(barcodeData) and m[2]=='0':
            f = open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\Password_verification.txt",'r+')
            f.write(str(room))
            g = open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\recognition_check.txt",'r+')
            g.write(format(barcodeData))
        elif m[1]!=format(barcodeData):
            speaker=win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("二维码匹配失败！")
    return image
def detect(room):
    mc=Minecraft.create("47.100.46.95",4784)
    entityId= mc.getPlayerEntityId("W")
    camera = cv2.VideoCapture(0)
    while True:
        # 读取当前帧
        ret, frame = camera.read()
        # 转为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im = decodeDisplay(gray,room)
        cv2.waitKey(5)
        cv2.imshow("camera", im)
        pos=mc.entity.getTilePos(entityId)
        x=pos.x
        y=pos.y
        z=pos.z
        #time.sleep(0.1)
        pos=mc.entity.getTilePos(entityId)
        if x!=pos.x or y!=pos.y or z!=pos.z:
            break
        g = open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\recognition_check.txt",'r+')
        check=g.read()
        if check!="":
            g = open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\recognition_check.txt",'r+')
            g.truncate()
            h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
            h.write("closecapflag")
            break
    camera.release()
    cv2.destroyAllWindows()
    
    
