import speech_recognition as sr

class Command:

	def __init__(self):
		pass

	def myCommand():
		r = sr.Recognizer()

		with sr.Microphone() as source:
			# r.pause_threshold = 2
			# r.adjust_for_ambient_noise(source, duration = 2)
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)

		try:
			command = r.recognize_google(audio, language = 'pt-br').lower()
			print('Você disse: ' + command + '\n')
		except sr.UnknownValueError:
			print('Seu últino comando não pode ser compreendido!')
			command = Command.myCommand()

		return command
