import sys
from view.QtMainWindowView import QtMainWindowView
from view.QtDestinationView import QtDestinationView
from view.QtListResultsView import QtListResultsView
from view.QtRouteView import QtRouteView
from PyQt4 import QtGui

class QtMainController(object):
    def __init__(self, model):
        self.model = model
        self.destination_view = QtDestinationView(self)
        self.mainwindow_view = QtMainWindowView(self)
        self.listresults_view = QtListResultsView(self)
        self.route_view = QtRouteView(self)
        
        self.listresults_view.setLabelText('Teste')
        
    def updateSpotList(self, view, value):
        self.spot_list = self.model.buscar_pontos_ou_locais(str(value))
        view.setContent(self.spot_list)
        
    def selectSpot(self, view, item):
		if view == self.mainwindow_view:
			self.updateSpotList(self.destination_view, '')
			self.destination_view.show()
			self.destination_view.activateWindow()
		else:
			print 'todo'
        
    def GoBack(self, view):
        view.close()

    def show(self):
        self.updateSpotList(self.mainwindow_view, '')
        self.mainwindow_view.show()
        #self.destination_view.show()
        #self.listresults_view.show()
        #self.route_view.show()
    
def main(model):
    app = QtGui.QApplication(sys.argv)
    controller = QtMainController(model)
    controller.show()
    sys.exit(app.exec_())
