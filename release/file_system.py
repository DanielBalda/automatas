from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from datetime import datetime
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, 'es_AR.utf8')


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
            listDayName = []
            listReason = []
            for lines in data:
                day = datetime.strptime(lines[1], '%d/%m/%Y')
                day = day.strftime("%A")
                listId.append(lines[0][0])
                listUser.append(lines[0][1])
                listDate.append(lines[1])
                listTime.append(lines[2])
                listDayName.append(day)
                listReason.append(lines[3])
            col0 = "ID"
            col1 = "Usuario"
            col2 = "Fecha Inicio"
            col3 = "Hora Inicio"
            col4 = "Día de la Semana"
            col5 = "Motivo"
            data = pd.DataFrame({col0: listId,
                                col1: listUser,
                                col2: listDate,
                                col3: listTime,
                                col4: listDayName,
                                col5: listReason})
            sheet = 'Datos - Inicio de Sesiones'
            writer = pd.ExcelWriter(file.name, engine="openpyxl")
            data.to_excel(writer, sheet_name=sheet)
            for col in data:
                col_idx = data.columns.get_loc(col)
                ch = chr(66+col_idx)
                dim = len(col)
                match ch:
                    case "B":
                        dim += 17
                        writer.sheets[sheet].column_dimensions[ch].width = dim
                    case "C":
                        dim += 15
                        writer.sheets[sheet].column_dimensions[ch].width = dim
                    case "D":
                        dim += 3
                        writer.sheets[sheet].column_dimensions[ch].width = dim
                    case "E":
                        writer.sheets[sheet].column_dimensions[ch].width = dim
                    case "F":
                        writer.sheets[sheet].column_dimensions[ch].width = dim
                    case "G":
                        dim += 30
                        writer.sheets[sheet].column_dimensions[ch].width = dim
            writer.save()
            return file.name.split('/')[-1]
        return False
