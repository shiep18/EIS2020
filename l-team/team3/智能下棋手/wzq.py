from time import sleep
import pygame, sys
from pygame.locals import *
from random import randint
import os
from os import system
import win32com.client
import copy
speaker = win32com.client.Dispatch("SAPI.SpVoice")
level = 15          #棋盘是15*15的
grade = 10
MAX = 100000000
co = []
def pvp(ch):
    pygame.init()   #开始game界面
    bg = 'bg1.png'
    white_image = 'white.png'
    black_image = 'black.png'   #导入图片

    screen = pygame.display.set_mode((850, 750), 0, 32) #设置屏幕大小为750*750
    background = pygame.image.load(bg).convert()        #导入背景
    white = pygame.image.load(white_image).convert_alpha()  #导入白棋，保留背景
    black = pygame.image.load(black_image).convert_alpha()  #导入黑棋，保留背景
    white = pygame.transform.smoothscale(white, (int(white.get_width() * 1.5), int(white.get_height() * 1.5)))
    black = pygame.transform.smoothscale(black, (int(black.get_width() * 1.5), int(black.get_height() * 1.5)))  #重新定义棋子大小

    screen.blit(background, (0, 0)) #设置背景，及背景坐标
    font = pygame.font.SysFont("黑体", 40)    #设置字体及大小
    
    pygame.event.set_allowed([MOUSEBUTTONDOWN, MOUSEBUTTONUP]) #允许鼠标点击

    dot_list = [(25 + i * 50 - white.get_width() / 2, 25 + j * 50 - white.get_height() / 2) for i in range(level) for
                j in range(level)]  #所有棋盘上可下的点的坐标列表
    color = -1  #颜色标志
    times = 0   #时间初始值
    flag = False    #游戏继续标志（目前未涉及，可以添加按钮后再做修改）
    while not flag: #五子棋主循环
        for event in pygame.event.get():    #遍历事件
            if event.type == QUIT:          #退出事件发生
                pygame.quit()                   #退出程序
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN: #点击时间发生
                x, y = pygame.mouse.get_pos()   #得到鼠标点击位置
                if 25 <= x <= 725 and 25 <= y <= 725 and ((x - 25) % 50 <= level or (x - 25) % 50 >= 0) and (
                        (y - 25) % 50 <= level or (y - 25) % 50 >= 0):  #判断在棋盘范围内
                    color = -1 * color  #黑棋为1
                    m = int(round((x - 25) / 50))
                    n = int(round((y - 25) / 50))   #得到棋盘上的行值和列值
                    ch.fall(m, n, color)    #在二维数组下黑子
                    co.append(copy.deepcopy(ch.a))
                    if color == 1:
                        screen.blit(black, dot_list[level * m + n]) #在游戏界面下黑子
                    else:
                        screen.blit(white, dot_list[level * m + n]) #在游戏界面下黑子
                    if Judge(m, n, color, ch.a, 4): #判断黑子输赢
                        if color == 1:
                            screen.blit(font.render('The Winner is Black!!', True, (0,0,0)), (125, 625))    #在该位置写下黑棋胜利
                            pygame.display.update() #更新屏幕显示
                            speaker.Speak("黑棋胜利")
                            break
                        else:
                            screen.blit(font.render('The Winner is White!!', True, (255,255,255)), (125, 625))    #在该位置写下黑棋胜利
                            pygame.display.update() #更新屏幕显示
                            speaker.Speak("白棋胜利")
                            break
                elif x>730 and 190<=y<=265:#重新开始
                    wzq_pvp()
                elif x>730 and 490<=y<=565:#退出
                    pygame.quit()
                    sys.exit()
                elif x>730 and 340<=y<=415:#悔棋
                    screen.blit(background, (0, 0))
                    co.pop()
                    if len(co)!=0:
                        color = -1 * color
                        ch.a=copy.deepcopy(co[-1])
                        for i in range(15):
                            for j in range(15):
                                if ch.a[i][j]==1:
                                    screen.blit(black, dot_list[level * i + j])
                                    pygame.display.update() #更新屏幕显示
                                elif ch.a[i][j]==-1:
                                    screen.blit(white, dot_list[level * i + j])
                                    pygame.display.update() #更新屏幕显示
        pygame.display.update() #更新屏幕显示
        if flag:
            sleep(5)
