from Controllers.Talk import Talk
from Controllers.Greeting import Greeting
from Controllers.Command import Command
import random

def tars(command):
	errors = [
	'Não compreendi seu último comando!',
	'Não compreendi o que você disse!',
	'Você disse cachorro passeando com o dono?',
	'Pode repetir por favor?',
	]

	if 'quem é você' in command:
		Talk.talk('Não há dados o suficiente para uma resposta significativa!')
	else:
		error = random.choice(errors)
		Talk.talk(error)
		#Talk.talk('Você disse: ' + command)

greeting = Greeting()
Talk.talk(greeting.greeting())
Talk.talk('Sou tars, Como posso ajudar?')

while True:
	tars(Command.myCommand())
