from gtts import gTTS
from pygame import mixer

class Talk:

	def __init__(self):
		pass

	def talk(audio):
		print(audio)
		for line in audio.splitlines():
			textSpeech = gTTS(text = audio, lang = 'pt-br')
			textSpeech.save('assets/audio/audio.mp3')
			mixer.init()
			mixer.music.load('assets/audio/audio.mp3')
			mixer.music.play()
			while mixer.music.get_busy():
				continue
