import wave
import pyaudio
print("MXMedia")


class MXMedia():
    def __init__(self):
        self.isPlay = False
        self.isPause = False

    def record(self, rs=4, fname="back.wav"):
        """录音"""
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        RECORD_SECONDS = rs
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        stream.start_stream()
        print("* 开始录音<<<<<<")

        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(fname, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        print("* 结束录音<<<<<<")

    def play(self, fname="back.wav"):
        """播放"""
        print("* 开始播放>>>>>>")
        wf = wave.open(fname, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            input=False,
            output=True)

        stream.start_stream()
        data = wf.readframes(1024)
        self.isPlay = True
        while data != b'' and self.isPlay:
            if not self.isPause:
                stream.write(data)
                data = wf.readframes(1024)

        stream.stop_stream()
        stream.close()
        p.terminate()
        print("* 结束播放>>>>>>")
