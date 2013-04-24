# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Destination.ui'
#
# Created: Wed Apr 24 14:50:28 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Destination(object):
    def setupUi(self, Destination):
        Destination.setObjectName(_fromUtf8("Destination"))
        Destination.resize(260, 360)
        Destination.setMinimumSize(QtCore.QSize(260, 360))
        Destination.setMaximumSize(QtCore.QSize(260, 360))
        font = QtGui.QFont()
        font.setPointSize(12)
        Destination.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Destination)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Destination)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(Destination)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.listWidget = QtGui.QListWidget(Destination)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(Destination)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Destination)
        QtCore.QMetaObject.connectSlotsByName(Destination)

    def retranslateUi(self, Destination):
        Destination.setWindowTitle(_translate("Destination", "Gorpa NextBus", None))
        self.label_2.setText(_translate("Destination", "Onde você quer ir?", None))
        self.pushButton.setText(_translate("Destination", "Aham", None))

