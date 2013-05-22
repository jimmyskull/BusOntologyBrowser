# -*- encoding: utf-8 -*-
from Controller import Controller

class MenuControllerAdmin(Controller):
	def __init__(self, model, view):
		Controller.__init__(self, model, view)
		self.choices = {
			1: self._choice_insert_line,
			"sair": self.finish}
			# 2: self._choice_lines_having_a_spot,
			# 3: self._choice_list_line_schedule}

	def _choice_insert_line(self):
		line = self.view.read_line_id()
		name = self.view.read_line_name()
		self.model.inserir_linha(line, name)

	def main(self):
		i = ""
		while i != "sair":
			self.view.show_menu()
			i = self.view.read_input()
			self.choices[i]()