def pve(ch):
    pygame.init()   #开始game界面
    bg = 'bg1.png'
    white_image = 'white.png'
    black_image = 'black.png'   #导入图片

    screen = pygame.display.set_mode((850, 750), 0, 32) #设置屏幕大小为750*750
    background = pygame.image.load(bg).convert()        #导入背景
    white = pygame.image.load(white_image).convert_alpha()  #导入白棋，保留背景
    black = pygame.image.load(black_image).convert_alpha()  #导入黑棋，保留背景
    white = pygame.transform.smoothscale(white, (int(white.get_width() * 1.5), int(white.get_height() * 1.5)))
    black = pygame.transform.smoothscale(black, (int(black.get_width() * 1.5), int(black.get_height() * 1.5)))  #重新定义棋子大小

    screen.blit(background, (0, 0)) #设置背景，及背景坐标
    font = pygame.font.SysFont("黑体", 40)    #设置字体及大小
    
    #pygame.event.set_blocked([1, 4, KEYUP, JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN, JOYBUTTONUP, JOYHATMOTION])    #不允许...
    pygame.event.set_allowed([MOUSEBUTTONDOWN, MOUSEBUTTONUP]) #允许鼠标点击

    dot_list = [(25 + i * 50 - white.get_width() / 2, 25 + j * 50 - white.get_height() / 2) for i in range(level) for
                j in range(level)]  #所有棋盘上可下的点的坐标列表
    color = -1  #颜色标志
    times = 0   #时间初始值
    flag = False    #游戏继续标志（目前未涉及，可以添加按钮后再做修改）
    while not flag: #五子棋主循环
        for event in pygame.event.get():    #遍历事件
            if event.type == QUIT:          #退出事件发生
                pygame.quit()                   #退出程序
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN: #点击时间发生
                x, y = pygame.mouse.get_pos()   #得到鼠标点击位置
                if 25 <= x <= 725 and 25 <= y <= 725 and ((x - 25) % 50 <= level or (x - 25) % 50 >= 0) and (
                        (y - 25) % 50 <= level or (y - 25) % 50 >= 0):  #判断在棋盘范围内
                    color = -1 * color  #黑棋为1
                    m = int(round((x - 25) / 50))
                    n = int(round((y - 25) / 50))   #得到棋盘上的行值和列值
                    ch.fall(m, n, color)    #在二维数组下黑子
                    #co.append(copy.deepcopy(ch.a))
                    screen.blit(black, dot_list[level * m + n]) #在游戏界面下黑子
                    if Judge(m, n, color, ch.a, 4): #判断黑子输赢
                        screen.blit(font.render('The Winner is Black!!', True, (0,0,0)), (125, 625))    #在该位置写下黑棋胜利
                        pygame.display.update() #更新屏幕显示
                        speaker.Speak("黑棋胜利")
                        break

                    color = -1 * color  #白棋为-1
                    sleep(0.1)  #延时0.1s
                    x, y = BetaGo(ch.a, m, n, color, times)
                    times += 1  #时间+1
                    #print("Predict:" + str(x) + " and " + str(y))
                    ch.fall(x, y, color)    #在二维数组下白子
                    co.append(copy.deepcopy(ch.a))
                    screen.blit(white, dot_list[level * x + y]) #在游戏界面下白子
                    if Judge(x, y, color, ch.a, 4): #判断白子输赢
                        screen.blit(font.render('The Winner is White!!', True, (255,255,255)), (125, 625))    ##在该位置写下白棋胜利
                        pygame.display.update() #更新屏幕显示
                        speaker.Speak("白棋胜利")
                        break
                elif x>730 and 190<=y<=265:#重新开始
                    wzq_pve()
                elif x>730 and 490<=y<=565:#退出
                    pygame.quit()
                    sys.exit()
                elif x>730 and 340<=y<=415:#悔棋
                    screen.blit(background, (0, 0))
                    co.pop()
                    if len(co)!=0:
                        ch.a=copy.deepcopy(co[-1])
                        for i in range(15):
                            for j in range(15):
                                if ch.a[i][j]==1:
                                    screen.blit(black, dot_list[level * i + j])
                                    pygame.display.update() #更新屏幕显示
                                elif ch.a[i][j]==-1:
                                    screen.blit(white, dot_list[level * i + j])
                                    pygame.display.update() #更新屏幕显示
        pygame.display.update() #更新屏幕显示
        if flag:
            sleep(5)

