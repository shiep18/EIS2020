import wave
from aip import AipSpeech
from xpinyin import Pinyin
from baiduvoice.weather import *
from baiduvoice.nature import *
from baiduvoice.music import *
from baiduvoice.mcmove import *

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

STATE = 0
TIME_START = 0
TIME_END = 0

num = 0


def readFile(fileName):
    with open(fileName, 'rb') as fp:
        return fp.read()


def writeFile(fileName, result):
    with open(fileName, 'wb') as fp:
        fp.write(result)


def getBaiduText():
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

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

    print("* 正在识别......")
    result = client.asr(readFile('audio.wav'), 'wav', 16000, {
        'dev_pid': 1537,
    })
    if result["err_no"] == 0:
        for t in result["result"]:
            return t
    else:
        print("没有识别到语音\n")
        return ""


def getBaiduVoice(text):
    result = client.synthesis(text, 'zh', 6, {'vol': 5, 'per': 4, 'spd': 5})
    if not isinstance(result, dict):
        writeFile("back.mp3", result)
    playVoice("back.mp3")


def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)


def wakeUp(result, pinyin):
    if getPinYin("小爱同学") in pinyin:
        if getPinYin("你好") in pinyin:
            print("你好")
            getBaiduVoice("你好")
        elif getPinYin("开灯") in pinyin:
            print("灯已打开")
            getBaiduVoice("灯已打开")
        elif getPinYin("关灯") in pinyin:
            print("灯已关闭")
            getBaiduVoice("灯已关闭")
        elif getPinYin("天气") in pinyin:
            weatherWeGet = getWeatherInfo(get_address(get_url(), result))
            print(weatherWeGet[0])
            getBaiduVoice(weatherWeGet[0])
            temStone(weatherWeGet[1])
        elif getPinYin("听") in pinyin:
            downMusic(getMusicName(result))
        elif getPinYin("首") in pinyin:
            downMusic(getMusicName(result))
        elif getPinYin("我的世界") in pinyin:
            if getPinYin("左") in pinyin:
                mcgo("left")
            elif getPinYin("右") in pinyin:
                mcgo("right")
            elif getPinYin("后") in pinyin:
                mcgo("back")
            elif getPinYin("前") in pinyin:
                mcgo("strange")
        else:
            print("我在")
            playVoice("im.mp3")


def main():
    while True:
        result = getBaiduText()
        pinyin = getPinYin(result)
        print("等待唤醒")
        print(result)
        wakeUp(result, pinyin)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system("back.mp3")
        os.system("audio.wav")
        os.system("rmdir /s/q __pycache__")
