import weather as w
import nature as n
import recordsound as rs
import wave2pinyin as w2p
import baidusound as bd
import time
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

f=True
print('若查询天气，请说天气')
str1='你好，欢迎使用语音控制系统'
times=bd.speak(str1)
time.sleep(times)
while f:
    pos = mc.player.getTilePos()
    rs.shibie()
    command=w2p.zhuanhua()
    if command == '天气' :
        str1='你好，请说出您要查询的城市'
        times=bd.speak(str1)
        time.sleep(times)
        while f:
            rs.shibie()
            command=w2p.zhuanhua()
            if command == '退出':
                print('感谢使用天气语音查询系统')
                break
            city=command
            str1=w.getWeatherInfo(city)
            tmp=int(w.gettmp(city))
            pos = mc.player.getTilePos()
            for i in range(1,tmp+1):
                mc.setBlock(pos.x,pos.y+i,pos.z,35.0)
            for i in range(1,tmp+1):
                if i%5 == 0 :
                    mc.setBlock(pos.x,pos.y+i,pos.z,35)
                else :
                    mc.setBlock(pos.x,pos.y+i,pos.z,41)
            print(str1)
            times=bd.speak(str1)
            time.sleep(times)
            print('不再使用此功能请说退出')
    if command =='前进' or command =='后退' or command =='左转' or command =='右转' or command =='上升' or command =='下降':
        if command =='前进' :
            mc.player.setTilePos([pos.x,pos.y,pos.z+3])
        if command =='后退' :
            mc.player.setTilePos([pos.x,pos.y,pos.z-3])
        if command =='左转' :
            mc.player.setTilePos([pos.x+3,pos.y,pos.z])
        if command =='右转' :
            mc.player.setTilePos([pos.x-3,pos.y,pos.z])
        if command =='上升' :
            mc.player.setTilePos([pos.x,pos.y+3,pos.z])
        if command =='下降' :
            if pos.y>-10 :
                mc.player.setTilePos([pos.x,pos.y-3,pos.z])
            else :
                print('已到最底层')
    else :
        city=command
        if city=='退出系统' :
            break
    print('不再使用此系统请说退出系统')
print('感谢使用我的世界语音控制系统')
