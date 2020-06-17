from cv2 import cv2
from aip import AipOcr
import numpy as np

APP_ID = '20329719'  
API_KEY = 'Zzfd3PTU2Xc2FNeGwXVCePzx'  
SECRECT_KEY = 'sBOzZejSHAnvATE1UQR8SUVpponrBMvY' 
client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
class chess():
    def __init__(self,APP_ID,API_KEY,SECRECT_KEY,client):
        self.API_KEY = API_KEY
        self.SECRECT_KEY = SECRECT_KEY
        self.APP_ID = APP_ID
        self.client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
    def compare(self,red,black):
        if red > 100 and black <100 :
            return '黑方获得最后胜利'
        if red <100 and black >100 :
            return '红方获得最后胜利'
        if red==-1 and black>1:
            return '红方获胜'
        if red>1 and black==-1:
            return '黑方获胜'
        if red <0 or black < 0 :
            if red>-2 or black>-2 :
               if red==1 : 
                   return '红方获胜'
               if black==1 : 
                   return '黑方获胜'
            return '同归于尽'
        if red >black :
            return '红方获胜'
        if red < black :
            return '黑方获胜'
        if red==black :
            return '同归于尽'
    def process(self,img,a,b,path):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        low_hsv = np.array(a)
        high_hsv = np.array(b)
        image = cv2.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
        kernel = np.ones((3,3), np.uint8)
        erosion = cv2.dilate(image, kernel)
        cv2.imwrite(path,erosion)
        #options={}
        #options["detect_direction"] = "true"
        with open(path, 'rb') as fp:
            img=fp.read()
        message=client.basicGeneral(img)#普通精度
        #message = client.basicAccurate(img)#高精度
        for item in message['words_result']:
            words=item['words']
            return words

