import numpy as np
import cv2

colors = [
0xE9ECEC,		#白色羊毛
0xF07613,		#橙色羊毛
0xBD44B3,		#品红色羊毛
0x3AAFD9,		#淡蓝色羊毛
0xF8C627,		#黄色羊毛
0x70B919,		#黄绿色羊毛
0xED8DAC,		#粉红色羊毛
0x3E4447,		#灰色羊毛
0x8E8E86,		#淡灰色羊毛
0x158991,		#青色羊毛
0x792AAC,		#紫色羊毛
0x35399D,		#蓝色羊毛
0x724728,		#棕色羊毛
0x546D1B,		#绿色羊毛
0xA12722,		#红色羊毛
0x141519,		#黑色羊毛
]
dict1 = []
# 16进制颜色格式颜色转换为RGB格式,并转化为灰度
def Hex_to_Gray(hex):
    r = int(hex[2:4],16)
    g = int(hex[4:6],16)
    b = int(hex[6:8],16)
    gray = int((r + g + b)/3)
    print(str(int(gray)))
    return gray

for i in range(0,16):
    co = hex(colors[i])
    graynew = Hex_to_Gray(co)
    dict1.append([graynew,i])
    print(dict1)
   # RGB_to_GRAY(Colornew)
