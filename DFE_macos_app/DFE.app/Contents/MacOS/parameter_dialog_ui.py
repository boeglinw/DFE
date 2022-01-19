# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_parameterDialog(object):
    def setupUi(self, parameterDialog):
        parameterDialog.setObjectName("parameterDialog")
        parameterDialog.resize(427, 383)
        parameterDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(parameterDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(parameterDialog)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(100)
        self.tableView.horizontalHeader().setHighlightSections(True)
        self.tableView.horizontalHeader().setMinimumSectionSize(50)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setCascadingSectionResizes(False)
        self.tableView.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(parameterDialog)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(parameterDialog)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(parameterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(parameterDialog)
        self.buttonBox.accepted.connect(parameterDialog.accept)
        self.buttonBox.rejected.connect(parameterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(parameterDialog)

    def retranslateUi(self, parameterDialog):
        _translate = QtCore.QCoreApplication.translate
        parameterDialog.setWindowTitle(_translate("parameterDialog", "Dialog"))
        self.addButton.setText(_translate("parameterDialog", "Add"))
        self.deleteButton.setText(_translate("parameterDialog", "Delete"))

