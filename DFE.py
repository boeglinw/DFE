# compile ui files using e.g. pyuic5 dfe_main_window.ui -o dfe_main_window.py 


import sys
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

import copy as C

from LT import pdatafile

from dfe_main_window import Ui_MainWindow
from variable_dialog import VariableDialog
from parameter_dialog import ParameterDialog
from header_dialog import HeaderDialog 
from new_dialog import NewDialog

# formats
fmt_conv_dict = {'f':float, 's':lambda x: x, 'i':int}

# default values

class datafileTableModel(qtc.QAbstractTableModel):
    """ The model for the datafile """
    def __init__(self, data_file , header_data = [], formats_data = {}, table_data = []): 
        super().__init__() 
        # filename given
        if data_file != '':
            self.filename = data_file
            try:
                self.df = pdatafile.pdfile(data_file)
            except:
                print(f'cannot open: {data_file}')
                return
            if (hasattr(self.df, "par")) and (self.df.par is not None):
                    # there are parameter data
                    self._parameter_names = self.df.par.get_variable_names()
                    self._parameter_values = [self.df.par[k] for k in self._parameter_names ]
            else:
                self._parameter_names = ['']
                self._parameter_values = ['']
                
            self._headers = self.df.keys[:-1]
            self._formats = self.df.formats  # this is a dict
            self._data = (self.df.get_data_list(':'.join( self.df.keys[:-1]))).tolist()
        else:
            # no filename given
            self.filename = 'new_file.data'
            self._headers = header_data
            self._formats = formats_data
            self._data = table_data
            self._parameter_names = ['']
            self._parameter_values = ['']

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._headers)  

    def data(self, index, role): 
        if role in (qtc.Qt.DisplayRole, qtc.Qt.EditRole):
            fmt = self._formats[ self._headers[index.column()]]
            val = self._data[index.row()][index.column()]
            try:
                return f'{fmt_conv_dict[fmt](val)}'
            except:
                return f'{val}'
        
    def headerData(self, section, orientation, role):

        if orientation == qtc.Qt.Horizontal and role == qtc.Qt.DisplayRole:
            return self._headers[section]
        else:
            return super().headerData(section, orientation, role)

    def sort(self, column, order):
        self.layoutAboutToBeChanged.emit()  # needs to be emitted before a sort
        try:
            self._data.sort(key=lambda x: x[column])
        except:
            print(f'Problem sorting different types, sort as string in column {column}')
            for i,r in enumerate(self._data):
                print(f'row = {i}, value = {r[column]},  type = {type(r[column])}')
            self._data.sort(key=lambda x: f'{x[column]}')
        if order == qtc.Qt.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()  # needs to be emitted after a sort

    def flags(self, index):
        return super().flags(index) | qtc.Qt.ItemIsEditable

    def setData(self, index, value, role):
        if index.isValid() and role == qtc.Qt.EditRole:
            # get the correct format
            fmt = self._formats[ self._headers[index.column()]]
            try:
                val = fmt_conv_dict[fmt](value)
            except:
                val = value
            self._data[index.row()][index.column()] = val
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

    def duplicateRow(self, position, row, parent):
        self.beginInsertRows(
            parent or qtc.QModelIndex(),
            position ,
            position + row - 1
        )
        new_row = self._data[position - 1]
        self._data.insert(position, new_row)
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

    # method for saving
    def save_data(self, new_file):

        with open(new_file, 'w', encoding='utf-8') as fh:
            # write parameters if anu
            for i, p_name in enumerate(self._parameter_names):
                p_l = f'#\\ {p_name} = {self._parameter_values[i]}\n'
                fh.write(p_l)
            # assemble header line
            hl = '#! '
            for i,k in enumerate(self._headers):
                hl += f'{k}[{self._formats[k]}, {i}]/ '
            fh.write(hl + '\n')
            for d in self._data:
                l = ''
                for i, x in enumerate(d):
                    fmt = self._formats[ self._headers[i] ]
                    try:
                        val = fmt_conv_dict[fmt](x)
                    except: 
                        if x == '':
                            val = 'No_Entry'
                        else:
                            val = x    
                    l += f'{val} '
                fh.write(l + '\n')

    def get_parameters(self):
        return self._parameter_names, self._parameter_values
    
    def set_parameters(self, names, values):
        self._parameter_names = names
        self._parameter_values = values
        
    def get_headers(self):
        return self._headers, [self._formats[k] for k in self._headers]
    
    def set_headers(self, new_header):
        self._headers = list(new_header.keys())
        self._formats = new_header
        # send header change signal
        self.headerDataChanged.emit(qtc.Qt.Horizontal, 0, len(self._headers) - 1 )
        
