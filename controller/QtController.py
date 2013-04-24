import sys
from view.QtMainView import QtMainView
from PyQt4 import QtGui

class QtMainController:
	def __init__(self, model):
		self.model = model
		self.view = QtMainView(self)
		
	def setFrom(self, value):
		print "atualizar busca para", value	

	def show(self):
		self.view.show()
	
def main(model):
	app = QtGui.QApplication(sys.argv)
	controller = QtMainController(model)
	controller.show()
	sys.exit(app.exec_())