class chess(object):    #棋盘的类
    def __init__(self):
        self.a = [[0 for high in range(15)] for col in range(15)]   #全15*15棋盘初值0（二维数组）

    def fall(self, x, y, color):    #在二维数组中下子
        if (x < 0 or x > level - 1 or y < 0 or y > level - 1):  #如果在棋盘范围外返回为空
            return
        self.a[x][y] = color    #棋子颜色，黑子为1，白子为-1
        if Judge(x, y, color, self.a, 4):   #判断输赢
            if color < 0:
                print("白旗胜利！")
            else:
                print("黑棋胜利！")

    def isEmpty(self, m, n):    #棋盘是否为空
        if self.a[m][n] != 0:
            return False
        else:
            return True     #棋盘为空返回True，否则返回False

def Scan(chesspad, color):
    shape = [[[0 for high in range(5)] for col in range(15)] for row in range(15)]
    # 扫描每一个点，然后在空白的点每一个方向上做出价值评估！！
    for i in range(15):
        for j in range(15):
            # 如果此处为空 那么就可以开始扫描周边
            if chesspad[i][j] == 0:
                m = i
                n = j
                # 如果上方跟当前传入的颜色参数一致，那么加分到0位！
                while n - 1 >= 0 and chesspad[m][n - 1] == color:
                    n -= 1
                    shape[i][j][0] += grade
                if n-1>=0 and chesspad[m][n - 1] == 0:
                    shape[i][j][0] += 1
                if n-1 >= 0 and chesspad[m][n - 1] == -color:
                    shape[i][j][0] -= 2
                m = i
                n = j
                # 如果下方跟当前传入的颜色参数一致，那么加分到0位！
                while (n + 1 < level  and chesspad[m][n + 1] == color):
                    n += 1
                    shape[i][j][0] += grade
                if n + 1 < level  and chesspad[m][n + 1] == 0:
                    shape[i][j][0] += 1
                if n + 1 < level  and chesspad[m][n + 1] == -color:
                    shape[i][j][0] -= 2
                m = i
                n = j
                # 如果左边跟当前传入的颜色参数一致，那么加分到1位！
                while (m - 1 >= 0 and chesspad[m - 1][n] == color):
                    m -= 1
                    shape[i][j][1] += grade
                if m - 1 >= 0 and chesspad[m - 1][n] == 0:
                    shape[i][j][1] += 1
                if m - 1 >= 0 and chesspad[m - 1][n] == -color:
                    shape[i][j][1] -= 2
                m = i
                n = j
                # 如果右边跟当前传入的颜色参数一致，那么加分到1位！
                while (m + 1 < level  and chesspad[m + 1][n] == color):
                    m += 1
                    shape[i][j][1] += grade
                if m + 1 < level  and chesspad[m + 1][n] == 0:
                    shape[i][j][1] += 1
                if m + 1 < level  and chesspad[m + 1][n] == -color:
                    shape[i][j][1] -= 2
                m = i
                n = j
                # 如果左下方跟当前传入的颜色参数一致，那么加分到2位！
                while (m - 1 >= 0 and n + 1 < level  and chesspad[m - 1][n + 1] == color):
                    m -= 1
                    n += 1
                    shape[i][j][2] += grade
                if m - 1 >= 0 and n + 1 < level  and chesspad[m - 1][n + 1] == 0:
                    shape[i][j][2] += 1
                if m - 1 >= 0 and n + 1 < level  and chesspad[m - 1][n + 1] == -color:
                    shape[i][j][2] -= 2
                m = i
                n = j
                # 如果右上方跟当前传入的颜色参数一致，那么加分到2位！
                while (m + 1 < level  and n - 1 >= 0 and chesspad[m + 1][n - 1] == color):
                    m += 1
                    n -= 1
                    shape[i][j][2] += grade
                if m + 1 < level  and n - 1 >= 0 and chesspad[m + 1][n - 1] == 0:
                    shape[i][j][2] += 1
                if m + 1 < level  and n - 1 >= 0 and chesspad[m + 1][n - 1] == -color:
                    shape[i][j][2] -= 2
                m = i
                n = j
                # 如果左上方跟当前传入的颜色参数一致，那么加分到3位！
                while (m - 1 >= 0 and n - 1 >= 0 and chesspad[m - 1][n - 1] == color):
                    m -= 1
                    n -= 1 
                    shape[i][j][3] += grade
                if m - 1 >= 0 and n - 1 >= 0 and chesspad[m - 1][n - 1] == 0:
                    shape[i][j][3] += 1
                if m - 1 >= 0 and n - 1 >= 0 and chesspad[m - 1][n - 1] == -color:
                    shape[i][j][3] -= 2
                m = i
                n = j
                # 如果右下方跟当前传入的颜色参数一致，那么加分到3位！
                while m + 1 < level  and n + 1 < level  and chesspad[m + 1][n + 1] == color:
                    m += 1
                    n += 1
                    shape[i][j][3] += grade
                if m + 1 < level  and n + 1 < level  and chesspad[m + 1][n + 1] == 0:
                    shape[i][j][3] += 1
                if m + 1 < level  and n + 1 < level  and chesspad[m + 1][n + 1] == -color:
                    shape[i][j][3] -= 2
    return shape

