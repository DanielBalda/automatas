# Seguimiento de los usuarios que se han conectado días feriados y
# no laborables (sábados y domingos).
# Debe incluir la posibilidad de ingresar un rango de fechas

from ast import pattern
from tabnanny import check
import tkinter
import os
import sys
import requests
import re

class Interface():

    def __init__(self):
        #self.apiData()
        self.window = tkinter.Tk()
        self.window.config(background="#333333")
        self.window.title("Final Automatas y Gramaticas")
        # PONER ICONO SI QUEREMOS
        # self.window.iconbitmap(self.resource_path('FOLDER/assets/icono.ico'))
        self.window.resizable(False, False)
        self.window.geometry("440x560")

        dateTitle = tkinter.Label(self.window,
                                  text="Busqueda por Fecha:",
                                  font='Helvetica 11 bold',
                                  background="#333333",
                                  fg="#519ABA")
        dateTitle.place(x=150, y=10)

        title1 = tkinter.Label(self.window,
                               text="Desde:",
                               font='Helvetica 11 bold',
                               background="#333333",
                               fg="#519ABA")
        title1.place(x=50, y=45)

        self.calFirst = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      font="Helvetica 10 bold",
                                      highlightthickness=1,
                                      width=10)
        self.calFirst.place(x=110, y=45)

        title2 = tkinter.Label(self.window,
                               text="Hasta:",
                               font='Helvetica 11 bold',
                               background="#333333",
                               fg="#519ABA")
        title2.place(x=220, y=45)

        self.calLast = tkinter.Entry(self.window,
                                     background="#606060",
                                     fg="#FFFFFF",
                                     font="Helvetica 10 bold",
                                     highlightthickness=1,
                                     width=10)
        self.calLast.place(x=275, y=45)

        self.btnFilter = tkinter.Button(self.window,
                                        text=" BUSCAR ",
                                        background="#519ABA",
                                        border=0, fg="#FFFFFF",
                                        font="Helvetica 9 bold",
                                        activebackground='#1E1E1E',
                                        activeforeground='#519ABA',
                                        relief='solid',
                                        command=lambda: self.options(1))

        self.btnFilter.place(x=190, y=80)

        title3 = tkinter.Label(self.window,
                               text="Resultados:",
                               font='Helvetica 11 bold',
                               background="#333333",
                               fg="#519ABA")
        title3.place(x=180, y=115)

        scroll = tkinter.Scrollbar(self.window,
                                   orient='vertical')
        scroll.place(x=418, y=140, height=404)

        self.textBox = tkinter.Text(self.window,
                                    width=51,
                                    height=25,
                                    background="#1E1E1E",
                                    yscrollcommand=scroll.set)
        self.textBox.tag_configure("lightblue", foreground="#11A8CD")
        scroll.config(command=self.textBox.yview)
        self.textBox.place(x=6, y=140)

        # Crea y muestra la interfaz
        self.window.mainloop()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def apiData(self):
        self.fecha = []
        for anio in range(5):
            url = 'http://nolaborables.com.ar/api/v2/feriados/20'+str(anio+18)
            response = requests.get(url)
            if(response.status_code == 200):
                for element in response.json():
                    self.fecha.append(str(element['dia']) +
                                      '/'+str(element['mes']) +
                                      '/20'+str(anio+18))
        return self.fecha

    def checkInputs(self):
        REpattern = r'([0-2][0-9]|3[0-1])(/|-)(0[1-9]|1[0-2])\2(\d{4})'
        checkDate = 0
        if re.match(REpattern, self.calFirst.get()) is None:
            self.calFirst.config(highlightbackground="red",
                                 highlightcolor="red")
        else:
            self.calFirst.config(highlightbackground="green",
                                 highlightcolor="green")
            checkDate += 1
        if re.match(REpattern, self.calLast.get()) is None:
            self.calLast.config(highlightbackground="red",
                                highlightcolor="red")
        else:
            self.calLast.config(highlightbackground="green",
                                highlightcolor="green")
            checkDate += 1
        if(checkDate == 2):
            return True
        else:
            return False

    def options(self, option):
        self.textBox.delete(1.0, tkinter.END)
        if(option == 1 and self.checkInputs()):
            self.textBox.delete(1.0, tkinter.END)
            with open(self.resource_path('./data_red.txt'), 'r') as dataFile:
                lines = dataFile.readlines()
                for index, line in enumerate(lines):
                    if(index != 0):
                        line = line.split(";")
                        resultsBox = "ID: "+line[0] + \
                                     " - Fecha: "+line[2].split(' ')[0] + \
                                     "\n"
                        self.textBox.insert(tkinter.INSERT,
                                            resultsBox,
                                            'lightblue')


if __name__ == "__main__":
    Interface()
