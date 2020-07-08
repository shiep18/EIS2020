import os
from aip.speech import AipSpeech
print("MXSpeech")


class MXSpeech():
    def __init__(self, APP_ID, API_KEY, SECRET_KEY):
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def TTS(self, text):
        """文本转语音"""
        result = self.client.synthesis(text, 'zh', 4, {
            'vol': 5, 'per': 4,
        })

        if not isinstance(result, dict):
            with open('back.mp3', 'wb') as f:
                f.write(result)

        os.system("ffmpeg -i back.mp3 -y back.wav")


    def STT(self, fname="back.wav"):
        """语音转文本"""
        with open(fname, 'rb') as fp:
            data = fp.read()

        result = self.client.asr(data, 'pcm', 16000, {
            'dev_pid': 1537,
        })
        if result['err_no'] == 0:
            return str(result['result'][0])
        else:
            return ""


