#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:52:52 2021

test dialog

@author: boeglinw
"""

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

#from variable_dialog import VariableDialog

#from parameter_dialog import ParameterDialog 

#from header_dialog import HeaderDialog

#from new_dialog import NewDialog

# from comment_dialog import CommentDialog 
from float_display_dialog import FloatDisplayDialog

TestDialog = FloatDisplayDialog

class Window(QMainWindow):
    """Main window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        # Use a QPushButton for the central widget
        self.centralWidget = QPushButton("Start here...")
        # Connect the .clicked() signal with the .onEmployeeBtnClicked() slot
        self.centralWidget.clicked.connect(self.onStartClicked)
        self.setCentralWidget(self.centralWidget)

    # Create a slot for launching the employee dialog
    def onStartClicked(self):
        """Launch the variable dialog."""
        #dlg = ParameterDialog()
        #dlg = HeaderDialog()
        #dlg = VariableDialog()
        dlg = TestDialog()
        dlg.exec()
        # get values
        #print('result = ', dlg.result() )
        print('values = ', dlg.get_values())
        # print('final text = ', dlg.lines)
        
if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the application's main window
    win = Window()
    win.show()
    # Run the application's main loop
    sys.exit(app.exec())      
    
