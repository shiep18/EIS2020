from aip import AipSpeech
import os

def zhuanhua():
    APP_ID='17980615'
    API_KEY='pIQlVZYLO4aPDLM55GGMGe5L'
    SECRET_KEY='0Pba78PqkEch32ozc4IbvMFmjN7kaejw'

    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)


    with open('audio.wav', 'rb') as fp:
            wave=fp.read()

    print("* 正在识别......",len(wave))
    result = client.asr(wave, 'wav', 16000, {'dev_pid':1537})
    print(result)
    key1=result['result']
    s=str(key1[0])
    s1=s[0:-1]
    if result["err_no"] == 0:
        for t in result["result"]:
            print(t)
    else:
        print("没有识别到语音\n",result["err_no"])
    return s1
