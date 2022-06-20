# Seguimiento de los usuarios que se han conectado días feriados y
# no laborables (sábados y domingos).
# Debe incluir la posibilidad de ingresar un rango de fechas


import tkinter
import os
import sys
import re
import time as tm
from datetime import date as dt
from file_system import File_System
from api import Api
from prettytable import PrettyTable


class Interface(Api, File_System):

    def __init__(self):
        self.file_system = File_System()
        api = Api()
        self.date, self.reason = api.get_data()
        self.weekendsDate = api.get_weekends()
        self.window = tkinter.Tk()
        self.window.config(background="#333333")
        self.window.title("Final Autómatas y Gramáticas")
        self.window.iconbitmap(self.resource_path('./um.ico'))
        self.window.resizable(False, False)
        w = 915
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
                                    width=59,
                                    height=19,
                                    background="#1E1E1E",
                                    font=("Consolas", 20),
                                    yscrollcommand=scroll.set)
        self.textBox.tag_configure("lightblue",
                                   foreground="#11A8CD",
                                   justify='center')
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
        dateTitle.place(x=340, y=10)
        title1.place(x=140, y=70)
        self.calFirst.place(x=250, y=70)
        title2.place(x=510, y=70)
        self.calLast.place(x=615, y=70)
        self.btnFilter.place(x=410, y=135)
        title3.place(x=403, y=185)
        scroll.place(x=893, y=220, height=612)
        self.textBox.place(x=4, y=220)
        self.btnExport.place(x=20, y=845)
        self.registerText.place(x=180, y=854)
        self.filterText.place(x=410, y=854)
        self.errorText.place(x=670, y=854)
        btnExit.place(x=810, y=845)

        # Crea y muestra la interfaz
        self.window.mainloop()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def select_file(self):
        filename, lines = self.file_system.open()
        if(lines):
            self.window.title("Final Autómatas y Gramáticas | Archivo: " +
                              filename)
            self.btnFilter['state'] = 'normal'
            self.lines = lines
        elif(filename != ""):
            self.window.title("Final Autómatas y Gramáticas")
            self.btnFilter['state'] = 'disabled'

    def checkInputs(self):
        REDate = r'(?:3[01]|[12][0-9]|0?[1-9])([-\/])(0?[1-9]|1[0-2])\1\d{4}'
        checkDate = 0
        self.flag = 0
        if(self.calFirst.get() == "" and self.calLast.get() == ""):
            self.calFirst.config(highlightbackground="#519ABA",
                                 highlightcolor="#519ABA")
            self.calLast.config(highlightbackground="#519ABA",
                                highlightcolor="#519ABA")
            return True
        if re.match(REDate, self.calFirst.get()) is None:
            self.calFirst.config(highlightbackground="#cf0909",
                                 highlightcolor="#cf0909")
        else:
            self.calFirst.config(highlightbackground="#85e52e",
                                 highlightcolor="#85e52e")
            checkDate += 1
        if re.match(REDate, self.calLast.get()) is None:
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
        REId = r'([a-z0-9]{16})'
        if re.match(REId, id):
            return True
        return False

    def checkDate(self, date):
        # formato 00/00/0000
        REDate = r'(?:3[01]|[12][0-9]|0?[1-9])([-\/])(0?[1-9]|1[0-2])\1\d{4}'
        if re.match(REDate, date):
            return True
        return False

    def checkTime(self, time):
        # formato 24Hs
        REDate = r'([0-1]?[0-9]|2[0-3])(:)([0-5][0-9])'
        if re.match(REDate, time):
            return True
        return False

    def checkRow(self, line):
        if len(line[0]) > 0 and len(line[1]) > 0 and len(line[2]) > 0:
            return True
        return False

    def checkCols(self, line, date, time):
        if self.checkId(line[0]) and \
           self.checkDate(date) and \
           self.checkTime(time):
            return True
        return False

    def drawValues(self, data):
        if(len(data) > 0):
            table = PrettyTable(['ID', 'Usuario', 'Fecha', 'Hora'])
            for line in data:
                table.add_row([line[0][0], line[0][1], line[1], line[2]])
            resultsBox = table
            self.textBox.insert(tkinter.INSERT,
                                resultsBox,
                                'lightblue')
            self.btnExport['state'] = 'normal'
        else:
            resultsBox = "SIN COINCIDENCIAS"
            self.textBox.insert(tkinter.INSERT,
                                resultsBox,
                                'lightblue')
            self.btnExport['state'] = 'disabled'

    def filter(self):
        if self.calFirst.get() == "":
            self.calFirst.insert(-1, "01/01/2011")
        if self.calLast.get() == "":
            self.calLast.insert(-1, dt.today().strftime("%d/%m/%Y"))
        self.exportData = []
        errors = 0
        filtered = 0
        for index, line in enumerate(self.lines[1:], start=2):
            line = line.split(";")
            if self.checkRow(line):
                date, time = line[2].split(' ')
                if(self.checkCols(line, date, time)):
                    if(date in self.date or date in self.weekendsDate):
                        dateFile = tm.strptime(date, "%d/%m/%Y")
                        First = tm.strptime(self.calFirst.get(),
                                            "%d/%m/%Y")
                        Last = tm.strptime(self.calLast.get(),
                                           "%d/%m/%Y")
                        if(dateFile >= First and dateFile <= Last):
                            try:
                                pos = self.date.index(date)
                                reason = self.reason[pos]
                            except ValueError:
                                reason = '-'
                            self.exportData.append([line, date, time, reason])
                            filtered += 1
                else:
                    errors += 1
            else:
                errors += 1
        self.drawValues(self.exportData)
        self.filterText.config(text=f'Filtrados: {filtered}')
        self.errorText.config(text=f'Errores: {errors}')
        self.registerText.config(text=f'Total: {index-1}')

    def main(self, option):
        if(option == 1 and self.checkInputs()):
            self.textBox.delete(1.0, tkinter.END)
            self.filter()
        if(option == 2):
            name = self.file_system.export(self.exportData)
            if name:
                tkinter.messagebox.showinfo(message="\""+name+"\"" +
                                            " fue guardado exitosamente!",
                                            title="Archivo Guardado!")
        if(option == 3):
            sys.exit()


if __name__ == "__main__":
    Interface()
