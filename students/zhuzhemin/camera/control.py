import cv2
import numpy as np 
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z
Rotation=mc.player.getRotation()#水平角度
def reset():
    global pos,x,y,z,Rotation
    pos = mc.player.getTilePos()
    x=pos.x
    y=pos.y
    z=pos.z
    Rotation=mc.player.getRotation()#水平角度
    print("reset")
#读取视频
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  
width = 640  #定义摄像头获取图像宽度
height = 480   #定义摄像头获取图像长度

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)  #设置宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  #设置长度
lower_red=np.array([120,130,120])
upper_red=np.array([255,255,255])
while(cap!=0):   
    #读取视频到frame中，颜色识别方式转换成HSV    
    ret, frame = cap.read()    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
    #显示原来的视频    
    #cv2.namedWindow('frame', cv2.WINDOW_FULLSCREEN)    
        
    #提取视频中hong色的部分    
    mask = cv2.inRange(hsv, lower_red, upper_red)  
    conts,hrc=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if(mask[30][30]==255):
        reset()
    if (0<=Rotation<45)|(315<=Rotation<360):
        if(mask[10][320]==255)|(mask[30][320]==255):
            print("1上")
            z+=1
            mc.player.setTilePos(x,y,z)
        elif(mask[470][320]==255)|(mask[450][320]==255):
            print("1下")
            z-=1
            mc.player.setTilePos(x,y,z)
        elif(mask[240][10]==255)|(mask[240][30]==255):
            print("1左")
            x+=1
            mc.player.setTilePos(x,y,z)
        elif(mask[240][610]==255)|(mask[240][630]==255):
            print("1右")
            x-=1
            mc.player.setTilePos(x,y,z)
###############################################################
    elif (45<=Rotation<135):
        if(mask[10][320]==255)|(mask[30][320]==255):
            print("2上")
            x+=1
            mc.player.setTilePos(x,y,z)
        elif(mask[470][320]==255)|(mask[450][320]==255):
            print("2下")
            x-=1
            mc.player.setTilePos(x,y,z)
        elif(mask[240][10]==255)|(mask[240][30]==255):
            print("2左")
            z-=1
            mc.player.setTilePos(x,y,z)
        elif(mask[240][610]==255)|(mask[240][630]==255):
            print("2右")
            z+=1
            mc.player.setTilePos(x,y,z)
################################################################
    elif (135<=Rotation<225):
        if(mask[10][320]==255)|(mask[30][320]==255):
            print("3上")
            z-=1
            mc.player.setTilePos(x,y,z)
        elif(mask[470][320]==255)|(mask[450][320]==255):
            print("3下")
            z+=1
            mc.player.setTilePos(x,y,z)
        elif(mask[240][10]==255)|(mask[240][30]==255):
            print("3左")
            x-=1
            mc.player.setTilePos(x,y,z)
        elif(mask[240][610]==255)|(mask[240][630]==255):
            print("3右")
            x+=1
            mc.player.setTilePos(x,y,z)
###########################################################
    elif (225<=Rotation<315):
        if(mask[10][320]==255)|(mask[30][320]==255):
            print("4上")
            x-=1
            mc.player.setTilePos(x,y,z)
        elif(mask[470][320]==255)|(mask[450][320]==255):
            print("4下")
            x+=1
            mc.player.setTilePos(x,y,z)
        elif(mask[240][10]==255)|(mask[240][30]==255):
            print("4左")
            z-=1
            mc.player.setTilePos(x,y,z)
        elif(mask[240][610]==255)|(mask[240][630]==255):
            print("4右")
            z+=1
            mc.player.setTilePos(x,y,z)
##############################################################
    #cv2.imshow('frame', frame)#原图 
    #print(conts)  
    #cv2.namedWindow('mask', cv2.WINDOW_FULLSCREEN)    
    cv2.imshow('Mask', mask) #black-white   
    #原视频和提取后的视频做与操作    
    res = cv2.bitwise_and(frame, frame, mask=mask)    
    cv2.namedWindow('res', cv2.WINDOW_FULLSCREEN)    
    cv2.imshow('res', res)#black-red   
    key = cv2.waitKey(1) & 0xFF
    # print(key)
    if key == ord('q'):
        break 
cap.release()
cv2.destroyAllWindows()