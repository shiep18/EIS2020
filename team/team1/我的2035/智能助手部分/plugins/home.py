from robot.sdk.AbstractPlugin import AbstractPlugin

class Plugin(AbstractPlugin):
	SLUG = "home"

	def handle(self,query):
		self.say("欢迎回家")
		return "欢迎回家"

	def isValid(self,query):
		return query == 1






