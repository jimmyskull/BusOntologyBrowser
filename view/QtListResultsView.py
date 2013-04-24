from PyQt4 import QtCore, QtGui
from design.Ui_ListResults import Ui_ListResults

class QtListResultsView(QtGui.QWidget, Ui_ListResults):
    def __init__(self, controller, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        #self.centerOnScreen()
        
    def setLabelText(self, text):
		self.label.setText(text)
        
    def centerOnScreen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                (resolution.height() / 2) - (self.frameSize().height() / 2))
