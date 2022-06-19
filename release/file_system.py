from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
import pandas as pd


class File_System():
    def __init__(self):
        self.filetypes = (('text files', '*.txt'),
                          ('text files', '*.xlsx'),
                          ('text files', '*.csv'))

    def open(self):
        filename = ""
        self.lines = ""
        try:
            filename = fd.askopenfilename(
                       title='Open a file',
                       initialdir='/',
                       filetypes=self.filetypes)
            name = filename.split('/')[-1]
            if('.txt' in name):
                with open(filename, 'r') as dataFile:
                    self.lines = dataFile.readlines()
            if('.xlsx' in name):
                excel = pd.read_excel(filename, index_col=0)
                self.lines = excel.to_csv(encoding='utf-8',
                                          sep=';',
                                          date_format="%d/%m/%Y %H:%M")
                self.lines = self.lines.splitlines()
            if('.csv' in name):
                with open(filename, 'r') as dataFile:
                    self.lines = dataFile.readlines()
        except Exception:
            return name, self.lines
        return name, self.lines

    def export(self, data):
        files = [('EXCEL', '*.xlsx')]
        file = asksaveasfile(filetypes=files, defaultextension=files)
        if(file):
            listId = []
            listUser = []
            listDate = []
            listTime = []
            for lines in data:
                listId.append(lines[0][0])
                listUser.append(lines[0][1])
                listDate.append(lines[1])
                listTime.append(lines[2])
            col0 = "ID"
            col1 = "Usuario"
            col2 = "Fecha Inicio"
            col3 = "Hora Inicio"
            data = pd.DataFrame({col0: listId,
                                col1: listUser,
                                col2: listDate,
                                col3: listTime})
            sheet = 'Datos - Inicio de Sesiones'
            writer = pd.ExcelWriter(file.name, engine="openpyxl")
            data.to_excel(writer, sheet_name=sheet)
            for col in data:
                col_idx = data.columns.get_loc(col)
                ch = chr(65+col_idx)
                dim = len(col) + 15
                if ch != 'A':
                    writer.sheets[sheet].column_dimensions[ch].width = dim

            writer.save()
            return file.name.split('/')[-1]
        return False
