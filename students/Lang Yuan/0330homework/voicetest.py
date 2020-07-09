import os
from os import system
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("我的第一个语音程序" )    
