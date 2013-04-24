from PyQt4 import QtCore, QtGui
from design.Ui_MainWindow import Ui_MainWindow

class QtMainWindowView(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, controller, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.centerOnScreen()
        self.connect(self.lineEdit, QtCore.SIGNAL('textChanged(QString)'), self.lineEditChanged)
        self.controller = controller
        
    def lineEditChanged(self, text):
        self.controller.setFrom(text)
        
    def centerOnScreen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                (resolution.height() / 2) - (self.frameSize().height() / 2))
