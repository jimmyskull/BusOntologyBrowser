# -*- encoding: utf-8 -*-
from Controller import Controller

class MenuController(Controller):
	def __init__(self, model, view):
		Controller.__init__(self, model, view)

	def main(self):
		self.view.show_menu()
		return self.view.read_input()

