# -*- encoding: utf-8 -*-
from controller.MenuController import MenuController
from view.TextView import TextView
from model.BusModel import BusModel

if __name__ == '__main__':
	menu = MenuController(BusModel("ontology.rdf"), TextView())
	menu.main()

