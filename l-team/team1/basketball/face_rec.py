from aip import AipFace
import base64



""" 你的 APPID AK SK """
APP_ID = '20367263'
API_KEY = '3GjtbAC0ySZQakKCkTu2LVBt'
SECRET_KEY = 'mSYkFDI5r8R4KeCMvdTns6YGdB4ISRHD'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


# 人脸检测
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


# 人脸注册
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


# 人脸更新
def face_update(file_path,userID,groupIdnew):

    with open(file_path,'rb') as f:
        pic = f.read()

    import base64
    image = str(base64.b64encode(pic), "utf-8")
    # image = "取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串"

    imageType = "BASE64"

    groupId = groupIdnew

    userID = str(userID)
    userId = userID

    """ 调用人脸更新 """
    client.updateUser(image, imageType, groupId, userId)

    """ 如果有可选参数 """
    options = {}
    options["user_info"] = "user's info"
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "LOW"

    """ 带参数调用人脸更新 """
    return client.updateUser(image, imageType, groupId, userId, options)


# 人脸删除
def face_delete(userID,groupID):
    # 进行人脸删除时要注意提前进行身份验证
    userId = userID

    groupId = groupID

    """ 调用用户信息查询 """
    return client.getUser(userId, groupId)


if __name__ == '__main__':
    file_path = './test.jpg'
    a = face_delete("wzy","wzy")
    print(a) #提取相似度
