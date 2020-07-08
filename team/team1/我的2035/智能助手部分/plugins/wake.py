from robot.sdk.AbstractPlugin import AbstractPlugin
import time

class Plugin(AbstractPlugin):
	SLUG = "wake"

	def handle(self,query):
		self.say("好的")
		return "好的"

	def isValid(self,query):
		return any(word in query for word in ["斯巴达"])