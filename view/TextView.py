# -*- encoding: utf-8 -*-
from View import View

class TextView(View):
	def __init__(self):
		View.__init__(self)
	
	def show_menu(self):
		print "1. Listar os horários em que há ônibus para um local."
		print "2. Listar linhas que passam por um ponto."
		print "3. Listar os horários de uma linha."
		print "4. Mostrar um itinerário para um local."
		print "5. Listar os pontos próximos de um local."
		print "6. Listar os horários em que há um itinerário de um local inicial para outro local."
		
	def read_input(self):
		MIN = 1
		MAX = 6
		try:
			question = raw_input('Entre um valor ({} - {}) >. '.format(MIN, MAX))	
			answer = int(question) 
			if not answer in range(MIN, MAX + 1):
				raise ValueError
			return answer
		except ValueError:
			print 'Entada inválida.  Valor deve estar entre {} - {}.'.format(MIN, MAX)
			self.read_input()
