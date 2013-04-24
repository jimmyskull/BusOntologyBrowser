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
        
    def setFrom(self, value):
        print "atualizar busca para", value 

    def show(self):
        self.mainwindow_view.show()
        self.destination_view.show()
        self.listresults_view.show()
        self.route_view.show()
    
def main(model):
    app = QtGui.QApplication(sys.argv)
    controller = QtMainController(model)
    controller.show()
    sys.exit(app.exec_())
