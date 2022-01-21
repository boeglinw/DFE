#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 07:34:32 2021

@author: boeglinw
"""

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from float_display_dialog_ui import Ui_FloatDisplayDialog

# Dialog setup
class FloatDisplayDialog(qtw.QDialog):
    """ Comment Dialog """
    def __init__(self, fmt, prec, parent = None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_FloatDisplayDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self, )
        # setup the initial text from a list of lines
        self.prec = prec
        self.float_format = fmt
        # setup precision initial valeus
        self.ui.floatPrecision_spinBox.setValue(self.prec)
        # setup check box
        if fmt == 'f':
            self.ui.fix_radioButton.setChecked(True)
        else:
            self.ui.fix_radioButton.setChecked(False)
            self.ui.sci_radioButton.setChecked(True)
        # connections
        self.ui.buttonBox.button(qtw.QDialogButtonBox.Ok).clicked.connect(self.get_values)        

    def get_values(self):
        # return the current values of the dialog
        self.prec = self.ui.floatPrecision_spinBox.value()
        if self.ui.fix_radioButton.isChecked():
            self.float_format = 'f'
        else:
            self.float_format = 'e'
        return self.float_format, self.prec

        





        
