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
		
		self.selected_origin = None
		self.selected_destination = None
		
	def updateSpotList(self, view, value):
		list_ = self.model.buscar_pontos_ou_locais(str(value))
		if view == self.mainwindow_view:
			self.origin_list = list_
		else:
			self.dest_list = list_
		view.setContent(list_[0])
		
	def selectSpot(self, view, item):
		if view == self.mainwindow_view:
			self.selected_origin = item
			self.updateSpotList(self.destination_view, '')
			self.destination_view.show()
			self.destination_view.activateWindow()
		else:
			self.selected_destination = item
			origin = self.origin_list[0][self.selected_origin]
			dest = self.dest_list[0][self.selected_destination]
			sorigin = origin[0].encode('iso-8859-1').decode('utf8')
			sdest = dest[0].encode('iso-8859-1').decode('utf8')
			self.route_view.setArrows(sorigin, sdest)
			route = self.model.buscar_ponto_origem_itinerario(origin[1][37:], dest[1][37:])
			
			print '*** ROTA', route
			print '**** ROTA1', route[1]
			textoOrigem = route[0][0].encode('iso-8859-1').decode('utf8') + '\n' +\
				 route[1][0][0].encode('iso-8859-1').decode('utf8')
				
			textoDestino = route[2][0].encode('iso-8859-1').decode('utf8') + '\n'+\
				route[3][0][0].encode('iso-8859-1').decode('utf8')
			
			self.route_view.lblPontoInicio.setText(textoOrigem)
			self.route_view.lblPontoChegada.setText(textoDestino)
			print '&&&&&&&& ROTA &&&&&&&&'
			print 'Origem: ',textoOrigem
			print 'Destino: ', textoDestino
			print '&&&&&&&& ---- &&&&&&&&'
			self.route_view.show()
			self.route_view.activateWindow()			
		
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
