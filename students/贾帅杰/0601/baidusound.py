from aip import AipSpeech
import os
from mutagen.mp3 import MP3


def speak(yuyin):
    APP_ID='17980615'
    API_KEY='pIQlVZYLO4aPDLM55GGMGe5L'
    SECRET_KEY='0Pba78PqkEch32ozc4IbvMFmjN7kaejw'

    client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
    voice=client.synthesis(yuyin,'zh',6,{'vol':15,'per':3,'spd':5})
    with open("voicebaidu.mp3",'wb') as fp:
        fp.write(voice)

    audio=MP3('voicebaidu.mp3')
    time=int(audio.info.length)
    os.system("voicebaidu.mp3")
    return time

