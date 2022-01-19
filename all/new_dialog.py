#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 07:34:32 2021

@author: boeglinw
"""

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from new_dialog_ui import Ui_newDialog


# Dialog setup
class NewDialog(qtw.QDialog):
    """ Parameter Dialog """
    def __init__(self, parent = None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_newDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

        # connections
        self.ui.buttonBox.button(qtw.QDialogButtonBox.Ok).clicked.connect(self.store_values)
                    
    def store_values(self):
        self.n_columns = self.ui.spinBox_Columns.value()
        self.n_rows = self.ui.spinBox_Rows.value()
        
    def get_values(self):
        return self.n_columns, self.n_rows

        
