#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 07:00:11 2021

@author: boeglinw
"""
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from parameter_dialog_ui import Ui_parameterDialog

class parameterTableModel(qtc.QAbstractTableModel):
    """ The model for parameter data """
    def __init__(self, names, values): 
        super().__init__() 
        self._headers = ['Parameter Name', 'Parameter Value']
        self._data = [list(l) for l in zip(names, values)]
    
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

    # Methods for inserting or deleting

    def insertRows(self, position, rows, parent):
        self.beginInsertRows(
            parent or qtc.QModelIndex(),
            position,
            position + rows - 1
        )

        for i in range(rows):
            default_row = [''] * len(self._headers)
            self._data.insert(position, default_row)
        self.endInsertRows()

    def removeRows(self, position, rows, parent):
        self.beginRemoveRows(
            parent or qtc.QModelIndex(),
            position,
            position + rows - 1
        )
        for i in range(rows):
            del(self._data[position])
        self.endRemoveRows()
        
    def show_parameters(self):
        for i, d in enumerate(self._data):
            print(f'Parameter {i} : {d[0]} = {d[1]}')



# Dialog setup
class ParameterDialog(qtw.QDialog):
    """ Parameter Dialog """
    def __init__(self, parent = None, names = [''], values = ['']):
        super().__init__(parent)
        # default values
        self.names = names
        self.values = values 
        # Create an instance of the GUI
        self.ui = Ui_parameterDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

        self.model = parameterTableModel(names, values)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        # connections
        self.ui.addButton.clicked.connect(self.add_parameter)
        self.ui.deleteButton.clicked.connect(self.delete_parameter)
        self.ui.buttonBox.button(qtw.QDialogButtonBox.Ok).clicked.connect(self.prepare_parameters)
        self.ui.buttonBox.button(qtw.QDialogButtonBox.Apply).clicked.connect(self.prepare_parameters)
        
    def add_parameter(self):
        selected = self.ui.tableView.selectedIndexes()
        row = selected[-1].row() if selected else self.model.rowCount(None)
        self.model.insertRows(row + 1, 1, None)

    def delete_parameter(self):
        selected = self.ui.tableView.selectedIndexes()
        start_row = selected[0].row()
        end_row = selected[-1].row()
        number_of_rows = abs(end_row - start_row) + 1 
        if selected:
            self.model.removeRows(start_row, number_of_rows, None)    
            
    def prepare_parameters(self):
        self.names = [d[0] for d in self.model._data]
        self.values = [d[1] for d in self.model._data]
        
    def get_names(self):
        return self.names
    
    def get_values(self):
        return self.values
        
        
