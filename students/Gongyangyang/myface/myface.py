import cv2
#import os module for reading training data directories and paths
import os
#import numpy to convert python lists to numpy arrays as 
#it is needed by OpenCV face recognizers
import numpy as np
from mcpi.minecraft import Minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time
import matplotlib.pyplot as plt


subjects = ["", "chenweiting", "Leonardo DiCaprio","Morgan Freeman"]


ports = list(serial.tools.list_ports.comports())
print (ports)

ser=serial.Serial(port='COM2')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

mc=Minecraft.create()


def door(x0,y0,z0,L,act):
    if act :
        m = block.AIR.id
    else :
        m = block.GLASS.id
    mc.setBlock(x0+int(L/2), y0+1, z0,m) #门
    mc.setBlock(x0+int(L/2), y0+2, z0,m)

def buildhouse(x0,y0,z0,L,W,H,M):
    for y in range(H):
        for x in range(L):
            mc.setBlock(x0+x,y0+y,z0,M)
            mc.setBlock(x0+x,y0+y,z0+W-1,M)
        for z in range(W):
            mc.setBlock(x0,y0+y,z0+z,M)
            mc.setBlock(x0+L-1,y0+y,z0+z,M)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x, y0+H-1, z0+z,1)
            mc.setBlock(x0+x, y0, z0+z,1)   #建地板

    door(x0,y0,z0,L,0)

    for z in range(2):
        for y in range(2): 
            mc.setBlock(x0+L-1,y0+y+2,z0+z+4,20) #窗

x0,y0,z0,L,W,H,M = (59,8,282,10,10,6,1)
buildhouse(x0,y0,z0,L,W,H,M)

def isInhouse(x,y,z,L,W,H):
        pos = mc.player.getTilePos()
        x0,y0,z0 = pos.x,pos.y,pos.z
        if x-10 <= x0 <= x+L+10 and y <= y0 <= y+H and z-10 <= z0 <= z+W+10:
            return True
        else :
            return False


def detect_face(img):
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector, I am using LBP which is fast
    #there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    #result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None
    
    #under the assumption that there will be only one face,
    #extract the face area
    (x, y, w, h) = faces[0]
    
    #return only the face part of the image
    return gray[y:y+w, x:x+h], faces[0]


face_recognizer  = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('Training.yml')

#function to draw rectangle on image 
#according to given (x, y) coordinates and 
#given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#function to draw text on give image starting from
#passed (x, y) coordinates. 
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


# First function `draw_rectangle` draws a rectangle on image based on passed rectangle coordinates. It uses OpenCV's built in function `cv2.rectangle(img, topLeftPoint, bottomRightPoint, rgbColor, lineWidth)` to draw rectangle. We will use it to draw a rectangle around the face detected in test image.
# 
# Second function `draw_text` uses OpenCV's built in function `cv2.putText(img, text, startPoint, font, fontSize, rgbColor, lineWidth)` to draw text on image. 
# 
# Now that we have the drawing functions, we just need to call the face recognizer's `predict(face)` method to test our face recognizer on test images. Following function does the prediction for us.

# In[9]:

#this function recognizes the person in image passed
#and draws a rectangle around detected face with name of the 
#subject
def predict(test_img):
    #make a copy of the image as we don't want to chang original image
    img = test_img.copy()
    #detect face from the image
    face, rect = detect_face(img)
    label_text = ""
    try :
        # cv2.imshow("face",face)
        # cv2.waitKey(1000)
        # cv2.destroyAllWindows()
        cv2.imwrite("face.jpg",face)
        #predict the image using our face recognizer 
        label, confidence = face_recognizer.predict(face)
        print("label,confidence",label,confidence)
        #get name of respective label returned by face recognizer
        label_text = subjects[label]
        
        #draw a rectangle around face detected
        draw_rectangle(img, rect)
        #draw name of predicted person
        draw_text(img, label_text, rect[0], rect[1]-5)
    except :
        pass
    return img,label_text

# Now that we have the prediction function well defined, next step is to actually call this function on our test images and display those test images to see if our face recognizer correctly recognized them. So let's do it. This is what we have been waiting for. 

cap = cv2.VideoCapture(0) 

i1 = 0
led = ""
# In[10]:
while True :
    ret, img= cap.read()
    #load test images
    # test_img1 = cv2.imread("test-data/test3.jpg")
    test_img1 = img

    #perform a prediction
    predicted_img1,sub = predict(test_img1)

    act = 0
    print("Prediction complete")
    i1 = i1 + 1
    led = "4567g"

    
    #display both images
    cv2.imshow("camera", cv2.resize(predicted_img1, (400, 500)))
    if sub in ["chenweiting", "Morgan Freeman"]:
        act = 1
        led = "0123y"

    if isInhouse(x0,y0,z0,L,W,H):
        pass
    else :
        led = "yg"
    if i1 > 8:
        ser.write(led.encode())
        i1 = 0
    door(x0,y0,z0,L,act)

    key = cv2.waitKey(1) & 0xFF
    # 按'q'健退出循环
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
