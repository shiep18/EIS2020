import numpy as np
import gym
import cv2
import time
import tkinter as tk
import win32api,win32com,win32com.client
#from gym.spaces import Discrete
from PIL import Image,ImageTk,ImageDraw,ImageFont
#from threading import Thread
#from torchvision import transforms
top=tk.Tk()
speaker = win32com.client.Dispatch("SAPI.SpVoice")

class SnakeEnv(gym.Env):
    SIZE=100 # 格子数量
  
    def __init__(self, ladder_num, dices,playernum,kkk):
        #print('c')
        font = ImageFont.truetype('arial.ttf',24) 
        self.img=np.zeros((700,700,3),np.uint8)
        self.img[:]=[200,5,100]
        #self.chess=np.zeros((3,3),np.int8)
        for i in range(11):
            cv2.line(self.img,(50,50+i*60),(650,50+i*60),(250,230,200),3)
        for j in range(11):
            cv2.line(self.img,(50+j*60,50),(50+j*60,650),(250,230,200),3)
        self.ladder_num = ladder_num #梯子数量
        self.dices = dices # 骰子数量
        self.flag=0
        self.playernum=playernum
        self.kkk=kkk
        self.pd=1
        while self.flag!=10:
            self.flag=0
            self.ladders = dict(np.random.randint(1, self.SIZE-1, size=(self.ladder_num, 2))) # 生成梯子，格式类似{78: 33, 52: 97, 71: 64, 51: 32}
            #self.observation_space=Discrete(self.SIZE+1)
            #self.action_space=Discrete(len(dices))
            print(self.ladders)
            keys = self.ladders.keys()
            values=self.ladders.values()
            #print(list(keys))
            #print(list(values))
            lads=[]
            for key in keys:
                if key not in lads:
                    self.flag+=1
                    lads.append(key)
            for value in values:
                if value not in lads:
                    lads.append(value)
                    self.flag+=1
            print(lads)
            if self.flag!=10:
                print('有重复，重新搭梯！')
        if self.flag==10:
            #print('a')
            print('搭梯完成，开始游戏！')
            for k in list(keys): # 将梯子反过来存一遍
                self.ladders[self.ladders[k]] = k   
            jishu=0
            self.a=[0,0,0,0,0,0,0,0,0,0]
            for k in list(keys):
                self.a[jishu]=k
                jishu+=1
                print(k)
            self.color=[[112,122,254],[86,248,252],[138,232,106],[226,108,230],[174,168,164],[200,5,100]]
            for jishu in range(5):
                alength1=(self.a[jishu]-1)//10
                alength2=(self.a[5+jishu]-1)//10
                if alength1%2==0:
                    awidth1=(self.a[jishu]-1)%10
                elif alength1%2!=0:
                    awidth1=9-(self.a[jishu]-1)%10
                #print(width1,length1)
                if alength2%2==0:
                    awidth2=(self.a[jishu+5]-1)%10
                elif alength2%2!=0:
                    awidth2=9-(self.a[jishu+5]-1)%10
                self.img[51+alength1*60:49+(alength1+1)*60,51+awidth1*60:49+(awidth1+1)*60]=self.color[jishu]
                self.img[51+alength2*60:49+(alength2+1)*60,51+awidth2*60:49+(awidth2+1)*60]=self.color[jishu]
            
            #cv2.imwrite('000.jpg',self.img)
            #img1 = Image.open("E:\zhu\\000.jpg")
            self.img = Image.fromarray(self.img)
            #self.img1 = Image.fromarray(self.img)
            draw = ImageDraw.Draw(self.img)
            num=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
            for case in range(100):
                alength1=(case)//10
                if alength1%2==0:
                    awidth1=(case)%10
                elif alength1%2!=0:
                    awidth1=9-(case)%10
                draw.text((55+awidth1*60,55+alength1*60),num[case], fill=(0,0,0),font=font)
            #self.img.show()
            self.img = np.array(self.img)
            cv2.imwrite('000.jpg',self.img)
            cv2.imshow('Snake Ladder Chess',self.img)
            #img1.save('001.jpg')
            print ('ladders info:')
            print (self.ladders)

    def reset(self):
        self.img=cv2.imread('000.jpg')
        #self.img = Image.fromarray(cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB))
        #self.img = numpy.array(self.img)
        self.pd=1
        self.pos = 0 # 白色位置重置为0
        self.pos1 = 0 # 黑色位置重置为0
        self.pos2 = 0 # 红色位置重置为0
        self.pos3 = 0 # 黄色位置重置为0
        self.width1=0
        self.width2=0
        self.width3=0
        self.width4=0
        self.length1=-1
        self.length2=-1
        self.length3=-1
        self.length4=-1
        if self.playernum==2:
            cv2.circle(self.img,(90+self.width1*60,70+self.length1*60),(10),(255,255,255),-1)
            cv2.circle(self.img,(90+self.width2*60,90+self.length2*60),(10),(0,0,0),-1)
        elif self.playernum==3:
            cv2.circle(self.img,(90+self.width1*60,70+self.length1*60),(10),(255,255,255),-1)
            cv2.circle(self.img,(90+self.width2*60,90+self.length2*60),(10),(0,0,0),-1)
            cv2.circle(self.img,(70+self.width3*60,70+self.length3*60),(10),(0,0,255),-1)
        elif self.playernum==4:
            cv2.circle(self.img,(90+self.width1*60,70+self.length1*60),(10),(255,255,255),-1)
            cv2.circle(self.img,(90+self.width2*60,90+self.length2*60),(10),(0,0,0),-1)
            cv2.circle(self.img,(70+self.width3*60,70+self.length3*60),(10),(0,0,255),-1)
            cv2.circle(self.img,(70+self.width3*60,90+self.length3*60),(10),(0,255,255),-1)
        cv2.imshow('Snake Ladder Chess',self.img)
        if self.kkk==1:
            print('游戏重新开始！')
            print('轮到白色了！')
        elif self.kkk==0:
            print('游戏开始！')
            print('轮到白色了！')
            self.kkk=1
        #return self.pos
    def player(self):
        if self.playernum==2:
            self.img=cv2.imread('000.jpg')      
            self.length1=(self.pos-1)//10
            if self.length1%2==0:
                self.width1=(self.pos-1)%10
            elif self.length1%2!=0:
                self.width1=9-((self.pos-1)%10)
            cv2.circle(self.img,(90+self.width1*60,70+self.length1*60),(10),(255,255,255),-1)
            #######
            self.length2=(self.pos1-1)//10
            if self.length2%2==0:
                self.width2=(self.pos1-1)%10
            elif self.length2%2!=0:
                self.width2=9-((self.pos1-1)%10)
            cv2.circle(self.img,(90+self.width2*60,90+self.length2*60),(10),(0,0,0),-1)
        elif self.playernum==3:
            self.img=cv2.imread('000.jpg')      
            self.length1=(self.pos-1)//10
            if self.length1%2==0:
                self.width1=(self.pos-1)%10
            elif self.length1%2!=0:
                self.width1=9-((self.pos-1)%10)
            cv2.circle(self.img,(90+self.width1*60,70+self.length1*60),(10),(255,255,255),-1)
            #######
            self.length2=(self.pos1-1)//10
            if self.length2%2==0:
                self.width2=(self.pos1-1)%10
            elif self.length2%2!=0:
                self.width2=9-((self.pos1-1)%10)
            cv2.circle(self.img,(90+self.width2*60,90+self.length2*60),(10),(0,0,0),-1)
            #######
            self.length3=(self.pos2-1)//10
            if self.length3%2==0:
                self.width3=(self.pos2-1)%10
            elif self.length3%2!=0:
                self.width3=9-((self.pos2-1)%10)
            cv2.circle(self.img,(70+self.width3*60,70+self.length3*60),(10),(0,0,255),-1)
            #######
        elif self.playernum==4:
            self.img=cv2.imread('000.jpg')      
            self.length1=(self.pos-1)//10
            if self.length1%2==0:
                self.width1=(self.pos-1)%10
            elif self.length1%2!=0:
                self.width1=9-((self.pos-1)%10)
            cv2.circle(self.img,(90+self.width1*60,70+self.length1*60),(10),(255,255,255),-1)
            #######
            self.length2=(self.pos1-1)//10
            if self.length2%2==0:
                self.width2=(self.pos1-1)%10
            elif self.length2%2!=0:
                self.width2=9-((self.pos1-1)%10)
            cv2.circle(self.img,(90+self.width2*60,90+self.length2*60),(10),(0,0,0),-1)
            #######
            self.length3=(self.pos2-1)//10
            if self.length3%2==0:
                self.width3=(self.pos2-1)%10
            elif self.length3%2!=0:
                self.width3=9-((self.pos2-1)%10)
            cv2.circle(self.img,(70+self.width3*60,70+self.length3*60),(10),(0,0,255),-1)
            #######
            self.length4=(self.pos3-1)//10
            if self.length4%2==0:
                self.width4=(self.pos3-1)%10
            elif self.length4%2!=0:
                self.width4=9-((self.pos3-1)%10)
            cv2.circle(self.img,(70+self.width4*60,90+self.length4*60),(10),(0,255,255),-1)
        cv2.imshow('Snake Ladder Chess',self.img)
    def test(self):
        cv2.imshow('Snake Ladder Chess',self.img)
    def step(self,aa):
        global pdd
        #cv2.imshow('result',self.img)
        if self.pd==1:
            pdd=1
            self.aa=aa
            step = np.random.randint(1, self.dices[self.aa] + 1) # 根据选择的骰子进行投掷
            print("白色玩家筛了一个: %d" % step)
            self.pos += step
            if self.pos < 100:
                env.player()
            elif self.pos == 100:
                env.player()
                self.pd=-1
                print('White WIN! Game over! ')
                env.g1()
                return 100, 100, 1, 0, {} # 到达位置100，终止游戏
            elif self.pos > 100:
                self.pos = 200 - self.pos # 超过100时要向回走
                env.player()
            if self.pos in self.ladders:
                self.pos = self.ladders[self.pos] # 遇到梯子要前进到梯子的另一头
                env.player()
            self.pd=2
            return self.pos, -1, 0, 1, {}
        elif self.pd==-1:
            print("无效！")
        elif self.pd==2:
            print("无效！！！请黑色玩家筛骰子！")
        elif self.pd==3:
            print("无效！！！请红色玩家筛骰子！")
        elif self.pd==4:
            print("无效！！！请黄色玩家筛骰子！")
        return self.pos, -1, 0, 0,{}
    def step1(self, aa):
        global pdd
        #cv2.imshow('result',self.img)
        if self.pd==2:
            pdd=1
            self.aa=aa
            step1 = np.random.randint(1, self.dices[aa] + 1) # 根据选择的骰子进行投掷
            self.pos1 += step1
            print("黑色玩家筛了一个: %d" % step1)
            if self.pos1 < 100:
                env.player()
            elif self.pos1 == 100:
                self.pd=-1
                env.player()
                print('Black WIN! Game over! ')
                env.g2()
                return 100, 100, 1, 0, {} # 到达位置100，终止游戏
            elif self.pos1 > 100:
                self.pos1 = 200 - self.pos1 # 超过100时要向回走
                env.player()
            if self.pos1 in self.ladders:
                self.pos1 = self.ladders[self.pos1] # 遇到梯子要前进到梯子的另一头
                env.player()
            if self.playernum==2:
                self.pd=1
            elif self.playernum==3 or self.playernum==4:
                self.pd=3
            return self.pos1, -1, 0, 1, {}
        elif self.pd==-1:
            print("无效！")
        elif self.pd==1 or self.pd==0 :
            print("无效！！！请白色玩家筛骰子！")
        elif self.pd==3:
            print("无效！！！请红色玩家筛骰子！")
        elif self.pd==4:
            print("无效！！！请黄色玩家筛骰子！")
        return self.pos1, -1, 0, 0, {}
    def step2(self, aa):
        global pdd
        #cv2.imshow('result',self.img)
        if self.pd==3:
            pdd=1
            self.aa=aa
            step2 = np.random.randint(1, self.dices[aa] + 1) # 根据选择的骰子进行投掷
            self.pos2 += step2
            print("红色玩家筛了一个: %d" % step2)
            if self.pos2 < 100:
                env.player()
            elif self.pos2 == 100:
                self.pd=-1
                env.player()
                print('Red WIN! Game over! ')
                env.g3()
                return 100, 100, 1, 0, {} # 到达位置100，终止游戏
            elif self.pos2 > 100:
                self.pos2 = 200 - self.pos2 # 超过100时要向回走
                env.player()
            if self.pos2 in self.ladders:
                self.pos2 = self.ladders[self.pos2] # 遇到梯子要前进到梯子的另一头
                env.player()
            if self.playernum==3:
                self.pd=1
            elif self.playernum==4:
                self.pd=4
            return self.pos2, -1, 0, 1, {}
        elif self.pd==-1:
            print("无效！")
        elif self.pd==1 or self.pd==0 :
            print("无效！！！请白色玩家筛骰子！")
        elif self.pd==2:
            print("无效！！！请黑色玩家筛骰子！")
        elif self.pd==4:
            print("无效！！！请黄色玩家筛骰子！")
        return self.pos2, -1, 0, 0, {}
    def step3(self, aa):
        global pdd
        #cv2.imshow('result',self.img)
        if self.pd==4:
            self.pd=-1
            pdd=1
            self.aa=aa
            step3 = np.random.randint(1, self.dices[aa] + 1) # 根据选择的骰子进行投掷
            self.pos3 += step3
            print("黄色玩家筛了一个: %d" % step3)
            if self.pos3 < 100:
                env.player()
            elif self.pos3 == 100:
                env.player()
                print('Yellow WIN! Game over! ')
                env.g4()
                return 100, 100, 1, 0, {} # 到达位置100，终止游戏
            elif self.pos3 > 100:
                self.pos3 = 200 - self.pos3 # 超过100时要向回走
                env.player()
            if self.pos3 in self.ladders:
                self.pos3 = self.ladders[self.pos3] # 遇到梯子要前进到梯子的另一头
                env.player()
            self.pd=1
            return self.pos3, -1, 0, 1, {}
        elif self.pd==-1:
            print("无效！")
        elif self.pd==1 or self.pd==0 :
            print("无效！！！请白色玩家筛骰子！")
        elif self.pd==2:
            print("无效！！！请黑色玩家筛骰子！")
        elif self.pd==3:
            print("无效！！！请红色玩家筛骰子！")
        return self.pos3, -1, 0, 0, {}
    def render(self):
        pass # 不进行图形渲染
    def g1(self):
        while True:
            try:
                speaker.Speak("白色获胜，游戏结束")
                break
            except:
                pass
    def g2(self):
        while True:
            try:
                speaker.Speak("黑色获胜，游戏结束")
                break
            except:
                pass
    def g3(self):
        while True:
            try:
                speaker.Speak("红色获胜，游戏结束")
                break
            except:
                pass
    def g4(self):
        while True:
            try:
                speaker.Speak("黄色获胜，游戏结束")
                break
            except:
                pass

