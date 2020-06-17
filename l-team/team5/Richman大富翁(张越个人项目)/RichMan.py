# coding: gbk
import cv2
import csv
import random
import numpy as np

from PIL import Image, ImageDraw, ImageFont

readers = csv.reader(open('map.csv', encoding='utf-8-sig'))
dataLab = []
for r in readers:
    dataLab.append(r)
img = 0
flag = 1
button = 0
player = 0
local = 0
dataLab[0][5] = '1'
dataLab[0][6] = '1'
dataLab[0][7] = '1'
dataLab[0][8] = '1'
money = [20000000, 20000000, 20000000, 20000000]
color = [(0, 255, 255), (255, 0, 255), (255, 255, 0), (0, 0, 0)]
print(dataLab)


# OpenCv使用中文
def cv2ImgAddText(img_in, text, left, top, textColor=(0, 255, 0), textSize=60):
    if isinstance(img_in, np.ndarray):  # 判断是否OpenCV图片类型
        img_in = Image.fromarray(cv2.cvtColor(img_in, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_in)
    fontText = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img_in), cv2.COLOR_RGB2BGR)


# 投骰子
def roll():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_all = roll1 + roll2
    return roll1, roll2, roll_all


# 清屏
def clear_all():
    global img
    for j in range(560):
        cv2.rectangle(img, (240 + j, 240 + j), (800 - j, 800 - j), (200, 5, 100), 3)
    img = cv2ImgAddText(img, "投骰子", 475, 600, (250, 230, 200), 30)
    img = cv2ImgAddText(img, "玩家1：" + str(money[0]), 375, 350, (250, 230, 200), 30)
    cv2.rectangle(img, (355, 350), (365, 360), color[0], 3)
    img = cv2ImgAddText(img, "玩家2：" + str(money[1]), 375, 400, (250, 230, 200), 30)
    cv2.rectangle(img, (355, 400), (365, 410), color[1], 3)
    img = cv2ImgAddText(img, "玩家3：" + str(money[2]), 375, 450, (250, 230, 200), 30)
    cv2.rectangle(img, (355, 450), (365, 460), color[2], 3)
    img = cv2ImgAddText(img, "玩家4：" + str(money[3]), 375, 500, (250, 230, 200), 30)
    cv2.rectangle(img, (355, 500), (365, 510), color[3], 3)
    cv2.imshow('RichMan', img)


# 画地图
def draw_map():
    global img
    img = np.zeros((1020, 1020, 3), np.uint8)
    img[:] = [200, 5, 100]
    for i in range(12):
        cv2.line(img, (80, 80 + i * 80), (960, 80 + i * 80), (250, 230, 200), 3)
        cv2.line(img, (80 + i * 80, 80), (80 + i * 80, 960), (250, 230, 200), 3)
    for i in range(8):
        cv2.line(img, (240 + i * 80, 160), (240 + i * 80, 880), (200, 5, 100), 3)
        cv2.line(img, (160, 240 + i * 80), (880, 240 + i * 80), (200, 5, 100), 3)
    for i in range(40):
        img = cv2ImgAddText(img, dataLab[i][1], int(dataLab[i][10]) + 5, int(dataLab[i][11]) + 5, (250, 230, 200), 14)

    img = cv2ImgAddText(img, "大富翁", 475, 30, (250, 230, 200), 30)
    img = cv2ImgAddText(img, "投骰子", 475, 600, (250, 230, 200), 30)


