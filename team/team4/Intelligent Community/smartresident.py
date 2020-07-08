import mcpi.minecraft as minecraft
import mcpi.block as block
import QRcode as qr
import time
import baidusound as bd
import expressdata as ex
import threading
import shibiechepai as sb
import face_reco_from_camera as face
import light
import outsidelight as olight
import expressbox as exbx
import zhineng as zn
import park.Car as car
import mccar
import lightshow as show
import warning
from twilio.rest import Client

def sms(text):
    account_sid = "AC396d7259db0517bbd6930ae267cc61f8"
    auth_token  = "88bb564ec34ca0d668cb5871422ac8ce"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to='+8617621776825',
        from_="+12057230906",
        body=text)

mc=minecraft.Minecraft.create('47.100.46.95',4784)
entityId= mc.getPlayerEntityId("W")

pos=mc.entity.getTilePos(entityId)
a=face.Face_Recognizer()
#位置检测。在某处站定3秒则触发功能
exbx.clear("standstate.txt")
exbx.clear("roomnumber.txt")
exbx.clear("closecap.txt")
global end
end=[1,1,1,1]

def detectpos_short(x,y,z):
    global pos
    if pos.x==x and pos.y==y and pos.z==z:
        return 1
    else:
        return 0

def detectpos(x,y,z):
    global pos,entityId
    if pos.x==x and pos.y==y and pos.z==z:
        for i in range(5):
            mc.postToChat(str(i+1))
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if pos.x==x and pos.y==y and pos.z==z:
            return 1
    else:
        return 0

#进_车牌识别开道闸
def car_in():
    global end
    if detectpos(1250,4,1148)==1 or detectpos(1251,4,1148)==1:
        sb.detect(1)
        mc.setBlock(1249,5,1149,152)
        mc.setBlock(1252,5,1149,152)
        time.sleep(5)
        mc.setBlock(1249,5,1149,251,0)
        mc.setBlock(1252,5,1149,251,0)
        time.sleep(5)
    end[0]=1
#出_车牌识别开道闸
def car_out():
    global end
    if detectpos(1244,4,1150)==1 or detectpos(1243,4,1150)==1:
        sb.detect(2)
        mc.setBlock(1242,5,1149,152)
        mc.setBlock(1245,5,1149,152)
        time.sleep(5)
        mc.setBlock(1242,5,1149,251,0)
        mc.setBlock(1245,5,1149,251,0)
        time.sleep(5)
    end[0]=1

#二维码识别快递员进门
def courierdetect():
    if detectpos(1284,4,1177)==1:
        if qr.detect(1)==1:
            #开门
            mc.setBlock(1285,7,1179,152)
            time.sleep(5)
            #关门
            mc.setBlock(1285,7,1179,155,2)
    if detectpos(1208,4,1177)==1:
        if qr.detect(2)==1:
            #开门
            mc.setBlock(1209,7,1179,152)
            time.sleep(5)
            #关门
            mc.setBlock(1209,7,1179,155,2)
            time.sleep(5)
    end[1]=1

#人脸识别用户进门
def ownerdetect():
    if detectpos(1286,4,1177)==1:
        if a.run()==1:
            #开门
            mc.setBlock(1285,7,1179,152)
            time.sleep(5)
            #关门
            mc.setBlock(1285,7,1179,155,2)
    if detectpos(1210,4,1177)==1:
        if a.run()==2:
            #开门
            mc.setBlock(1209,7,1179,152)
            time.sleep(5)
            #关门
            mc.setBlock(1209,7,1179,155,2)
            time.sleep(5)
    end[2]=1

#快递员录入信息
def inputinfo():
    if detectpos(1254,4,1148)==1:
        ex.info()
        time.sleep(5)
    end[3]=1

def firedetect():
    state=0
    info1=list(mc.getBlocks(1229,3,1178,1190,23,1192))
    info2=list(mc.getBlocks(1305,3,1178,1266,23,1192))
    info=info1+info2
    if 51 in info:
        bd.speak("楼内着火，请拨打火警")
        if state==0:
            sms("您所在的居民楼现有火情，请注意避险")
            state=1
    else:
        state=0
        # f = open('C:\\Users\\23004\\AppData\\Roaming\\.homeassistant\\custom_components\\state.txt','w')
        # f.write('dangerous')
    # else:
    #     f = open('C:\\Users\\23004\\AppData\\Roaming\\.homeassistant\\custom_components\\state.txt','w')
    #     f.write('safe')        


light.main()
exbx.main()
zn.main()
car.main()
#mccar.main()
show.main()
warning.main()
while True:
    pos=mc.entity.getTilePos(entityId)
    car_in()
    car_out()
    courierdetect()
    inputinfo()
    firedetect()
    ownerdetect()
    firedetect()
    olight.lightctrl()