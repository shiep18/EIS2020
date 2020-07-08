from PIL import Image
import pymysql
from MyQR import myqr
from xpinyin import Pinyin
import cv2
import os
import pyzbar.pyzbar as pyzbar
import time
import expressdata as ex

def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    barcodeData=99999
    for barcode in barcodes:
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
        # 条形码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
 
        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)
 
        # 向终端打印条形码数据和条形码类型
        #print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image,barcodeData
 
 
def detect(i):
 
    camera = cv2.VideoCapture(0)
 
    while True:
        # 读取当前帧
        ret, frame = camera.read()
        # 转为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im,data=decodeDisplay(gray)
 
        cv2.waitKey(5)
        cv2.imshow("camera", im)
        if data!=99999:
            time.sleep(3)
            break

    camera.release()
    cv2.destroyAllWindows()
    
    data=data.split(',')
    if ex.compared(data,i)==1:
        return 1
    elif ex.compared(data,i)==0:
        return 0


 
# if __name__ == '__main__':
#     pass
