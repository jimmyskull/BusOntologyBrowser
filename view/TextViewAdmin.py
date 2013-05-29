# -*- encoding: utf-8 -*-
from View import View

class TextViewAdmin(View):
	def __init__(self):
		View.__init__(self)

	def show_menu(self):
		print "========================================================================="
		print "                          Menu Administrador"
		print "========================================================================="
		print "1. Inserir um novo ponto."
		print "2. Inserir um novo horario."
		print "3. Inserir um novo local próximo de um ponto já existente."
		
	def read_input(self):
		MIN = 1
		MAX = 3
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

	def read_stop_id(self):
		answer = raw_input('Entre com o identificador do ponto >. ')	
		return answer
	
	def read_stop_name(self):
		answer = raw_input('Entre com o nome do ponto >. ')	
		return answer
	
	def read_stop_times(self):
		ids, names = [], []
		s = "y"
		while s == "y":
			ids.append(self.read_time_id())
			names.append(self.read_time_name())
			s = raw_input("Deseja inserir mais algum? (y - n) >. ")
		return [ids, names]
	
	def read_time_id(self):
		answer = raw_input('Entre com o identificador do horário >. ')	
		return answer
	
	def read_time_name(self):
		answer = raw_input('Entre com um horário >. ')	
		return answer
	
	def read_local_id(self):
		answer = raw_input('Entre com o identificador do local >. ')	
		return answer
	
	def read_local_name(self):
		answer = raw_input('Entre com o nome do local >. ')	
		return answer

	def read_wish_add(self, item):
		answer = raw_input("O recurso {} não está na base de dados. \nDeseja adicioná-lo? (y - n) >.".format(item))
		return answer

	def not_in_base(self, item):
		print "O recurso {} não está na base de dados. Você terá que adicioná-lo.".format(item)

if __name__ == '__main__':
	tva = TextViewAdmin()
	print tva.read_stop_times()