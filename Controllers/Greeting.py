import datetime
import random

class Greeting:

	def __init__(self):
		pass

	def greeting(self):
	    now = int(datetime.datetime.now().hour)

	    if now > 17:
	    	return self.night()
	    if now > 12:
	        return self.afternoon()
	    else:
	    	return self.morning()

	def morning(self):
		morning = [
		'Ótimo dia',
		'Que dia maravilhoso',
		'Que dia lindo'
		]
		return random.choice(morning)

	def afternoon(self):
		afternoon = [
		'Ótima tarde',
		'Que tarde maravilhosa',
		'Que tarde linda'
		]
		return random.choice(afternoon)

	def night(self):
		night = [
		'Ótima noite',
		'Que noite maravilhosa',
		'Que noite linda'
		]
		return random.choice(night)
