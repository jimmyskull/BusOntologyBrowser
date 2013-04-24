# -*- encoding: utf-8 -*-
from controller.MenuController import MenuController
from view.TextView import TextView
from model.BusModel import BusModel

if __name__ == '__main__':
	try:
		menu = MenuController(BusModel("bus_ontology_browser.rdf"), TextView())
		menu.main()
	except KeyboardInterrupt:
		print '\b'

