#-*- coding:utf-8 -*-
from robot.sdk.AbstractPlugin import AbstractPlugin
import time
import locale
locale.setlocale(locale.LC_CTYPE, 'chinese')
class Plugin(AbstractPlugin):
	SLUG = "time"  

	def handle(self,query):
		if any(word in query for word in ["时间", "几点"]):

			self.say(time.strftime("现在时间是%p%H:%M:%S", time.localtime()).replace("AM","下午").replace("PM","下午"))
		elif any(word in query for word in ["日期","几号","日子"]):
			self.say(time.strftime("今天是%Y-%m-%d，星期%w", time.localtime()).replace("星期0","星期天"))
		elif "星期" in query:		
			self.say(time.strftime("今天是星期%w", time.localtime()).replace("星期0","星期天"))
		
		
	def isValid(self,query):
		return any(word in query for word in ["时间", "几点","日期","几号","日子","星期"])




