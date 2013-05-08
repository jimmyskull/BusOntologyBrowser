# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Route.ui'
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

class Ui_Route(object):
    def setupUi(self, Route):
        Route.setObjectName(_fromUtf8("Route"))
        Route.resize(240, 320)
        Route.setMinimumSize(QtCore.QSize(240, 320))
        Route.setMaximumSize(QtCore.QSize(240, 320))
        self.verticalLayout_4 = QtGui.QVBoxLayout(Route)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Route)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblFrom = QtGui.QLabel(Route)
        self.lblFrom.setObjectName(_fromUtf8("lblFrom"))
        self.horizontalLayout.addWidget(self.lblFrom)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(Route)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lblTo = QtGui.QLabel(Route)
        self.lblTo.setObjectName(_fromUtf8("lblTo"))
        self.horizontalLayout.addWidget(self.lblTo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(Route)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.lblPontoInicio = QtGui.QLabel(Route)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblPontoInicio.setFont(font)
        self.lblPontoInicio.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPontoInicio.setObjectName(_fromUtf8("lblPontoInicio"))
        self.verticalLayout_2.addWidget(self.lblPontoInicio)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_7 = QtGui.QLabel(Route)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.lblPontoChegada = QtGui.QLabel(Route)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblPontoChegada.setFont(font)
        self.lblPontoChegada.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPontoChegada.setObjectName(_fromUtf8("lblPontoChegada"))
        self.verticalLayout_3.addWidget(self.lblPontoChegada)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Route)
        QtCore.QMetaObject.connectSlotsByName(Route)

    def retranslateUi(self, Route):
        Route.setWindowTitle(_translate("Route", "Gorpa NextBus", None))
        self.label.setText(_translate("Route", "Rota:", None))
        self.lblFrom.setText(_translate("Route", "TextLabel", None))
        self.label_2.setText(_translate("Route", "→", None))
        self.lblTo.setText(_translate("Route", "TextLabel", None))
        self.label_5.setText(_translate("Route", "Ponto de início:", None))
        self.lblPontoInicio.setText(_translate("Route", "TextLabel", None))
        self.label_7.setText(_translate("Route", "Ponto de chegada:", None))
        self.lblPontoChegada.setText(_translate("Route", "TextLabel", None))

