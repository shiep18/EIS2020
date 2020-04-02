import pyaudio
from aip import AipSpeech
from xpinyin import Pinyin

def RecodeSound():
    import wave
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 8000
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "audio.wav"

    APP_ID='19165306'
    API_KEY='F0NWZzLVAnModNc6OG820Gu7'
    SECRET_KEY='	M8enxlGmxLqSeFxpV9XHgwI50sHk6486'
    client =AipSpeech(APP_ID,API_KEY,SECRET_KEY)

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    stream.start_stream()
    print("* 开始录音......")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    #录音结束

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    with open('audio.wav','rb') as fp:
        wave=fp.read()

    print("*正在识别......",len(wave))
    result=client.asr(wave,'wav',16000,{'dev_pid':1537})
    #print(result)
    if '。' in result['result'][0]:
        result['result'][0]=result['result'][0].replace('。','')
    if result["err_no"]==0:
        k=''
        for t in result['result']:
            k+=t
        command=MinecraftCommand(k)
    else:
        print("没有识别到语音\n",result["err_no"])
        return 'Error'
    if command[0]=='w' or command[0]=='a' or command[0]=='s' or command[0]=='d':
        if command[1]>9:
            print('距离较远,开始传送')
        else:
            pass
        return command
    else:
        print('指令有误，请重新读入')
        return RecodeSound()

def NumSel(text):
    num=''
    for i in text:
        if i>='0' and i<='9':
            num=num+i
        else:
            pass
    print(num)
    return int(num)

def MinecraftCommand(text):
    cmd=[]
    p = Pinyin()
    ptxt = p.get_pinyin(text)
    print(ptxt)
    if p.get_pinyin('前进') in ptxt:
        cmd.append('w')
    elif p.get_pinyin('后退') in ptxt:
        cmd.append('s')
    elif p.get_pinyin('左转') in ptxt or p.get_pinyin('向左') in ptxt:
        cmd.append('a')
    elif p.get_pinyin('右转') in ptxt or p.get_pinyin('向右') in ptxt:
        cmd.append('d')
    else:
        pass
    if '一' in text:
        cmd.append(1)
    elif '二' in text:
        cmd.append(2)
    elif '三' in text:
        cmd.append(3)
    elif '四' in text:
        cmd.append(4)
    elif '五' in text:
        cmd.append(5)
    elif '六' in text:
        cmd.append(6)
    elif '七' in text:
        cmd.append(7)
    elif '八' in text:
        cmd.append(8)
    elif '九' in text:
        cmd.append(9)
    else:
        cmd.append(NumSel(text))
    return cmd

if __name__=='__main__':
    CMD=RecodeSound()
    print(CMD)