# inserting and removing cols

    def insertColumns(self, position, cols, header_str, fmt_str, parent):
        self.beginInsertColumns(
            parent or qtc.QModelIndex(),
            position,
            position + cols - 1
        )
        for i in range(cols):
            self._headers.insert(position, header_str)
            self._formats[header_str] = fmt_str
        for row in self._data:
            for i in range(cols):
                row.insert(position, '')
        self.endInsertColumns()

    def removeColumns(self, position, cols,  parent):
        self.beginRemoveColumns(
            parent or qtc.QModelIndex(),
            position,
            position + cols - 1
        )
        for i in range(cols):
            header_str = self._headers[position]
            del(self._formats[header_str])
            del(self._headers[position])            
        for row in self._data:
            for i in range(cols):
                del(row[position])
        self.endRemoveColumns()




class MainWindow(qtw.QMainWindow, Ui_MainWindow):

    model = None

    def __init__(self):
        super(MainWindow, self).__init__()
        # setup UI
        self.setupUi(self)
        # Create an instance of the GUI

        # setup connections
        
        # File menu
        self.actionOpen.triggered.connect(self.select_file)
        self.actionNew.triggered.connect(self.new_file)
        self.actionSave.triggered.connect( self.save_file)
        self.actionSave_As.triggered.connect( self.save_file_as)
        #self.actionQuit.triggered.connect(self.close)
        #self.actionQuit.triggered.connect(qtw.QApplication.quit)
        self.actionQuit.triggered.connect(self.quit_all)
        
        # Edit menu
        self.actionInsert_Row_Above.triggered.connect(self.insert_row_above)
        self.actionInsert_Row_Below.triggered.connect(self.insert_row_below)
        self.actionDuplicate_Row.triggered.connect(self.duplicate_row)
        
        self.actionRemove_Rows.triggered.connect(self.remove_rows)
        
        self.actionAdd_Column_Right.triggered.connect(self.insert_col_right)
        self.actionAdd_Column_Left.triggered.connect(self.insert_col_left)
        self.actionRemove_Columns.triggered.connect(self.remove_cols)
        
        # edit parameters menu
        self.action_Edit_Parameters.triggered.connect(self.edit_parameters)
        
        # edit headers menu
        self.action_Edit_Headers.triggered.connect(self.edit_headers)
        # End main UI code
        self.show()
        self.current_dir = os.path.expanduser("~")  # initialize to home directory
        qtc.QDir.setCurrent(self.current_dir)
        
    # File methods
    
    
    def select_file(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            'Select a datafile to open…',
            qtc.QDir.currentPath(),
            'datafile Files (*.data) ;; All Files (*)'
        )
        if filename:
            loc_directory, f_name = os.path.split(filename)
            self.current_dir = loc_directory
            qtc.QDir.setCurrent(loc_directory)
            self.model = datafileTableModel(filename)
            self.tableView.setModel(self.model)
            self.setWindowTitle(filename)
            """
            for i in range(self.tableView.horizontalHeader().count()):
                # set properties
                self.tableView.horizontalHeader().setSectionResizeMode(i, qtw.QHeaderView.Stretch)
            """


    def new_file(self):
        dlg = NewDialog()
        dlg.exec()
        if dlg.result():
            n_col, n_row = dlg.get_values()
            # generate some default values
            headers_def = [f'C{n}' for n in range(n_col)]
            fmt = n_col*['f']
            formats_def = dict(zip(headers_def, fmt))
            data_def = []
            for r in range(n_row):
                data_def.append([0. for c in range(n_col)])
                # initialize table
            self.model = datafileTableModel('', header_data = headers_def, formats_data = formats_def, table_data = data_def)
            self.tableView.setModel(self.model)
            self.setWindowTitle('New File')


    def save_file(self):
        if self.model:
            if self.model.filename == '':
                self.safe_file_as()
            else:
                self.model.save_data(self.model.filename)

    def save_file_as(self):
        new_filename, _ = qtw.QFileDialog.getSaveFileName(
            self,
            'Save data as',
            qtc.QDir.currentPath(),
            'datafile Files (*.data) ;; All Files (*)'
        )
        
        if self.model and new_filename:
            loc_directory, f_name = os.path.split(new_filename)
            self.current_dir = loc_directory
            qtc.QDir.setCurrent(loc_directory)            
            self.model.save_data(new_filename)
            self.model.filename = new_filename
            self.setWindowTitle(new_filename)
            
    def quit_all(self):
        self.close()
        qtw.QApplication.quit()
        
    # Methods for insert/remove

    def insert_row_above(self):
        selected = self.tableView.selectedIndexes()
        row = selected[0].row() if selected else 0
        self.model.insertRows(row, 1, None)

    def insert_row_below(self):
        selected = self.tableView.selectedIndexes()
        row = selected[-1].row() if selected else self.model.rowCount(None)
        self.model.insertRows(row + 1, 1, None)

    def duplicate_row(self):
        selected = self.tableView.selectedIndexes()
        row = selected[-1].row() if selected else self.model.rowCount(None)
        self.model.duplicateRow(row + 1, 1, None)

    def remove_rows(self):
        selected = self.tableView.selectedIndexes()
        start_row = selected[0].row()
        end_row = selected[-1].row()
        number_of_rows = abs(end_row - start_row) + 1 
        if selected:
            self.model.removeRows(start_row, number_of_rows, None)
            
    def get_variable_name(self):
        # get new header name
        v_name = ''
        dlg = VariableDialog(self)
        dlg.exec()
        v_name = dlg.get_name()
        v_type = dlg.get_type()
        return v_name, v_type
    
            
    def insert_col_left(self):
        v_name, v_type = self.get_variable_name()
        if v_name == '':
            return
        selected = self.tableView.selectedIndexes()
        col = selected[0].column() if selected else 0
        self.model.insertColumns(col, 1, v_name, v_type, None)

    def insert_col_right(self):
        v_name, v_type = self.get_variable_name()
        if v_name == '':
            return
        selected = self.tableView.selectedIndexes()
        col = selected[0].column() if selected else 0
        loc = col + 1
        self.model.insertColumns(loc, 1, v_name, v_type, None)

    def remove_cols(self):
        selected = self.tableView.selectedIndexes()
        start_col = selected[0].column()
        end_col = selected[-1].column()
        number_of_cols = abs(end_col - start_col) + 1 
        if selected:
            self.model.removeColumns(start_col, number_of_cols, None)

    def edit_parameters(self):
        p_names, p_values = self.model.get_parameters()
        dlg = ParameterDialog(names = p_names, values = p_values)
        dlg.exec()
        if dlg.result():
            names = dlg.get_names()
            values = dlg.get_values()
            self.model.set_parameters(names, values)

    def edit_headers(self):
        h_names, h_types = self.model.get_headers()
        dlg = HeaderDialog(names = h_names, types = h_types)
        dlg.exec()
        if dlg.result():
            names = dlg.get_names()
            types = dlg.get_types()
            new_header = dict(zip(names, types))
            self.model.set_headers(new_header)

#%%
if __name__ == '__main__':
    # for running from withing Spyder
    # def run_app():
    if not qtw.QApplication.instance():
        app = qtw.QApplication(sys.argv)
    else:
        app = qtw.QApplication.instance()
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    app.exec_()
    # run_app()
    """
    # for stand alone
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec_())
    """
