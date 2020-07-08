import cv2
from aip import AipFace
import base64
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
APP_ID='20568324'
API_KEY='LcSNDhFKyjVUQksZs1vu0c76'
SECRET_KEY='hlR0bBfAeHWPDrrWiF4BPVnTAw9H8dQ5'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

#cap = cv2.VideoCapture(0)

def face_register(file_path,groupIdnew,userIdnew):
    with open(file_path,'rb') as f:
        pic = f.read()

    import base64
    image = str(base64.b64encode(pic), "utf-8")
    # image = "取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串"

    imageType = "BASE64"

    #这里是你在后台创建的一个应用，然后自己命名，最多创建100个，然后里面是一个一个的用户id
    groupId = groupIdnew

    #用户id
    userId = userIdnew

    """ 如果有可选参数 """
    options = {}
    options["user_info"] = "user's info"
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "LOW"

    """ 带参数调用人脸注册 """
    return client.addUser(image, imageType, groupId, userId, options)

def face_test(file_path,groupIdold):
    with open(file_path,'rb') as f:
        pic = f.read()
    
    image = str(base64.b64encode(pic), "utf-8")
    # image = "取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串"

    imageType = "BASE64"

   #""" 调用人脸检测 """
   # client.detect(image, imageType)

    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age"
    options["max_face_num"] = 2
    options["face_type"] = "LIVE"

    """ 带参数调用人脸搜索 """
    return client.search(image, imageType,groupIdold)

def face_in():
    cap = cv2.VideoCapture(0)
    num = 1
    people = 1
    speaker.Speak("欢迎光临")
    while True:
        ret, frame = cap.read()
        cv2.imshow("frame",frame)
        cv2.imencode('.jpg',frame)[1].tofile(str(people)+'_'+str(num)+".jpg") #存图片
        face_register('./'+str(people)+'_'+str(num)+".jpg",str(people),str(num)) #人脸注册
        num += 1 
        cv2.waitKey(1000)
        if num>2: #读取两张图片
            people += 1
            break
    cap.release()
    cv2.destroyAllWindows()

def face_out():
    cap = cv2.VideoCapture(0)
    people = 1
    while True:
        ret, frame = cap.read()
        cv2.imshow("frame",frame)
        cv2.waitKey(1000)
        cv2.imencode('.jpg',frame)[1].tofile("new"+".jpg") #存图片
        facedata = face_test('./new.jpg',people)#人脸识别
        break
    cap.release()
    cv2.destroyAllWindows()
    if(int(facedata['result']['user_list'][0]['score'])>40):
        speaker.Speak("谢谢惠顾")
    else:
        speaker.Speak("不存在此人")

