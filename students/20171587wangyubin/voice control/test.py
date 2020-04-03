import weather as w
import wave2pinyin as w2p
import recordsound as rs
import mcmove as mc
move=["前进","后退","向左","向右"]
while True:
    rs.record()
    order=w2p.w2p()
    if order != "没有识别到语音":
        if order == "结束":
            print("感谢使用")
            break
        elif order in move:
            if order == move[0]:
                mc.go_forward()
            elif order == move[1]:
                mc.go_backward()
            elif order == move[2]:
                mc.go_left()
            elif order == move[3]:
                mc.go_right()                        
        elif w.getWeatherInfo(order) == -1:
            print("没有查到%s的天气"%order)
        else:
            tmp=int(w.getWeatherInfo(order))
            print("%s温度为%d度" %(order,tmp))
            mc.build(tmp)