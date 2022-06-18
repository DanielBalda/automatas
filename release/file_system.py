from tkinter import filedialog as fd
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
                self.lines = pd.read_csv(filename)
                self.lines = self.lines.splitlines()
        except Exception:
            return name, self.lines
        return name, self.lines
