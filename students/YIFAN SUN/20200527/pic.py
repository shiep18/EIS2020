import cv2
pd1 = cv2.imread('ON.jpg')
pd2 = cv2.imread('OFF.jpg')
pd3 = cv2.imread('LOCK.jpg')
data=['ON','OFF','LOCK']
global p
a=0
F=0
T=1
p=F
cv2.imshow('result',pd1)
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if ((75<x<190) or (215<x<330)) and (247<y<290 or 312<y<397):
            #p=T
            cv2.imshow('result',pd2)
            #pass
            with open("C:/Apache24/htdocs/num.html","w") as f:
                
                f.writelines(data[1])
        elif 190<x<215 and 290<y<312:
            cv2.imshow('result',pd3)
            cv2.setMouseCallback('result',click)
            with open("C:/Apache24/htdocs/num.html","w") as f:
                
                f.writelines(data[2])
        else:
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            with open("C:/Apache24/htdocs/num.html","w") as f:
                
                f.writelines(data[0])
            
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:#27是esc
            break
cv2.destroyAllWindows()
