import requests
import simplejson
import json
import base64
import cv2
import time
import speech_recognition as sr
import logging
from aip import AipSpeech
global p
F=0
T=1
p=F
pd0 = cv2.imread('b1.jpg')
pd1 = cv2.imread('b2.jpg')
pd2= cv2.imread('b3.jpg')
pd='b2.jpg'
x0 = 'face-change0.jpg'
x1 = 'face-change1.jpg' 
BAIDU_APP_ID = '19166265'
BAIDU_API_KEY = 'pIQlVZYLO4aPDLM55GGMGe5L'
BAIDU_SECRET_KEY = '-------------'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

def find_face(imgpath):     
    print("finding")     
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'     
    data = {"api_key": 'bimR1xFnmffX3Cs34DftMZ2t_ke2ysPG',
        "api_secret": '---------', "image_url": imgpath, "return_landmark": 1}     
    files = {"image_file": open(imgpath, "rb")}     
    response = requests.post(http_url, data=data, files=files)     
    req_con = response.content.decode('utf-8')     
    req_dict = json.JSONDecoder().decode(req_con)    
    this_json = simplejson.dumps(req_dict)     
    this_json2 = simplejson.loads(this_json)     
    faces = this_json2['faces']     
    list0 = faces[0]     
    rectangle = list0['face_rectangle']      
    return rectangle
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
    data = {"api_key": 'bimR1xFnmffX3Cs34DftMZ2t_ke2ysPG', "api_secret": '--------------',
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
def change(m,n,name):               
    merge_face(n,m,name,95)
   
change(x1,pd,'zxy.jpg')
change(x0,pd,'lzl.jpg')
zxy= cv2.imread('zxy.jpg')
lzl= cv2.imread('lzl.jpg')
while True:
    print('>>>>>>录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print('>>>>>>识别中...')
    start_time = time.time()
    audio_data = audio.get_wav_data()
    ret = aip_speech.asr(audio_data, 'wav', 16000, {'dev_pid': 1537, }) 
    if ret and ret['err_no'] == 0:
        result = ret['result'][0]
        print(result)
        end_time = time.time()
        if result=='黑色。':
            cv2.imshow('result',pd0)
        elif result=='白色。':
            cv2.imshow('result',pd1)
        elif result=='黄色。':
            cv2.imshow('result',pd2)
        elif result=='林志玲。':
            cv2.imshow('result',lzl)
        elif result=='张学友。':      
            cv2.imshow('result',zxy)
        if cv2.waitKey(10)&0xFF==27:
            break
        pd = cv2.imread('pd.jpg')  
    else:
        print(" ")
