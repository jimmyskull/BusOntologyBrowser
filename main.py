# -*- encoding: utf-8 -*-
from model.BusModel import BusModel

ONTOLOGIA = "bus_ontology_browser.rdf"

def text_version():
	from controller.MenuController import MenuController
	from view.TextView import TextView
	menu = MenuController(BusModel("bus_ontology_browser.rdf"), TextView())
	menu.main()

def gui_version():
	from controller import QtController
	QtController.main(BusModel(ONTOLOGIA))

if __name__ == '__main__':
	try:
		gui_version()
		# text_version()
	except KeyboardInterrupt:
		print '\b'
