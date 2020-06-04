import cv2

# 待检测的图片路径
ImagePath = './clothes/cat1.jpg'

def cat_face():
    # 读取图片
    image = cv2.imread(ImagePath)
    # 把图片转换为灰度模式
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 探测图片中的人脸
    # 获取训练好的人脸的参数数据,进行人脸检测
    face_cascade = cv2.CascadeClassifier(r'./detectFace/haarcascade_frontalcatface_extended.xml')
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(3, 3))

    # 绘制人脸的矩形区域(红色边框)
    for (x, y, w, h) in faces:
        # cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)
        pass

    return image[y:y + h, x:x + w]

def human_face(image):
    # 读取图片
    # image = cv2.imread(ImagePath)
    # 把图片转换为灰度模式
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 探测图片中的人脸
    # 获取训练好的人脸的参数数据,进行人脸检测
    face_cascade = cv2.CascadeClassifier(r'./detectFace/lbpcascade_frontalface.xml')
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(3, 3))

    # 绘制人脸的矩形区域(红色边框)
    for (x, y, w, h) in faces:
        # cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)
        pass

    return image[y:y + h, x:x + w],y,h,x,w



if __name__ == "__main__":
    img = cat_face()
    img1 = cv2.imread('./clothes/1.jpg')
    img1,*_ = human_face(img1)
    img = cv2.resize(img, img1.shape[:2])

    # 显示图片
    cv2.imshow('Find cat faces!', img)
    cv2.imshow('Find human faces!', img1)
    cv2.waitKey(0)