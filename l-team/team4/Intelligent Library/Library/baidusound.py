from aip import AipSpeech
import os
from mutagen.mp3 import MP3
from playsound import playsound
import pyaudio
import wave
def speak(yuyin):
    APP_ID='17980615'
    API_KEY='pIQlVZYLO4aPDLM55GGMGe5L'
    SECRET_KEY='0Pba78PqkEch32ozc4IbvMFmjN7kaejw'

    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
    result = client.synthesis(yuyin, 'zh', 1, {'vol': 5,})

    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
        
    playsound("auido.mp3")

def record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 8000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "audio.wav"

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
    wf.close()

def w2p():
    APP_ID='19165156'
    API_KEY='WtdBurU6FFaQ1ZDfIqoxwm5l'
    SECRET_KEY='13k6LOB86dLS7QWsIIkSsYLYoIr3EhT9'
    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

    with open('audio.wav', 'rb') as fp:
            wave=fp.read()

    print("* 正在识别......",len(wave))
    result = client.asr(wave, 'wav', 16000, {'dev_pid':1537})
    if result["err_no"] == 0:
        order=str(result["result"])
        order=order[2:-3]
    else:
        order="没有识别到语音"
    print(order)
    return order
