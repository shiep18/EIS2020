from aip import AipSpeech
import os

def w2p():
    APP_ID='19165156'
    API_KEY='WtdBurU6FFaQ1ZDfIqoxwm5l'
    SECRET_KEY='13k6LOB86dLS7QWsIIkSsYLYoIr3EhT9'

    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)


    with open('audio.wav', 'rb') as fp:
            wave=fp.read()

    print("* 正在识别......",len(wave))
    result = client.asr(wave, 'wav', 16000, {'dev_pid':1537})
    #print(result)
    if result["err_no"] == 0:
        city=str(result["result"])
        city=city[2:-3]

    else:
        #print("没有识别到语音\n",result["err_no"])
        city="没有识别到语音"
    print(city)
    return city
