#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 07:00:11 2021

@author: boeglinw
"""
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from header_dialog_ui import Ui_headerDialog

class HeaderDelegate(qtw.QItemDelegate):

    def __init__(self, parent = None):
        super(HeaderDelegate, self).__init__(parent)

    def createEditor(self, parent, styleOption, index):
        if index.column() == 1:
            editor = qtw.QComboBox(parent)
            editor.addItems(['f','i','s'])
            return editor
        editor = qtw.QLineEdit(parent)
        editor.editingFinished.connect(self.commitAndCloseEditor)
        return editor        

    def commitAndCloseEditor(self):
        editor = self.sender()
        self.commitData.emit(editor)
        self.closeEditor.emit(editor, qtw.QItemDelegate.NoHint)

    def setEditorData(self, editor, index):
        if isinstance(editor, qtw.QComboBox):
            pass
            # editor.setText(index.model().data(index, Qt.EditRole))
        elif isinstance(editor, qtw.QLineEdit):
            editor.setText(index.model().data(index, qtc.Qt.EditRole))

    def setModelData(self, editor, model, index):
        if isinstance(editor, qtw.QComboBox):
            model.setData(index, editor.currentText(), qtc.Qt.EditRole)
        elif isinstance(editor, qtw.QLineEdit):
            model.setData(index, editor.text(), qtc.Qt.EditRole )
            


class headerTableModel(qtc.QAbstractTableModel):
    """ The model for header data """
    def __init__(self, names, types): 
        super().__init__() 
        self._headers = ['Header Name', 'Header Type']
        self._data = [list(l) for l in zip(names, types)]
    
    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._headers)  

    def data(self, index, role):
        if role in (qtc.Qt.DisplayRole, qtc.Qt.EditRole):
            return self._data[index.row()][index.column()]
        
    def headerData(self, section, orientation, role):

        if orientation == qtc.Qt.Horizontal and role == qtc.Qt.DisplayRole:
            return self._headers[section]
        else:
            return super().headerData(section, orientation, role)

    def sort(self, column, order):
        self.layoutAboutToBeChanged.emit()  # needs to be emitted before a sort
        self._data.sort(key=lambda x: x[column])
        if order == qtc.Qt.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()  # needs to be emitted after a sort

    def flags(self, index):
        return super().flags(index) | qtc.Qt.ItemIsEditable

    def setData(self, index, value, role):
        if index.isValid() and role == qtc.Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        else:
            return False
        
    def show_headers(self):
        for i, d in enumerate(self._data):
            print(f'header {i} : {d[0]} = {d[1]}')



# Dialog setup
class HeaderDialog(qtw.QDialog):
    """ header Dialog """
    def __init__(self, parent = None, names = [''], types = ['']):
        super().__init__(parent)
        # default names and types
        self.names = names
        self.types = types 
        # Create an instance of the GUI
        self.ui = Ui_headerDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

        self.model = headerTableModel(names, types)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.ui.tableView.setItemDelegate(HeaderDelegate(self.ui.tableView))
        # connections
        self.ui.buttonBox.button(qtw.QDialogButtonBox.Ok).clicked.connect(self.prepare_headers)
        

    def prepare_headers(self):
        self.names = [d[0] for d in self.model._data]
        self.types = [d[1] for d in self.model._data]
        
    def get_names(self):
        return self.names
    
    def get_types(self):
        return self.types
    
        
