#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 07:34:32 2021

@author: boeglinw
"""

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from comment_dialog_ui import Ui_commentDialog


# Dialog setup
class CommentDialog(qtw.QDialog):
    """ Comment Dialog """
    def __init__(self, lines = [], parent = None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_commentDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        # setup the initial text from a list of lines
        self.lines = lines
        txt = ''.join([s + '\n' for s in self.lines])
        self.ui.plainCommentTextEdit.setPlainText(txt)
        # connections
        self.ui.buttonBox.button(qtw.QDialogButtonBox.Ok).clicked.connect(self.get_current_text)        

    def get_current_text(self):
        # convert the text back to a list of lines once OK has been clicked
        self.lines = self.ui.plainCommentTextEdit.toPlainText().split('\n')




        
