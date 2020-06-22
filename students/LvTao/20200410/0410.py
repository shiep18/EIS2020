import cv2

a=370
b=180
d=160

img=cv2.imread("red.jpg")
print(img.shape)
cv2.rectangle(img,(a,b),(a+d,b+d),(0,255,0),3)
cv2.imwrite("myhead.jpg",img[b:(b+d),a:(a+d)])

imghead=cv2.imread("myhead.jpg")
cv2.imshow("myhead1",imghead)
cv2.imshow("mybigwindow",img)

def mycircle(event,x,y,flags,pa):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        print("click")
        cv2.circle(img,(x,y),50,(255,0,0),3)

cv2.setMouseCallback("mybigwindow",mycircle)

while True:
    cv2.waitKey(1000)
    cv2.imshow("mybigwindow",img)
    
cv2.destroyAllWindows()

