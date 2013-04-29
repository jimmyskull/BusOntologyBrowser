# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SelectSpot.ui'
#
# Created: Mon Apr 29 16:56:13 2013
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

class Ui_SelectSpot(object):
    def setupUi(self, SelectSpot):
        SelectSpot.setObjectName(_fromUtf8("SelectSpot"))
        SelectSpot.resize(240, 320)
        SelectSpot.setMinimumSize(QtCore.QSize(240, 320))
        SelectSpot.setMaximumSize(QtCore.QSize(240, 320))
        font = QtGui.QFont()
        font.setPointSize(12)
        SelectSpot.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(SelectSpot)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit = QtGui.QLineEdit(SelectSpot)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.listWidget = QtGui.QListWidget(SelectSpot)
        self.listWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonBack = QtGui.QPushButton(SelectSpot)
        self.pushButtonBack.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButtonBack.setObjectName(_fromUtf8("pushButtonBack"))
        self.horizontalLayout.addWidget(self.pushButtonBack)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonOk = QtGui.QPushButton(SelectSpot)
        self.pushButtonOk.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SelectSpot)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), self.pushButtonOk.click)
        QtCore.QMetaObject.connectSlotsByName(SelectSpot)
        SelectSpot.setTabOrder(self.lineEdit, self.listWidget)
        SelectSpot.setTabOrder(self.listWidget, self.pushButtonBack)
        SelectSpot.setTabOrder(self.pushButtonBack, self.pushButtonOk)

    def retranslateUi(self, SelectSpot):
        SelectSpot.setWindowTitle(_translate("SelectSpot", "Gorpa NextBus", None))
        self.pushButtonBack.setText(_translate("SelectSpot", "Voltar", None))
        self.pushButtonOk.setText(_translate("SelectSpot", "Ok", None))