def Judge(x, y, color, ch, length):
    count1, count2, count3, count4 = 0, 0, 0, 0
    # 横向判断
    i = x - 1
    while (i >= 0):
        if color == ch[i][y]:
            count1 += 1
            i -= 1
        else:
            break
    i = x + 1
    while i < level:
        if ch[i][y] == color:
            count1 += 1
            i += 1
        else:
            break

    # 纵向判断
    j = y - 1
    while (j >= 0):
        if ch[x][j] == color:
            count2 += 1
            j -= 1
        else:
            break
    j = y + 1
    while j < level:
        if ch[x][j] == color:
            count2 += 1
            j += 1
        else:
            break

    # 正对角线判断
    i, j = x - 1, y - 1
    while (i >= 0 and j >= 0):
        if ch[i][j] == color:
            count3 += 1
            i -= 1
            j -= 1
        else:
            break
    i, j = x + 1, y + 1
    while (i < level and j < level):
        if ch[i][j] == color:
            count3 += 1
            i += 1
            j += 1
        else:
            break
    # 反对角线判断
    i, j = x + 1, y - 1
    while (i < level and j >= 0):
        if ch[i][j] == color:
            count4 += 1
            i += 1
            j -= 1
        else:
            break
    i, j = x - 1, y + 1
    while (i >= 0 and j < level):
        if ch[i][j] == color:
            count4 += 1
            i -= 1
            j += 1
        else:
            break

    if count1 >= length or count2 >= length or count3 >= length or count4 >= length:
        return True
    else:
        return False

def Sort(shape):
    for i in shape:
        for j in i:
            for x in range(5):
                for w in range(3, x - 1, -1):
                    if j[w - 1] < j[w]:
                        temp = j[w]
                        j[w - 1] = j[w]
                        j[w] = temp
    #print("This Time Sort Done !")
    return shape

def Evaluate(shape):
    for i in range(level):
        for j in range(level):

            if shape[i][j][0] == 4:
                return i, j, MAX
            shape[i][j][4] = shape[i][j][0]*1000 + shape[i][j][1]*100 + shape[i][j][2]*10 + shape[i][j][3]
    max_x = 0
    max_y = 0
    max = 0
    for i in range(15):
        for j in range(15):
            if max < shape[i][j][4]:
                max = shape[i][j][4]
                max_x = i
                max_y = j
    #print("the max is "+ str(max) + " at ( "+ str(max_x)+" , "+str(max_y)+" )")
    return max_x, max_y, max

def Autoplay(ch, m, n):
    a1 = [1,-1,1,-1,1,-1,0,0]
    b1 = [1,-1,-1,1,0,0,1,-1]
    rand = randint(0,7)
    while m+a1[rand]>=0 and m+a1[rand]<level and n+b1[rand]>=0 and n+b1[rand]<level and ch[m+a1[rand]][n+b1[rand]]!=0 :
        rand = randint(0,7)
    return m + a1[rand], n+b1[rand]

def BetaGo(ch, m, n, color, times):
    if times < 2:
        return Autoplay(ch, m, n)
    else:
        shape_P = Scan(ch, -color)
        shape_C = Scan(ch,color)
        shape_P = Sort(shape_P)
        shape_C = Sort(shape_C)
        max_x_P, max_y_P, max_P = Evaluate(shape_P)
        max_x_C, max_y_C, max_C = Evaluate(shape_C)
        if max_P>max_C and max_C<MAX:
            return max_x_P,max_y_P
        else:
            return max_x_C,max_y_C

def wzq_pve():
    pve(chess())       #开始五子棋

def wzq_pvp():
    pvp(chess())       #开始五子棋

