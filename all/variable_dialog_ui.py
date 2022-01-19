# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'variable_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VariableDialog(object):
    def setupUi(self, VariableDialog):
        VariableDialog.setObjectName("VariableDialog")
        VariableDialog.setWindowModality(QtCore.Qt.WindowModal)
        VariableDialog.resize(402, 219)
        VariableDialog.setModal(True)
        self.layoutWidget = QtWidgets.QWidget(VariableDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(17, 13, 315, 102))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.variableNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.variableNameLabel.setObjectName("variableNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.variableNameLabel)
        self.variableNameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.variableNameEdit.setObjectName("variableNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.variableNameEdit)
        self.variableTypeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.variableTypeLabel.setObjectName("variableTypeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.variableTypeLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.float_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.float_radioButton.setChecked(True)
        self.float_radioButton.setObjectName("float_radioButton")
        self.horizontalLayout.addWidget(self.float_radioButton)
        self.integer_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.integer_radioButton.setObjectName("integer_radioButton")
        self.horizontalLayout.addWidget(self.integer_radioButton)
        self.string_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.string_radioButton.setObjectName("string_radioButton")
        self.horizontalLayout.addWidget(self.string_radioButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(VariableDialog)
        self.buttonBox.accepted.connect(VariableDialog.accept)
        self.buttonBox.rejected.connect(VariableDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VariableDialog)

    def retranslateUi(self, VariableDialog):
        _translate = QtCore.QCoreApplication.translate
        VariableDialog.setWindowTitle(_translate("VariableDialog", "Variable Name and Type"))
        self.variableNameLabel.setText(_translate("VariableDialog", "Variable name"))
        self.variableTypeLabel.setText(_translate("VariableDialog", "Variable type"))
        self.float_radioButton.setText(_translate("VariableDialog", "Float"))
        self.integer_radioButton.setText(_translate("VariableDialog", "Integer"))
        self.string_radioButton.setText(_translate("VariableDialog", "String"))

