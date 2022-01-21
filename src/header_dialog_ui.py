# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'header_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_headerDialog(object):
    def setupUi(self, headerDialog):
        headerDialog.setObjectName("headerDialog")
        headerDialog.resize(427, 383)
        headerDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(headerDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(headerDialog)
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(headerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(headerDialog)
        self.buttonBox.accepted.connect(headerDialog.accept)
        self.buttonBox.rejected.connect(headerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(headerDialog)

    def retranslateUi(self, headerDialog):
        _translate = QtCore.QCoreApplication.translate
        headerDialog.setWindowTitle(_translate("headerDialog", "Dialog"))

