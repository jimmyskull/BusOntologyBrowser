# -*- encoding: utf-8 -*-
from View import View

class TextView(View):
	def __init__(self):
		View.__init__(self)
	
	def show_menu(self):
		print "1. Listar linhas de um ponto"
		
	def read_input(self):
		MIN = 1
		MAX = 1
		try:
			question = raw_input('Entre um valor ({} - {}) >. '.format(MIN, MAX))	
			answer = int(question) 
			if not answer in range(MIN, MAX + 1):
				raise ValueError
			return answer
		except ValueError:
			print 'Entada inválida.  Valor deve estar entre {} - {}.'.format(MIN, MAX)
			self.read_input()