def two():
    global env,pdd
    env = SnakeEnv(5, [3,6],2,0) # 5个梯子，2个筛子最大值分别是3和6,1为第一次
    '''
    Thread(target=env.g1).start()
    Thread(target=env.g2).start()
    '''
    env.reset()
    def shake():
        print("白色玩家使用了普通筛子。")
        state, reward, terminate, pdd, _ = env.step(1) # 选择正常的骰子
        print ("白色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到黑色了！')
            pdd=0
    def shake1():
        print("白色玩家使用了重复筛子。")
        state, reward, terminate, pdd, _ = env.step(0) # 选择重复骰子
        print ("白色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到黑色了！')
            pdd=0
    def shake2():
        print("黑色玩家使用了普通筛子。")
        state, reward, terminate, pdd, _ = env.step1(1) # 选择正常的骰子
        print ("黑色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到白色了！')
            pdd=0
    def shake3():
        print("黑色玩家使用了重复筛子。")
        state, reward, terminate, pdd, _ = env.step1(0) # 选择重复骰子
        print ("黑色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到白色了！')
            pdd=0
    def rst():
        env.reset()
    two = tk.Toplevel(top)
    two.title("玩家控制界面")
    tk.Label(two,text="白色玩家",font=("Arial",14)).place(x=60,y=10)
    tk.Label(two,text="黑色玩家",font=("Arial",14)).place(x=240,y=10)
    two.geometry("%dx%d" %(500,500))
    btn=tk.Button(two,text="普通筛子",command=shake)
    btn.place(x=100,y=50)
    btn=tk.Button(two,text="重复筛子",command=shake1)
    btn.place(x=100,y=100)
    btn=tk.Button(two,text="普通筛子",command=shake2)
    btn.place(x=200,y=50)
    btn=tk.Button(two,text="重复筛子",command=shake3)
    btn.place(x=200,y=100)
    btn=tk.Button(two,text="reset",command=rst)
    btn.place(x=160,y=150)
    top.mainloop()
def three():
    global env,pdd
    env = SnakeEnv(5, [3,6],3,0) # 5个梯子，2个筛子最大值分别是3和6,1为第一次
    '''
    Thread(target=env.g1).start()
    Thread(target=env.g2).start()
    Thread(target=env.g3).start()
    '''
    env.reset()
    def shake():
        print("白色玩家使用了普通筛子。")
        state, reward, terminate, pdd, _ = env.step(1) # 选择正常的骰子
        print ("白色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到黑色了！')
            pdd=0
    def shake1():
        print("白色玩家使用了重复筛子。")
        state, reward, terminate, pdd, _ = env.step(0) # 选择重复骰子
        print ("白色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到黑色了！')
            pdd=0
    def shake2():
        print("黑色玩家使用了普通筛子。")
        state, reward, terminate, pdd, _ = env.step1(1) # 选择正常的骰子
        print ("黑色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到红色了！')
            pdd=0
    def shake3():
        print("黑色玩家使用了重复筛子。")
        state, reward, terminate, pdd, _ = env.step1(0) # 选择重复骰子
        print ("黑色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到红色了！')
            pdd=0
    def shake4():
        print("红色玩家使用了普通筛子。")
        state, reward, terminate, pdd, _ = env.step2(1) # 选择正常的骰子
        print ("红色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到白色了！')
            pdd=0
    def shake5():
        print("红色玩家使用了重复筛子。")
        state, reward, terminate, pdd, _ = env.step2(0) # 选择重复骰子
        print ("红色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到白色了！')
            pdd=0
    def rst():
        env.reset()
    two = tk.Toplevel(top)
    two.title("玩家控制界面")
    tk.Label(two,text="白色玩家",font=("Arial",14)).place(x=60,y=10)
    tk.Label(two,text="黑色玩家",font=("Arial",14)).place(x=240,y=10)
    tk.Label(two,text="红色玩家",font=("Arial",14)).place(x=60,y=300)
    two.geometry("%dx%d" %(500,500))
    btn=tk.Button(two,text="普通筛子",command=shake)
    btn.place(x=100,y=50)
    btn=tk.Button(two,text="重复筛子",command=shake1)
    btn.place(x=100,y=100)
    btn=tk.Button(two,text="普通筛子",command=shake2)
    btn.place(x=200,y=50)
    btn=tk.Button(two,text="重复筛子",command=shake3)
    btn.place(x=200,y=100)
    btn=tk.Button(two,text="普通筛子",command=shake4)
    btn.place(x=100,y=200)
    btn=tk.Button(two,text="重复筛子",command=shake5)
    btn.place(x=100,y=250)
    btn=tk.Button(two,text="reset",command=rst)
    btn.place(x=160,y=150)
    top.mainloop()
def four():
    global env,pdd
    env = SnakeEnv(5, [3,6],4,0) # 5个梯子，2个筛子最大值分别是3和6,1为第一次
    '''
    Thread(target=env.g1).start()
    Thread(target=env.g2).start()
    Thread(target=env.g3).start()
    Thread(target=env.g4).start()
    '''
    env.reset()
    def shake():
        print("白色玩家使用了普通筛子。")
        state, reward, terminate, pdd, _ = env.step(1) # 选择正常的骰子
        print ("白色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到黑色了！')
            pdd=0
    def shake1():
        print("白色玩家使用了重复筛子。")
        state, reward, terminate, pdd, _ = env.step(0) # 选择重复骰子
        print ("白色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到黑色了！')
            pdd=0
    def shake2():
        print("黑色玩家使用了普通筛子。")
        state, reward, terminate, pdd, _ = env.step1(1) # 选择正常的骰子
        print ("黑色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到红色了！')
            pdd=0
    def shake3():
        print("红色玩家使用了普通筛子。")
        state, reward, terminate, pdd, _ = env.step1(0) # 选择重复骰子
        print ("黑色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到红色了！')
            pdd=0
    def shake4():
        print("红色玩家使用了重复筛子。")
        state, reward, terminate, pdd, _ = env.step2(1) # 选择正常的骰子
        print ("红色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到黄色了！')
            pdd=0
    def shake5():
        state, reward, terminate, pdd, _ = env.step2(0) # 选择重复骰子
        print ("红色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到黄色了！')
            pdd=0
    def shake6():
        print("黄色玩家使用了普通筛子。")
        state, reward, terminate, pdd, _ = env.step3(1) # 选择正常的骰子
        print ("黄色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到白色了！')
            pdd=0
    def shake7():
        print("黄色玩家使用了重复筛子。")
        state, reward, terminate, pdd, _ = env.step3(0) # 选择重复骰子
        print ("黄色: %d"% state) # 打印位置
        if terminate!=1 and pdd ==1:
            print('轮到白色了！')
            pdd=0
    def rst():
        env.reset()
    two = tk.Toplevel(top)
    two.title("玩家控制界面")
    tk.Label(two,text="白色玩家",font=("Arial",14)).place(x=60,y=10)
    tk.Label(two,text="黑色玩家",font=("Arial",14)).place(x=240,y=10)
    tk.Label(two,text="红色玩家",font=("Arial",14)).place(x=60,y=300)
    tk.Label(two,text="黄色玩家",font=("Arial",14)).place(x=240,y=300)
    two.geometry("%dx%d" %(500,500))
    btn=tk.Button(two,text="普通筛子",command=shake)
    btn.place(x=100,y=50)
    btn=tk.Button(two,text="重复筛子",command=shake1)
    btn.place(x=100,y=100)
    btn=tk.Button(two,text="普通筛子",command=shake2)
    btn.place(x=200,y=50)
    btn=tk.Button(two,text="重复筛子",command=shake3)
    btn.place(x=200,y=100)
    btn=tk.Button(two,text="普通筛子",command=shake4)
    btn.place(x=100,y=200)
    btn=tk.Button(two,text="重复筛子",command=shake5)
    btn.place(x=100,y=250)
    btn=tk.Button(two,text="普通筛子",command=shake6)
    btn.place(x=200,y=200)
    btn=tk.Button(two,text="重复筛子",command=shake7)
    btn.place(x=200,y=250)
    btn=tk.Button(two,text="reset",command=rst)
    btn.place(x=160,y=150)
    top.mainloop()
if __name__=="__main__":
    bkimg=Image.open('000.jpg')
    photo = ImageTk.PhotoImage(bkimg)
    label_img = tk.Label(top, image = photo)
    label_img.pack()
    top.title('游戏模式')
    top.geometry("%dx%d" %(450,450))
    tk.Label(top,text="蛇梯棋",font=("Arial",20)).place(x=180,y=100)
    btn=tk.Button(top,text="双人游戏",command=two)
    btn.place(x=100,y=200)
    btn=tk.Button(top,text="三人游戏",command=three)
    btn.place(x=200,y=200)
    btn=tk.Button(top,text="四人游戏",command=four)
    btn.place(x=300,y=200)
    top.mainloop()


#while True:
#state, reward, terminate, _ = env.step(1) # 每次都选择正常的骰子
#time.sleep(1)
#print (reward, state) # 打印r和s
#state, reward, terminate, _ = env.step(1) # 每次都选择正常的骰子
#time.sleep(1)
#print (reward, state) # 打印r和s
#if terminate == 1:
    #break

