# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dfe_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRows = QtWidgets.QMenu(self.menubar)
        self.menuRows.setObjectName("menuRows")
        self.menuColumns = QtWidgets.QMenu(self.menubar)
        self.menuColumns.setObjectName("menuColumns")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.action_Edit_Parameters = QtWidgets.QAction(MainWindow)
        self.action_Edit_Parameters.setObjectName("action_Edit_Parameters")
        self.action_Edit_Headers = QtWidgets.QAction(MainWindow)
        self.action_Edit_Headers.setObjectName("action_Edit_Headers")
        self.actionInsert_Row_Above = QtWidgets.QAction(MainWindow)
        self.actionInsert_Row_Above.setObjectName("actionInsert_Row_Above")
        self.actionInsert_Row_Below = QtWidgets.QAction(MainWindow)
        self.actionInsert_Row_Below.setObjectName("actionInsert_Row_Below")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRemove_Rows = QtWidgets.QAction(MainWindow)
        self.actionRemove_Rows.setObjectName("actionRemove_Rows")
        self.actionAdd_Column_Right = QtWidgets.QAction(MainWindow)
        self.actionAdd_Column_Right.setObjectName("actionAdd_Column_Right")
        self.actionAdd_Column_Left = QtWidgets.QAction(MainWindow)
        self.actionAdd_Column_Left.setObjectName("actionAdd_Column_Left")
        self.actionRemove_Columns = QtWidgets.QAction(MainWindow)
        self.actionRemove_Columns.setObjectName("actionRemove_Columns")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionDuplicate_Row = QtWidgets.QAction(MainWindow)
        self.actionDuplicate_Row.setObjectName("actionDuplicate_Row")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.action_Edit_Parameters)
        self.menuEdit.addAction(self.action_Edit_Headers)
        self.menuRows.addAction(self.actionInsert_Row_Above)
        self.menuRows.addAction(self.actionInsert_Row_Below)
        self.menuRows.addAction(self.actionDuplicate_Row)
        self.menuRows.addSeparator()
        self.menuRows.addAction(self.actionRemove_Rows)
        self.menuColumns.addAction(self.actionAdd_Column_Right)
        self.menuColumns.addAction(self.actionAdd_Column_Left)
        self.menuColumns.addSeparator()
        self.menuColumns.addAction(self.actionRemove_Columns)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRows.menuAction())
        self.menubar.addAction(self.menuColumns.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRows.setTitle(_translate("MainWindow", "Rows"))
        self.menuColumns.setTitle(_translate("MainWindow", "Columns"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.action_Edit_Parameters.setText(_translate("MainWindow", "Parameters"))
        self.action_Edit_Headers.setText(_translate("MainWindow", "Headers"))
        self.actionInsert_Row_Above.setText(_translate("MainWindow", "Add Above"))
        self.actionInsert_Row_Below.setText(_translate("MainWindow", "Add Below"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionRemove_Rows.setText(_translate("MainWindow", "Remove Row(s)"))
        self.actionAdd_Column_Right.setText(_translate("MainWindow", "Add Right"))
        self.actionAdd_Column_Left.setText(_translate("MainWindow", "Add Left"))
        self.actionRemove_Columns.setText(_translate("MainWindow", "Remove Column(s)"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionDuplicate_Row.setText(_translate("MainWindow", "Duplicate "))
