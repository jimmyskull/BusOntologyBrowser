# -*- encoding: utf-8 -*-
import sys
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
		if '--help' in sys.argv:
			print 'BusOntologyBrowser help'
			print '{} [OPTION]'.format(sys.argv[0])
			print '\t--admin\tStart admin menu'
			print '\t--gui\tStart version with graphical interface'
			print '\t--text\tStart interactive text mode version'
			exit(0)
		if '--gui' in sys.argv:
			gui_version()
		elif '--admin' in sys.argv:
			text_version_admin()
		else:
			text_version()
	except KeyboardInterrupt:
		print '\b'
