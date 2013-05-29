# -*- encoding: utf-8 -*-
from Controller import Controller

class MenuControllerAdmin(Controller):
	def __init__(self, model, view):
		Controller.__init__(self, model, view)
		self.choices = {
			1: self._choice_insert_stop,
			2: self._choice_insert_time,
			3: self._choice_insert_local,
			"sair": self.finish}

	def _choice_insert_stop(self):
		stop = self.view.read_stop_id()
		name = self.view.read_stop_name()
		times = self.view.read_stop_times()
		self.model.inserir_ponto(stop, name, times)

	def _choice_insert_time(self):
		time = self.view.read_time_id()
		name = self.view.read_time_name()
		self.model.inserir_horario(time, name)

	def _choice_insert_local(self):
		local = self.view.read_local_id() 
		name = self.view.read_local_name()
		stop = self.view.read_stop_id()
		if not self.model.ponto_existe(stop):
			self.view.not_in_base(stop)
			name = self.view.read_stop_name()
			times = self.view.read_stop_times()
			self.model.inserir_ponto(stop, name, times)
		self.model.inserir_local(local, name, stop)

	def main(self):
		i = ""
		while i != "sair":
			self.view.show_menu()
			i = self.view.read_input()
			self.choices[i]()

