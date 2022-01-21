#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:29:11 2021

@author: boeglinw
"""
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class HeaderDelegate(qtw.QItemDelegate):

    def __init__(self, parent = None):
        super(HeaderDelegate, self).__init__(parent)

    def createEditor(self, parent, styleOption, index):
        if index.column() == 1:
            editor = qtw.QComboBox(parent)
            editor.addItems(['f','i','s'])
            return editor

    def commitAndCloseEditor(self):
        editor = self.sender()
        self.commitData.emit(editor)
        self.closeEditor.emit(editor, qtw.QItemDelegate.NoHint)

    def setEditorData(self, editor, index):
        if isinstance(editor, qtw.QComboBox):
            print('setEditorData:', editor.currentText(), editor.currentIndex())
            # editor.setText(index.model().data(index, Qt.EditRole))

    def setModelData(self, editor, model, index):
        if isinstance(editor, qtw.QComboBox):
            print('setModelData:', editor.currentText(), editor.currentIndex())
            model.setData(index, editor.currentText(), qtc.Qt.EditRole)


class Model(qtc.QAbstractTableModel):
    def __init__(self):
        qtc.QAbstractTableModel.__init__(self)
        self.items = [[1, 'one', 'ONE'], [2, 'two', 'TWO'], [3, 'three', 'THREE']]

    def flags(self, index):
        return qtc.Qt.ItemIsEnabled | qtc.Qt.ItemIsEditable

    def rowCount(self, parent=qtc.QModelIndex()):
        return 3

    def columnCount(self, parent=qtc.QModelIndex()):
        return 3

    def data(self, index, role):
        if not index.isValid():
            return

        if role in [qtc.Qt.DisplayRole, qtc.Qt.EditRole]:
            return self.items[index.row()][index.column()]

    def setData(self, index, value, role):
        if index.isValid() and role == qtc.Qt.EditRole:
            self.items[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        else:
            return False


class MainWindow(qtw.QMainWindow):
    def __init__(self, parent=None):
        qtw.QMainWindow.__init__(self, parent)
        self.clipboard = qtw.QApplication.clipboard()
        mainWidget = qtw.QWidget()
        self.setCentralWidget(mainWidget)
        mainWidget.setLayout(qtw.QVBoxLayout())

        view = qtw.QTableView()
        view.setModel(Model())
        view.setItemDelegate(HeaderDelegate(view))
        self.layout().addWidget(view)
        self.show()
    


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())
