# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comment_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_commentDialog(object):
    def setupUi(self, commentDialog):
        commentDialog.setObjectName("commentDialog")
        commentDialog.resize(829, 357)
        commentDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(commentDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainCommentTextEdit = QtWidgets.QPlainTextEdit(commentDialog)
        self.plainCommentTextEdit.setObjectName("plainCommentTextEdit")
        self.horizontalLayout.addWidget(self.plainCommentTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(commentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(commentDialog)
        self.buttonBox.accepted.connect(commentDialog.accept)
        self.buttonBox.rejected.connect(commentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(commentDialog)

    def retranslateUi(self, commentDialog):
        _translate = QtCore.QCoreApplication.translate
        commentDialog.setWindowTitle(_translate("commentDialog", "Dialog"))

