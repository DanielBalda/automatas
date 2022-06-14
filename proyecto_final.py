# Seguimiento de los usuarios que se han conectado días feriados y
# no laborables (sábados y domingos).
# Debe incluir la posibilidad de ingresar un rango de fechas


import tkinter
import os
import sys
import requests
import re
import pandas as pd
import time as tm
from tkinter import filedialog as fd
from datetime import date


class Interface():

    def __init__(self):
        self.apiData()
        self.weekends()
        self.window = tkinter.Tk()
        self.window.config(background="#333333")
        self.window.title("Final Autómatas y Gramáticas")
        self.window.iconbitmap(self.resource_path('./um.ico'))
        self.window.resizable(False, False)
        w = 900
        h = 900
        xPos = self.window.winfo_screenwidth()/2-w/2
        yPos = self.window.winfo_screenheight()/2-h/2
        self.window.geometry('%dx%d+%d+%d' % (w, h, xPos, yPos))

        btnOpen = tkinter.Button(self.window,
                                 text="Abrir Archivo",
                                 width=14,
                                 height=2,
                                 background="#519ABA",
                                 border=0,
                                 fg="#FFFFFF",
                                 font="Helvetica 10 bold",
                                 activebackground='#1E1E1E',
                                 activeforeground='#519ABA',
                                 relief='solid',
                                 command=lambda: self.select_file())

        dateTitle = tkinter.Label(self.window,
                                  text="Búsqueda por Fecha:",
                                  font='Helvetica 20 bold',
                                  background="#333333",
                                  fg="#519ABA")

        title1 = tkinter.Label(self.window,
                               text="Desde:",
                               font='Helvetica 20 bold',
                               background="#333333",
                               fg="#519ABA")

        self.calFirst = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      font="Helvetica 20 bold",
                                      highlightthickness=1,
                                      width=10)

        title2 = tkinter.Label(self.window,
                               text="Hasta:",
                               font='Helvetica 20 bold',
                               background="#333333",
                               fg="#519ABA")

        self.calLast = tkinter.Entry(self.window,
                                     background="#606060",
                                     fg="#FFFFFF",
                                     font="Helvetica 20 bold",
                                     highlightthickness=1,
                                     width=10)

        self.btnFilter = tkinter.Button(self.window,
                                        state='disabled',
                                        text=" BUSCAR ",
                                        width=18,
                                        height=2,
                                        background="#519ABA",
                                        border=0,
                                        fg="#FFFFFF",
                                        font="Helvetica 10 bold",
                                        activebackground='#1E1E1E',
                                        activeforeground='#519ABA',
                                        relief='solid',
                                        command=lambda: self.main(1))

        title3 = tkinter.Label(self.window,
                               text="Resultados:",
                               font='Helvetica 20 bold',
                               background="#333333",
                               fg="#519ABA")

        scroll = tkinter.Scrollbar(self.window,
                                   orient='vertical')

        self.textBox = tkinter.Text(self.window,
                                    width=58,
                                    height=19,
                                    background="#1E1E1E",
                                    font=("Helvetica", 20),
                                    yscrollcommand=scroll.set)
        self.textBox.tag_configure("lightblue", foreground="#11A8CD")
        scroll.config(command=self.textBox.yview)

        self.btnExport = tkinter.Button(self.window,
                                        state='disabled',
                                        text=" Exportar ",
                                        width=15,
                                        height=2,
                                        background="#519ABA",
                                        border=0,
                                        fg="#FFFFFF",
                                        font="Helvetica 10 bold",
                                        activebackground='#1E1E1E',
                                        activeforeground='#519ABA',
                                        relief='solid',
                                        command=lambda: self.main(2))

        self.registerText = tkinter.Label(self.window,
                                          text="Total:",
                                          font='Helvetica 10 bold',
                                          background="#333333",
                                          fg="white")

        self.filterText = tkinter.Label(self.window,
                                        text="Filtrados:",
                                        font='Helvetica 10 bold',
                                        background="#333333",
                                        fg="white")

        self.errorText = tkinter.Label(self.window,
                                       text="Errores:",
                                       font='Helvetica 10 bold',
                                       background="#333333",
                                       fg="white")

        btnExit = tkinter.Button(self.window,
                                 text=" SALIR ",
                                 width=10,
                                 height=2,
                                 background="#519ABA",
                                 border=0,
                                 fg="#FFFFFF",
                                 font="Helvetica 10 bold",
                                 activebackground='#1E1E1E',
                                 activeforeground='#519ABA',
                                 relief='solid',
                                 command=lambda: self.main(3))

        # Posicion de los elementos
        btnOpen.place(x=20, y=10)
        dateTitle.place(x=310, y=10)
        title1.place(x=110, y=70)
        self.calFirst.place(x=220, y=70)
        title2.place(x=480, y=70)
        self.calLast.place(x=575, y=70)
        self.btnFilter.place(x=380, y=135)
        title3.place(x=372, y=185)
        scroll.place(x=878, y=220, height=612)
        self.textBox.place(x=4, y=220)
        self.btnExport.place(x=20, y=845)
        self.registerText.place(x=180, y=854)
        self.filterText.place(x=400, y=854)
        self.errorText.place(x=660, y=854)
        btnExit.place(x=790, y=845)

        # Crea y muestra la interfaz
        self.window.mainloop()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def select_file(self):
        try:
            filetypes = (('text files', '*.txt'),
                         ('text files', '*.xlsx'),
                         ('text files', '*.csv'))
            self.filename = fd.askopenfilename(
                            title='Open a file',
                            initialdir='/',
                            filetypes=filetypes)
            with open(self.filename, 'r') as dataFile:
                self.lines = dataFile.readlines()
            self.window.title("Final Autómatas y Gramáticas | Archivo: " +
                              self.filename.split('/')[-1])
            self.btnFilter['state'] = 'normal'
        except Exception:
            pass
        return

    def apiData(self):
        self.date = []
        for anio in range(2016, date.today().year+1):
            url = 'http://nolaborables.com.ar/api/v2/feriados/'+str(anio)
            response = requests.get(url)
            if(response.status_code == 200):
                for element in response.json():
                    self.date.append(f'{element["dia"]:02d}/' +
                                     f'{element["mes"]:02d}/' +
                                     str(anio))
            else:
                # Aca deberiamos tener un archivo con los feriados
                # en caso de que la API no responda
                # o tener una exepcion ante el error y reintentar unas 3 veces
                pass
        return self.date

    def weekends(self):
        zone = 'America/Argentina/Buenos_Aires'
        self.weekendsDate = pd.bdate_range(start=str(2016),
                                           end=str(date.today().year+1),
                                           freq="C",
                                           weekmask="Sat Sun",
                                           tz=zone).strftime('%d/%m/%Y').tolist()
        return self.weekendsDate

    def checkInputs(self):
        REpatternDate = r'(?:3[01]|[12][0-9]|0?[1-9])([-/])(0?[1-9]|1[1-2])\1\d{4}'
        checkDate = 0
        self.flag = 0
        if(self.calFirst.get() == "" and self.calLast.get() == ""):
            self.calFirst.config(highlightbackground="#519ABA",
                                 highlightcolor="#519ABA")
            self.calLast.config(highlightbackground="#519ABA",
                                highlightcolor="#519ABA")
            return True
        if re.match(REpatternDate, self.calFirst.get()) is None:
            self.calFirst.config(highlightbackground="#cf0909",
                                 highlightcolor="#cf0909")
        else:
            self.calFirst.config(highlightbackground="#85e52e",
                                 highlightcolor="#85e52e")
            checkDate += 1
        if re.match(REpatternDate, self.calLast.get()) is None:
            self.calLast.config(highlightbackground="#cf0909",
                                highlightcolor="#cf0909")
        else:
            self.calLast.config(highlightbackground="#85e52e",
                                highlightcolor="#85e52e")
            checkDate += 1
        if(checkDate == 2):
            self.flag = 1
            return True
        return False

    def checkId(self, id):
        REpatternId = r'([a-z0-9]{16})'
        if re.match(REpatternId, id):
            return True
        return False

    def checkDate(self, date):
        # formato 00/00/0000
        REpatternDate = r'(?:3[01]|[12][0-9]|0?[1-9])([-/])(0?[1-9]|1[1-2])\1\d{4}'
        if re.match(REpatternDate, date):
            return True
        return False

    def checkTime(self, time):
        # formato 24Hs
        REpatternDate = r'([0-1][0-9]|2[0-3])(:)([0-5][0-9])'
        if re.match(REpatternDate, time):
            return True
        return False

    def simpleSearch(self):
        errors = 0
        filter = 0
        self.export = []
        for index, line in enumerate(self.lines):
            line = line.split(";")
            if(index > 0 and len(line[0]) > 0 and len(line[2]) > 0):
                date, time = line[2].split(' ')
                if(self.checkId(line[0]) and self.checkDate(date) and self.checkTime(time)):
                    if(date in self.date or date in self.weekendsDate):
                        resultsBox = "User: "+line[1] + \
                                     " - Fecha: "+date + \
                                     " - Hora: "+time + \
                                     "\n"
                        self.textBox.insert(tkinter.INSERT,
                                            resultsBox,
                                            'lightblue')
                        self.filterText.config(text=f'Filtrados: {filter}')
                        filter += 1
            else:
                self.errorText.config(text=f'Errores: {errors}')
                errors += 1
            self.registerText.config(text=f'Total: {index}')

    def rangeSearch(self):
        errors = 0
        filter = 0
        self.export = []
        for index, line in enumerate(self.lines):
            line = line.split(";")
            if(index > 0 and len(line[0]) > 0 and len(line[2]) > 0):
                date, time = line[2].split(' ')
                if(self.checkId(line[0]) and self.checkDate(date) and self.checkTime(time)):
                    dateFile = tm.strptime(date, "%d/%m/%Y")
                    First = tm.strptime(self.calFirst.get(),
                                        "%d/%m/%Y")
                    Last = tm.strptime(self.calLast.get(),
                                       "%d/%m/%Y")
                    if(dateFile >= First and dateFile <= Last):
                        if(date in self.date or date in self.weekendsDate):
                            resultsBox = "User: "+line[1] + \
                                         " - Fecha: "+date + \
                                         " - Hora: "+time + \
                                         "\n"
                            self.textBox.insert(tkinter.INSERT,
                                                resultsBox,
                                                'lightblue')
                            self.filterText.config(text=f'Filtrados: {filter}')
                            filter += 1
            else:
                self.errorText.config(text=f'Errores: {errors}')
                errors += 1
            self.registerText.config(text=f'Total: {index}')

    def main(self, option):
        if(option == 1 and self.checkInputs()):
            self.textBox.delete(1.0, tkinter.END)
            if(self.flag == 0):
                self.simpleSearch()
            else:
                self.rangeSearch()
            self.btnExport['state'] = 'normal'
        if(option == 2):
            # cambiar por el texto mostrado en el textBox
            data = pd.read_csv(self.resource_path('./data_red.txt'), sep=';')
            data.to_excel(self.resource_path('./output.xlsx'), 'Sheet1')
        if(option == 3):
            sys.exit()


if __name__ == "__main__":
    Interface()
