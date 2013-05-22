# -*- encoding: utf-8 -*-
from model.BusModel import BusModel

# ONTOLOGIA = "bus_ontology_browser.rdf"
ONTOLOGIA = "bus_ontology.rdf"

def text_version():
	from controller.MenuController import MenuController
	from view.TextView import TextView
	menu = MenuController(BusModel(ONTOLOGIA), TextView())
	menu.main()

def text_version_admin():
	from controller.MenuControllerAdmin import MenuControllerAdmin
	from view.TextViewAdmin import TextViewAdmin
	menu = MenuControllerAdmin(BusModel(ONTOLOGIA), TextViewAdmin())
	menu.main()

def gui_version():
	from controller import QtController
	QtController.main(BusModel(ONTOLOGIA))

if __name__ == '__main__':
	try:
		# gui_version()
		# text_version()
		text_version_admin()
	except KeyboardInterrupt:
		print '\b'
