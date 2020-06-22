import requests
import simplejson
import json
import base64
import cv2
import matplotlib.pyplot as plt
import numpy as np

def find_face(imgpath):
     
    print("finding")
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    data = {"api_key": 'CN07QX7yqvvUdRXh-I1uTtO7LRgeO_gR',
        "api_secret": '_j3wIWxVyvJXk2v-UfI2EgrOrDmWurys', "image_url": imgpath, "return_landmark": 1}
    files = {"image_file": open(imgpath, "rb")}
    response = requests.post(http_url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = json.JSONDecoder().decode(req_con)
    this_json = simplejson.dumps(req_dict)
    this_json2 = simplejson.loads(this_json)
    faces = this_json2['faces']
    list0 = faces[0]
    rectangle = list0['face_rectangle']
    # print(rectangle)
    return rectangle

#number表示换脸的相似度
def merge_face(image_url_1,image_url_2,image_url,number):
    ff1 = find_face(image_url_1)
    ff2 = find_face(image_url_2)
    rectangle1 = str(str(ff1['top']) + "," + str(ff1['left']) + "," + str(ff1['width']) + "," + str(ff1['height']))
    rectangle2 = str(ff2['top']) + "," + str(ff2['left']) + "," + str(ff2['width']) + "," + str(ff2['height'])
    url_add = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"
    f1 = open(image_url_1, 'rb')
    f1_64 = base64.b64encode(f1.read())
    f1.close()
    f2 = open(image_url_2, 'rb')
    f2_64 = base64.b64encode(f2.read())
    f2.close()
    data = {"api_key": 'CN07QX7yqvvUdRXh-I1uTtO7LRgeO_gR', "api_secret": '_j3wIWxVyvJXk2v-UfI2EgrOrDmWurys',
        "template_base64": f1_64, "template_rectangle": rectangle1,
        "merge_base64": f2_64, "merge_rectangle": rectangle2, "merge_rate": number}
    response = requests.post(url_add, data=data)
    req_con = response.content.decode('utf-8')
    req_dict = json.JSONDecoder().decode(req_con)
    result = req_dict['result']
    imgdata = base64.b64decode(result)
    file = open(image_url, 'wb')
    file.write(imgdata)
    file.close()

def test(a,you):
    b = '.png'
    c = a+b
    image1 = you
    image2 = c #被换
    image = r"yuemm.jpg"   #结果
    merge_face(image2,image1,image,90)

    img1 = cv2.imread(you)
    cv2.namedWindow("a", 0)
    cv2.resizeWindow("a", 640, 480)
    cv2.imshow('a',img1)

    img2 = cv2.imread(c)
    cv2.namedWindow("b", 0)
    cv2.resizeWindow("b", 300, 600)
    cv2.imshow('b', img2)

    img3 = cv2.imread('yuemm.jpg')
    cv2.namedWindow("c", 0)
    cv2.resizeWindow("c", 300, 600)
    cv2.imshow('c', img3)

    while True:
        if cv2.waitKey(10) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

'''
    #图片显示
    plt.figure(1)
    lena1 = plt.imread('yue.jpg')
    plt.imshow(lena1)
    
    plt.figure(2)
    lena2 = plt.imread('baby1.jpg')
    plt.imshow(lena2)
    plt.figure(3)
    lena3 = plt.imread('yuemm.jpg')
    plt.imshow(lena3)
    #plt.axis('off')
    
    plt.show()
    '''




    



    


    
    

    
