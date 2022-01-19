#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:02:06 2021

@author: boeglinw
"""
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

from variable_dialog_ui import Ui_VariableDialog

class VariableDialog(QDialog):
    """ Variable Dialog """
    def __init__(self, parent = None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_VariableDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        
    def get_name(self):
        if self.result():
            return self.ui.variableNameEdit.text()
        else:
            return ''
    
    def get_type(self):
        # determine variable type
        if not self.result():
            return ''
        if self.ui.float_radioButton.isChecked():
            v_type = 'f'
        elif self.ui.integer_radioButton.isChecked():
            v_type = 'i'
        else:
            v_type = 's'
        return v_type