def click(event, x, y, flags, param):
    global flag, button, player, local, img
    if event == cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:', x, y)
        if 480 < x < 570 and 600 < y < 630 and button == 0:
            clear_all()
            num1, num2, num = roll()
            if flag % 4 == 1:
                img = cv2ImgAddText(img, "当前是玩家一的回合", 375, 250, (250, 230, 200), 30)
                cv2.imshow('RichMan', img)
                player_ball("player1", num)
            elif flag % 4 == 2:
                img = cv2ImgAddText(img, "当前是玩家二的回合", 375, 250, (250, 230, 200), 30)
                cv2.imshow('RichMan', img)
                player_ball("player2", num)
            elif flag % 4 == 3:
                img = cv2ImgAddText(img, "当前是玩家三的回合", 375, 250, (250, 230, 200), 30)
                cv2.imshow('RichMan', img)
                player_ball("player3", num)
            elif flag % 4 == 0:
                img = cv2ImgAddText(img, "当前是玩家四的回合", 375, 250, (250, 230, 200), 30)
                cv2.imshow('RichMan', img)
                player_ball("player4", num)
            flag = flag + 1
        if 280 < x < 370 and 600 < y < 630 and button == 1:
            print('yes')
            buy_and_pay(player, local, 1)

        elif 680 < x < 770 and 600 < y < 630 and button == 1:
            print('no')
            buy_and_pay(player, local, 2)


# 移动玩家标志物
def player_ball(which, rolls):
    k = 0
    global player, local, button
    print(which, rolls)
    global dataLab, img
    if which == "player1":
        # 检索玩家位置
        for j in range(40):
            if int(dataLab[j][5]) == 1:
                break
            else:
                k = k + 1
        cv2.rectangle(img, (int(dataLab[k][10]) + 5, int(dataLab[k][11]) + 35),
                      (int(dataLab[k][10]) + 15, int(dataLab[k][11]) + 45), (200, 5, 100), 3)  # 1
        # 更改原先的位置信息
        dataLab[k][5] = '0'
        # 判断是否路过起点
        if (k + rolls) >= 40:
            k = (k + rolls) - 40
            money[0] = money[0] + 200000
        else:
            k = k + rolls
        cv2.rectangle(img, (int(dataLab[k][10]) + 5, int(dataLab[k][11]) + 35),
                      (int(dataLab[k][10]) + 15, int(dataLab[k][11]) + 45), (0, 255, 255), 3)  # 1
        # 更新位置信息
        cv2.imshow('RichMan', img)
        dataLab[k][5] = '1'
        print(k, dataLab[k][1], dataLab[k][10], dataLab[k][11], dataLab[k][9])
        if dataLab[k][9] is not '':
            player = 1
            button = 1

    elif which == "player2":
        # 检索玩家位置
        for j in range(40):
            if int(dataLab[j][6]) == 1:
                break
            else:
                k = k + 1
        cv2.rectangle(img, (int(dataLab[k][10]) + 25, int(dataLab[k][11]) + 35),
                      (int(dataLab[k][10]) + 35, int(dataLab[k][11]) + 45), (200, 5, 100), 3)  # 2
        # 更改原先的位置信息
        dataLab[k][6] = '0'
        # 判断是否路过起点
        if (k + rolls) >= 40:
            k = (k + rolls) - 40
            money[1] = money[1] + 200000
        else:
            k = k + rolls
        cv2.rectangle(img, (int(dataLab[k][10]) + 25, int(dataLab[k][11]) + 35),
                      (int(dataLab[k][10]) + 35, int(dataLab[k][11]) + 45), (255, 0, 255), 3)  # 2
        # 更新位置信息
        cv2.imshow('RichMan', img)
        dataLab[k][6] = '1'
        print(k, dataLab[k][1], dataLab[k][10], dataLab[k][11])
        if dataLab[k][9] is not '':
            player = 2
            button = 1

    elif which == "player3":
        # 检索玩家位置
        for j in range(40):
            if int(dataLab[j][7]) == 1:
                break
            else:
                k = k + 1
        cv2.rectangle(img, (int(dataLab[k][10]) + 45, int(dataLab[k][11]) + 35),
                      (int(dataLab[k][10]) + 55, int(dataLab[k][11]) + 45), (200, 5, 100), 3)  # 2
        # 更改原先的位置信息
        dataLab[k][7] = '0'
        # 判断是否路过起点
        if (k + rolls) >= 40:
            k = (k + rolls) - 40
            money[2] = money[2] + 200000
        else:
            k = k + rolls
        cv2.rectangle(img, (int(dataLab[k][10]) + 45, int(dataLab[k][11]) + 35),
                      (int(dataLab[k][10]) + 55, int(dataLab[k][11]) + 45), (255, 255, 0), 3)  # 3
        # 更新位置信息
        cv2.imshow('RichMan', img)
        dataLab[k][7] = '1'
        print(k, dataLab[k][1], dataLab[k][10], dataLab[k][11])
        if dataLab[k][9] is not '':
            player = 3
            button = 1

    elif which == "player4":
        # 检索玩家位置
        for j in range(40):
            if int(dataLab[j][8]) == 1:
                break
            else:
                k = k + 1
        cv2.rectangle(img, (int(dataLab[k][10]) + 65, int(dataLab[k][11]) + 35),
                      (int(dataLab[k][10]) + 75, int(dataLab[k][11]) + 45), (200, 5, 100), 3)  # 2
        # 更改原先的位置信息
        dataLab[k][8] = '0'
        # 判断是否路过起点
        if (k + rolls) >= 40:
            k = (k + rolls) - 40
            money[3] = money[3] + 200000
        else:
            k = k + rolls
        cv2.rectangle(img, (int(dataLab[k][10]) + 65, int(dataLab[k][11]) + 35),
                      (int(dataLab[k][10]) + 75, int(dataLab[k][11]) + 45), (0, 0, 0), 3)  # 3
        # 更新位置信息
        cv2.imshow('RichMan', img)
        dataLab[k][8] = '1'
        print(k, dataLab[k][1], dataLab[k][10], dataLab[k][11])
        if dataLab[k][9] is not '':
            player = 4
            button = 1

    # 刷新更改
    img = cv2ImgAddText(img, dataLab[k][1], 475, 550, (250, 230, 200), 30)
    if dataLab[k][9] is not '':
        img = cv2ImgAddText(img, "是", 285, 600, (250, 230, 200), 30)
        img = cv2ImgAddText(img, "否", 685, 600, (250, 230, 200), 30)
        if int(dataLab[k][9]) == 0:
            img = cv2ImgAddText(img, "是否购买", 375, 300, (250, 230, 200), 30)
        elif player == int(dataLab[k][9]) and dataLab[k][12] != 3:
            img = cv2ImgAddText(img, "受否升级", 375, 300, (250, 230, 200), 30)
        else:
            img = cv2ImgAddText(img, "你需要交过路费", 375, 300, (250, 230, 200), 30)
    cv2.imshow('RichMan', img)
    local = k


