import cv2
from aip import AipOcr
import serial
import tkinter
#from os import system
import os
import win32com.client
from pygame import mixer # Load the required library


APP_ID = '20329897'
API_KEY = 'z8D0PlnOuGxSMg9LgA3wNNBN'
SECRET_KEY = 'SyLQ39pw7c7ngqw8qhStQXo4h1n8ZrRv'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
x=0
y=0
def play():
    mixer.init()
    mixer.music.load('8813.wav')
    mixer.music.play()
def feedback():
    sign_up = tkinter.Toplevel(top)
    sign_up.geometry("500x495")
    tkinter.Label(sign_up, text='如有产品问题或建议,请联系开发者', font=('Times', 16,'bold')).place(x=25, y=40)
    tkinter.Label(sign_up, text='email:  cjy110@yeah.net', font=('Times', 14)).place(x=30, y=125)
    tkinter.Label(sign_up, text='QQ: 1305564441', font=('Times', 14)).place(x=30, y=190)
    #tkinter.Label(sign_up, text='', font=('Times', 14)).place(x=30, y=140)
def create():
    sign_up = tkinter.Toplevel(top)
    sign_up.geometry("500x495")
    def camera():
        global x
        global y
        ii=0
        key=['','']
        cap=cv2.VideoCapture(0)
        while True:
            ret,frame=cap.read()
            cv2.imshow('Video',frame)
            cv2.imwrite('q.jpg',frame)
            with open('q.jpg','rb') as f:
                image=f.read()
                text=client.basicAccurate(image)
           #     text=client.basicGeneral(image)
            for i in text.get('words_result'):
                key[ii]=i.get('words')
                ii+=1
                if ii==2:
                    ii=0
            red=key[0]
            black=key[1]
            if cv2.waitKey(1)&0xFF==ord('q')or len(black)>1:
                break
            print(key[0],key[1])
        cap.release()
        cv2.destroyAllWindows()
       # print('out')
        dic=dict(地雷=12,司令=11, 军长=10, 师长=9,旅长=8,团长=7,营长=6,连长=5,排长=4,工兵=3,爆破=2)
      #  print(dic.get(red))
        if red=='炸弹'or black=='炸弹':
            black='爆破'
            red=black
        elif red=='地雷'and black=='工兵':
            red='爆破'
        elif black=='地雷'and red=='工兵':
            black='爆破'
        if red=='军旗':
            play()
            tkinter.Label(sign_up, text='黑方胜', font=('Times', 28,'bold'),bg='yellow',wraplength = 1,anchor = 'w').place(x=220, y=140)
            
        elif black=='军旗':
     
            tkinter.Label(sign_up, text='红方胜', font=('Times', 28,'bold'),bg='yellow',wraplength = 1,anchor = 'w').place(x=220, y=140)
            play()
        elif len(black)>1 and dic.get(red)>dic.get(black):
            print(red,'赢')
            tkinter.Label(sign_up, text='红方留子', font=('Times', 20,'bold'),bg='white',wraplength = 1,anchor = 'w').place(x=220, y=140)
            x+=1
            tkinter.Label(sign_up, text='伤亡:%d'%x, font=('Times', 18,'bold')).place(x=335, y=200)
            speaker.Speak('红方留子')
            #play('红方留子.wav')
        elif len(black)>1 and dic.get(red)==dic.get(black):
            print('平')
            x+=1
            y+=1
            tkinter.Label(sign_up, text='同归于尽', font=('Times', 20,'bold'),bg='white',wraplength = 1,anchor = 'w').place(x=220, y=140)
            tkinter.Label(sign_up, text='伤亡:%d'%y, font=('Times', 18,'bold')).place(x=55, y=200)
            tkinter.Label(sign_up, text='伤亡:%d'%x, font=('Times', 18,'bold')).place(x=335, y=200)
            speaker.Speak('同归于尽')
          #play('同归于尽.wav')
        else:
            print(black,'黑赢')
            y+=1
            tkinter.Label(sign_up, text='黑方留子', font=('Times', 20,'bold'),bg='white',wraplength = 1,anchor = 'w').place(x=220, y=140)
            tkinter.Label(sign_up, text='伤亡:%d'%y, font=('Times', 18,'bold')).place(x=55, y=200)
            speaker.Speak('黑方留子')
          #  play('黑方留子.wav')
    tkinter.Label(sign_up, text='对局1', font=('Times', 20,'bold')).place(x=205, y=40)
    tkinter.Label(sign_up, text='红方', font=('Times', 16,'bold'),fg='red').place(x=65, y=110)
    tkinter.Label(sign_up, text='黑方', font=('Times', 16,'bold')).place(x=345, y=110)
    login = tkinter.Button(sign_up, text='判断胜负',font=('Times', 20,'bold'), command=camera)
    login.place(x=175, y=350)

top = tkinter.Tk()
top.title('智能军师')
top.geometry("500x495")
label_text = tkinter.Label(top)
label_text.pack()
img_png = tkinter.PhotoImage(file='logo.gif')
label_img = tkinter.Label(top, image=img_png)
label_img.pack()
tkinter.Label(top, text='Copyright© 2020-2020 曹嘉扬', font=('Times', 10)).place(x=160, y=467)
tkinter.Label(top, text='V1.0', font=('Times', 12)).place(x=315, y=445)
tkinter.Label(top, text='欢迎使用智能军师', font=('Times', 16,'bold')).place(x=135, y=440)
btn_login = tkinter.Button(top, text='用户反馈',font=('Times', 22,'bold'),command=feedback)
btn_login.place(x=275, y=360)
btn_login = tkinter.Button(top, text='新建对局',font=('Times', 22,'bold'),command=create)
btn_login.place(x=80, y=360)


