from cv2 import cv2
from aip import AipOcr
import numpy as np
import time
from  threading import Thread
from class_chess import chess
APP_ID = '20329719'  
API_KEY = 'Zzfd3PTU2Xc2FNeGwXVCePzx'  
SECRECT_KEY = 'sBOzZejSHAnvATE1UQR8SUVpponrBMvY'
client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
G=chess(APP_ID,API_KEY,SECRECT_KEY,client)
value={
    '工兵':1,
    '排长':2,
    '连长':3,
    '营长':4,
    '团长':5,
    '旅长':6,
    '师长':7,
    '军长':8,
    '司令':9,
    '地雷':-1,
    '炸弹':-2,
    '军旗':200,
}

def getImage():
    cap = cv2.VideoCapture(0)
    while True:
        ret , frame = cap.read()
        if ret:
            if frame is not None:
                cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#转灰度图
                cv2.imshow('capture',frame)
                cv2.imwrite('3.jpg',frame)#储存图片,''路径自定义
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
def judge():
    while True:
        try:
            temporary=[]
            src = cv2.imread("3.jpg")#读取图片,''对应路径
            pro = G.process(src,[0,128,180],[180,240,255],'mask.jpg')#mask为自定义路径下储存的图片名
            print(pro)
            if pro in value:
                temporary.append(pro)
            pro1 = G.process(src,[0,75,0],[120,255,55],'mask1.jpg')#两个数组为颜色阈值，识别效果不好可以通过调整阈值来改进
            print(pro1)
            if pro1 in value:
                temporary.append(pro1)
            if len(temporary)>=2:
                    c=G.compare(value[temporary[0]],value[temporary[1]])
                    print(c)
        except:
            pass
 
if __name__ == "__main__":
     Thread(target=judge).start()
     getImage()
