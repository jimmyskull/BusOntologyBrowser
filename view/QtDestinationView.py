# -*- encoding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from design.Ui_SelectSpot import Ui_SelectSpot, _fromUtf8

class QtDestinationView(QtGui.QWidget, Ui_SelectSpot):
    def __init__(self, controller, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.centerOnScreen()
        self.setObjectName("DestinationView")
        self.connect(self.lineEdit, QtCore.SIGNAL('textChanged(QString)'), self.lineEditChanged)
        self.connect(self.pushButtonOk, QtCore.SIGNAL('clicked()'), self.pushButtonOkClick)
        self.connect(self.pushButtonBack, QtCore.SIGNAL('clicked()'), self.pushButtonBackClick)
        self.lineEdit.setPlaceholderText(_fromUtf8('Onde você quer ir?'))
        self.controller = controller
        
    def setContent(self, data):
        l = [r[0].encode('iso-8859-1').decode('utf8') for r in data]
        self.data = l
        self.listWidget.clear()
        self.listWidget.addItems(sorted(set(l)))
        
    def lineEditChanged(self, text):
        self.controller.updateSpotList(self, text)
        
    def pushButtonOkClick(self):
        item = self.listWidget.currentItem()
        if item:
            text = str(item.text().toUtf8()).decode('utf8')
            for i, t in enumerate(self.data):
                if text == t:
                    self.controller.selectSpot(self, i)
                    return
    
    def pushButtonBackClick(self):
        self.controller.GoBack(self)
        
    def centerOnScreen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                (resolution.height() / 2) - (self.frameSize().height() / 2))
