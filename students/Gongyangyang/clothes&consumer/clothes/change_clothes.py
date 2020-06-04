import cv2
from voice import *
from detect_face import cat_face,human_face

cloth1 = cv2.imread("./clothes/1.jpg")
cloth2 = cv2.imread("./clothes/2.jpg")
cloth3 = cv2.imread("./clothes/3.jpg")

catFace = cat_face()

def replace_face(img):
    humanFace,y,h,x,w = human_face(img)
    rs_catFace = cv2.resize(catFace, humanFace.shape[:2])
    new_img = img.copy()
    new_img[y:y + h,x:x + w] = rs_catFace 
    cv2.imshow('result', new_img)

# cv2.imshow('result',cloth1)
replace_face(cloth1)

def click(event,x,y,flags,param):  # 左键点击开始录音
    if event==cv2.EVENT_LBUTTONDOWN:
        record()
        cloth = recognize()
        if cloth is not None:
            if '白' in cloth:
                replace_face(cloth2)
            elif '黑' in cloth:
                replace_face(cloth1)
            elif '黄' in cloth:
                replace_face(cloth3)
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)

while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
