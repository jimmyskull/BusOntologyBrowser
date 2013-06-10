# -*- encoding: utf-8 -*-
from Controller import Controller

class MenuController(Controller):
	def __init__(self, model, view):
		Controller.__init__(self, model, view)
		self.choices = {
			1: self._choice_list_location_schedule,
			2: self._choice_lines_having_a_spot,
			3: self._choice_list_line_schedule,
			4: self._choice_list_itinerary_lines,
			5: self._choice_list_bus_spot_near_location,
			6: self._choice_list_available_schedules_of_initial_itinerary_bus_stop,
			"sair": self.finish}

	# Questão 1
	def _choice_lines_having_a_spot(self):
		spot = self.view.read_bus_spot_name()
		result = self.model.buscar_linhas_em_um_ponto(spot)
		self.view.show_lines_having_a_spot(spot, result)
		
	# Questão 2
	def _choice_list_location_schedule(self):
		local = self.view.read_location_name()
		result = self.model.buscar_horarios_para_local(local)
		self.view.show_location_schedule(local, result)
	
	# Questão 3
	def _choice_list_line_schedule(self):
		linha = self.view.read_line_name()
		result = self.model.buscar_horarios_linha(linha)
		self.view.show_line_schedule(linha, result)
		
	# Questão 4
	def _choice_list_itinerary_lines(self):
		local = self.view.read_location_name()
		result = self.model.buscar_itinerario_para_local(local)
		self.view.show_itinerary_lines(local, result)

	# Questão 5
	def _choice_list_bus_spot_near_location(self):
		local = self.view.read_location_name()
		result = self.model.buscar_ponto_proximo_local(local)
		self.view.show_bus_spot_near_location(local, result)
	
	# Questão 5
	def _choice_list_available_schedules_of_initial_itinerary_bus_stop(self):
		local1 = self.view.read_location_name()
		local2 = self.view.read_location_name()
		result = self.model.buscar_horarios_ponto_proximo_para_outro_local(local1, local2)
		self.view.show_available_schedules_of_initial_itinerary_bus_stop(local1, local2, result)
	
	def _register_choice(self, ch, callback):
		self.choices[ch] = callback

	def main(self):
		i = ""
		while i != "sair":
			self.view.show_menu()
			i = self.view.read_input()
			self.choices[i]()
