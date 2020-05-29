import cv2
pd = cv2.imread('on.jpg')
pd1 = cv2.imread('off.jpg')
pd2=cv2.imread('lock.jpg')
data=['on','off','lock']
global p
F=0
T=1
p=F
cv2.imshow('result',pd)
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 135<x<295 and 90<y<290:
            print ('pd')
            #p=T
            cv2.imshow('result',pd)
            #pass
            with open("C:/Apache24/htdocs/num.html","w") as f:
                f.writelines(data[0])
        elif: 295<x<350 and 290<y<350
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            with open("C:/Apache24/htdocs/num.html","w") as f:
                
                f.writelines(data[1])
        else:
            cv2.imshow('result',pd2)
            cv2.setMouseCallback('result',click)
            with open("C:/Apache24/htdocs/num.html","w") as f:
                
                f.writelines(data[2])
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:#27是esc
            break
cv2.destroyAllWindows()
#f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")网页自动刷新
