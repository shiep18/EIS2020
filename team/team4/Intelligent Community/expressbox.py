import box_vtk
import recognition
import threading
import expressboxinfo
from mcpi.minecraft import Minecraft
def clear(name):
    u = open("C:\\Users\\23004\\AppData\\Roaming\\.homeassistant\\custom_components\\"+name,'r+')
    u.truncate()
    u.close() 

def query(name):
    u = open("C:\\Users\\23004\\AppData\\Roaming\\.homeassistant\\custom_components\\"+name,'r+')
    check=u.read()
    u.close()
    return check 

def writetxt(name,info):
    u = open("C:\\Users\\23004\\AppData\\Roaming\\.homeassistant\\custom_components\\"+name,'w')
    u.write(info)
    u.close()
    
def recognition_job():
    while True:
        check=query("standstate.txt")
        room=recognition.detectpos()
        #print(room)
        n=expressboxinfo.express_info(str(room))
        a=query("closecap.txt")
        if room==1 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==2 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==3 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==4 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==5 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==6 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==7 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==8 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==9 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==10 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==11 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)
        if room==12 and n[2]=='0' and a=="" and check=="":
            recognition.detect(room)

def box_vtk_job():
    while True:
        
        room=box_vtk.detectpos()
        #print(room)
        writetxt("roomnumber.txt",str(room))
        check=query("standstate.txt")
        if check=="":
            if room==1 or room==2 or room==3 or room==4 or room==5  or room==6 or room==7 or room==8 or room==9 or room==10 or room==11 or room==12:
                writetxt("standstate.txt","stand")
                box_vtk.main()
                while True:
                    mc=Minecraft.create("47.100.46.95",4784)
                    entityId= mc.getPlayerEntityId("W")
                    pos=mc.entity.getTilePos(entityId)
                    x=pos.x
                    y=pos.y
                    z=pos.z
                    #time.sleep(0.1)
                    pos=mc.entity.getTilePos(entityId)
                    if x!=pos.x or y!=pos.y or z!=pos.z:
                        clear("standstate.txt")
                        break
def main():
    first_thread=threading.Thread(target=recognition_job,name='T1')
    first_thread.start()
    second_thread=threading.Thread(target=box_vtk_job,name='T2')
    second_thread.start()
    #print(threading.active_count())
    #print(threading.enumerate())
    #print(threading.current_thread())

if __name__=='__main__':
    main()
    