# player 玩家 local 玩家现在的位置
def buy_and_pay(player, local, yes_no):
    global img, button
    multiple = 1
    clear_all()
    if int(dataLab[local][9]) == 0:
        img = cv2ImgAddText(img, "是", 285, 600, (250, 230, 200), 30)
        img = cv2ImgAddText(img, "否", 685, 600, (250, 230, 200), 30)
        cv2.imshow('RichMan', img)
        print(money)
        cv2.setMouseCallback('RichMan', click)
        if yes_no == 1:
            money[player - 1] = money[player - 1] - int(dataLab[local][3])
            print(money)
            dataLab[local][9] = str(player)
            img = cv2ImgAddText(img, "购买成功", 475, 300, (250, 230, 200), 30)
            cv2.rectangle(img, (int(dataLab[local][10]) + 5, int(dataLab[local][11]) + 65),
                          (int(dataLab[local][10]) + 15, int(dataLab[local][11]) + 75), color[player - 1], 3)
            cv2.imshow('RichMan', img)
            button = 0
            return
        elif yes_no == 2:
            img = cv2ImgAddText(img, "没有购买", 475, 300, (250, 230, 200), 30)
            button = 0
            return
    elif int(dataLab[local][9]) != 0:
        if player == int(dataLab[local][9]) and dataLab[local][12] != 3:
            cv2.imshow('RichMan', img)
            if yes_no == 1:
                if dataLab[local][12] == 0:
                    multiple = 1
                    cv2.rectangle(img, (int(dataLab[local][10]) + 15, int(dataLab[local][11]) + 55),
                                  (int(dataLab[local][10]) + 25, int(dataLab[local][11]) + 65), color[player - 1], 3)
                    cv2.imshow('RichMan', img)
                elif dataLab[local][12] == 1:
                    multiple = 2
                    cv2.rectangle(img, (int(dataLab[local][10]) + 25, int(dataLab[local][11]) + 55),
                                  (int(dataLab[local][10]) + 35, int(dataLab[local][11]) + 65), color[player - 1], 3)
                    cv2.imshow('RichMan', img)
                elif dataLab[local][12] == 2:
                    multiple = 3
                    cv2.rectangle(img, (int(dataLab[local][10]) + 35, int(dataLab[local][11]) + 55),
                                  (int(dataLab[local][10]) + 45, int(dataLab[local][11]) + 65), color[player - 1], 3)
                    cv2.imshow('RichMan', img)
                money[player - 1] = money[player - 1] - int(dataLab[local][3]) * multiple
                dataLab[local][12] = str(int(dataLab[local][12]) + 1)
                img = cv2ImgAddText(img, "升级成功", 475, 300, (250, 230, 200), 30)
                cv2.imshow('RichMan', img)
                button = 0
                print(multiple)
                return
            elif yes_no == 2:
                img = cv2ImgAddText(img, "没有升级", 475, 300, (250, 230, 200), 30)
                cv2.imshow('RichMan', img)
                button = 0
                return
        else:
            print(money)
            if dataLab[local][12] == 0:
                multiple = 1
            elif dataLab[local][12] == 1:
                multiple = 2
            elif dataLab[local][12] == 2:
                multiple = 4
            elif dataLab[local][12] == 3:
                multiple = 8
            money[player - 1] = money[player - 1] - int(dataLab[local][4]) * multiple
            money[int(dataLab[local][9]) - 1] = money[int(dataLab[local][9]) - 1] + int(dataLab[local][4]) * multiple
            img = cv2ImgAddText(img, "你交了路费" + str(int(dataLab[local][4]) * multiple), 475, 300, (250, 230, 200), 30)
            cv2.imshow('RichMan', img)
            print(money)
            button = 0
            return
    else:
        return


