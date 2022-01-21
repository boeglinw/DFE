# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'float_display_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FloatDisplayDialog(object):
    def setupUi(self, FloatDisplayDialog):
        FloatDisplayDialog.setObjectName("FloatDisplayDialog")
        FloatDisplayDialog.setWindowModality(QtCore.Qt.WindowModal)
        FloatDisplayDialog.resize(398, 129)
        FloatDisplayDialog.setModal(True)
        self.layoutWidget = QtWidgets.QWidget(FloatDisplayDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(17, 13, 371, 105))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.floatPrecisionLabel = QtWidgets.QLabel(self.layoutWidget)
        self.floatPrecisionLabel.setObjectName("floatPrecisionLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.floatPrecisionLabel)
        self.floatDisplayTypeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.floatDisplayTypeLabel.setObjectName("floatDisplayTypeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.floatDisplayTypeLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fix_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.fix_radioButton.setChecked(True)
        self.fix_radioButton.setObjectName("fix_radioButton")
        self.horizontalLayout.addWidget(self.fix_radioButton)
        self.sci_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.sci_radioButton.setObjectName("sci_radioButton")
        self.horizontalLayout.addWidget(self.sci_radioButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.floatPrecision_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.floatPrecision_spinBox.setObjectName("floatPrecision_spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.floatPrecision_spinBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FloatDisplayDialog)
        self.buttonBox.accepted.connect(FloatDisplayDialog.accept)
        self.buttonBox.rejected.connect(FloatDisplayDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FloatDisplayDialog)

    def retranslateUi(self, FloatDisplayDialog):
        _translate = QtCore.QCoreApplication.translate
        FloatDisplayDialog.setWindowTitle(_translate("FloatDisplayDialog", "Variable Name and Type"))
        self.floatPrecisionLabel.setText(_translate("FloatDisplayDialog", "Float  Precision"))
        self.floatDisplayTypeLabel.setText(_translate("FloatDisplayDialog", "Float Display Type"))
        self.fix_radioButton.setText(_translate("FloatDisplayDialog", "Fixed"))
        self.sci_radioButton.setText(_translate("FloatDisplayDialog", "Scientific"))

