# -*- encoding: utf-8 -*-
from View import View

class TextView(View):
	def __init__(self):
		View.__init__(self)
	
	def show_menu(self):
		print ""
		print "Menu"
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
		
	def read_bus_spot_name(self):
		return 'terminal_Fonte'
		answer = raw_input('Entre o nome do ponto >. ')	
		return answer
		
	def read_location_name(self):
		#return 'local_CEDETEG'
		answer = raw_input('Entre o nome do local >. ')	
		return answer
		
	def read_line_name(self):
		return 'linha_Karpinsky'
		answer = raw_input('Entre o nome da linha >. ')	
		return answer
		
	def _print_first_columns(self, results):
		for r in results:
			print '\t', r[0]
		
	def show_lines_having_a_spot(self, ponto, linhas):
		print('Linhas que passam pelo ponto {}:'.format(ponto))
		self._print_first_columns(linhas)
		
	def show_location_schedule(self, local, horarios):
		print('Horários em que há ônibus para o local {}:'.format(local))
		self._print_first_columns(horarios)
			
	def show_line_schedule(self, linha, horarios):
		print('Horários da linha {}:'.format(linha))
		self._print_first_columns(horarios)

	def show_itinerary_lines(self, itinerario, linhas):
		print('Linhas do itinerário {}:'.format(itinerario))
		self._print_first_columns(linhas)

	def show_bus_spot_near_location(self, local, pontos):
		print('Pontos próximos do local {}:'.format(local))
		self._print_first_columns(pontos)
			
	def show_available_schedules_of_initial_itinerary_bus_stop(self, local1, local2, horarios):
		print('Horários do ponto {} para chegar ao ponto {}:'.format(local1, local2))
		self._print_first_columns(horarios)