def win_lost():
    global money
    if money[0] <= 0 or money[1] <= 0 or money[2] <= 0 or money[3] <= 0:
        if money[0] <= 0:
            print("游戏结束，玩家1失败")
        elif money[1] <= 0:
            print("游戏结束，玩家2失败")
        elif money[2] <= 0:
            print("游戏结束，玩家3失败")
        elif money[3] <= 0:
            print("游戏结束，玩家4失败")
    return 0


draw_map()
cv2.rectangle(img, (int(dataLab[0][10]) + 5, int(dataLab[0][11]) + 35),
              (int(dataLab[0][10]) + 15, int(dataLab[0][11]) + 45), (0, 255, 255), 3)  # 1
cv2.rectangle(img, (int(dataLab[0][10]) + 25, int(dataLab[0][11]) + 35),
              (int(dataLab[0][10]) + 35, int(dataLab[0][11]) + 45), (255, 0, 255), 3)  # 2
cv2.rectangle(img, (int(dataLab[0][10]) + 45, int(dataLab[0][11]) + 35),
              (int(dataLab[0][10]) + 55, int(dataLab[0][11]) + 45), (255, 255, 0), 3)  # 3
cv2.rectangle(img, (int(dataLab[0][10]) + 65, int(dataLab[0][11]) + 35),
              (int(dataLab[0][10]) + 75, int(dataLab[0][11]) + 45), (0, 0, 0), 3)  # 4
clear_all()
cv2.imshow('RichMan', img)
cv2.namedWindow('RichMan')
cv2.setMouseCallback('RichMan', click)

while True:
    if cv2.waitKey(10) & 0xFF == 27:
        break
    elif win_lost() != 0:
        break
cv2.destroyAllWindows()
