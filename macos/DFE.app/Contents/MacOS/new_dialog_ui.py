# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newDialog(object):
    def setupUi(self, newDialog):
        newDialog.setObjectName("newDialog")
        newDialog.resize(232, 164)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(newDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelNrColumn = QtWidgets.QLabel(newDialog)
        self.labelNrColumn.setObjectName("labelNrColumn")
        self.horizontalLayout.addWidget(self.labelNrColumn)
        self.spinBox_Columns = QtWidgets.QSpinBox(newDialog)
        self.spinBox_Columns.setMinimum(1)
        self.spinBox_Columns.setObjectName("spinBox_Columns")
        self.horizontalLayout.addWidget(self.spinBox_Columns)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelNr_Rows = QtWidgets.QLabel(newDialog)
        self.labelNr_Rows.setObjectName("labelNr_Rows")
        self.horizontalLayout_2.addWidget(self.labelNr_Rows)
        self.spinBox_Rows = QtWidgets.QSpinBox(newDialog)
        self.spinBox_Rows.setMinimum(1)
        self.spinBox_Rows.setObjectName("spinBox_Rows")
        self.horizontalLayout_2.addWidget(self.spinBox_Rows)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(newDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(newDialog)
        self.buttonBox.accepted.connect(newDialog.accept)
        self.buttonBox.rejected.connect(newDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(newDialog)

    def retranslateUi(self, newDialog):
        _translate = QtCore.QCoreApplication.translate
        newDialog.setWindowTitle(_translate("newDialog", "Dialog"))
        self.labelNrColumn.setText(_translate("newDialog", "Number of Columns"))
        self.labelNr_Rows.setText(_translate("newDialog", "Number of Rows      "))

