import numpy as np
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('baby.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,5)
for(x,y,w,h)in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=gray[y:y+h,x:x+w]
    roi_color=img[y:y+h,x:x+w]
cv2.imwrite("face.jpg",img[y:y+h,x:x+w])
face=cv2.imread("face.jpg")
cv2.imshow('img',img)
cv2.imshow('face',face)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
