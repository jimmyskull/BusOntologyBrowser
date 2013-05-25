# -*- encoding: utf-8 -*-
from View import View

class TextViewAdmin(View):
	def __init__(self):
		View.__init__(self)

	def show_menu(self):
		print "========================================================================="
		print "                          Menu Administrador"
		print "========================================================================="
		print "1. Inserir uma nova linha."
		print "2. Remover uma linha."
		
	def read_input(self):
		MIN = 1
		MAX = 2
		try:
			question = raw_input('Entre um valor ({} - {}) >. '.format(MIN, MAX))	
			if question == "sair":
				return question 
			answer = int(question) 
			print answer
			if not answer in range(MIN, MAX + 1):
				raise ValueError
			return answer
		except ValueError:
			print 'Entada inválida.  Valor deve estar entre {} - {}.'.format(MIN, MAX)
			self.read_input()
	
	def read_line_id(self):
		answer = raw_input('Entre identificador da linha >. ')	
		return answer
	
	def read_line_name(self):
		answer = raw_input('Entre o nome da linha >. ')	
		return answer