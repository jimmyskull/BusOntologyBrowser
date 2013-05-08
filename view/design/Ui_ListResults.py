# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ListResults.ui'
#
# Created: Wed May  8 10:51:49 2013
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

class Ui_ListResults(object):
    def setupUi(self, ListResults):
        ListResults.setObjectName(_fromUtf8("ListResults"))
        ListResults.resize(260, 360)
        ListResults.setMinimumSize(QtCore.QSize(260, 360))
        ListResults.setMaximumSize(QtCore.QSize(260, 360))
        font = QtGui.QFont()
        font.setPointSize(12)
        ListResults.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(ListResults)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ListResults)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtGui.QListWidget(ListResults)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(ListResults)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ListResults)
        QtCore.QMetaObject.connectSlotsByName(ListResults)

    def retranslateUi(self, ListResults):
        ListResults.setWindowTitle(_translate("ListResults", "Gorpa NextBus", None))
        self.label.setText(_translate("ListResults", "TextLabel", None))
        self.pushButton.setText(_translate("ListResults", "Retroceder", None))

