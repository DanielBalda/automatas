# Seguimiento de los usuarios que se han conectado días feriados y
# no laborables (sábados y domingos).
# Debe incluir la posibilidad de ingresar un rango de fechas

import tkinter
from tkcalendar import DateEntry
from datetime import date
import os
import sys


class Interface():

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(background="#333333")
        self.window.title("Final Automatas y Gramaticas")
        # PONER ICONO SI QUEREMOS
        # self.window.iconbitmap(self.resource_path('FOLDER/assets/icono.ico'))
        self.window.resizable(False, False)
        self.window.geometry("440x560")
        dateTime = str(date.today()).split("-")

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

        cal = DateEntry(self.window,
                        width=10,
                        bg="darkblue",
                        fg="white",
                        day=int(dateTime[0]),
                        month=int(dateTime[1]),
                        year=int(dateTime[2]))
        cal.place(x=110, y=45)

        title2 = tkinter.Label(self.window,
                               text="Hasta:",
                               font='Helvetica 11 bold',
                               background="#333333",
                               fg="#519ABA")
        title2.place(x=220, y=45)

        cal = DateEntry(self.window,
                        width=10,
                        bg="darkblue",
                        fg="white",
                        day=int(dateTime[0]),
                        month=int(dateTime[1]),
                        year=int(dateTime[2]))
        cal.place(x=275, y=45)

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

        textTmp = ("TEST")
        self.textBox.delete(1.0, tkinter.END)
        self.textBox.insert(tkinter.INSERT, textTmp, 'lightblue')

        # Crea y muestra la interfaz
        self.window.mainloop()

    def options(self, option):
        if(option == 1):
            self.textBox.delete(1.0, tkinter.END)
            with open(self.resource_path('./data_red.txt'), 'r') as dataFile:
                lines = dataFile.readlines()
                for index, line in enumerate(lines):
                    if(index != 0):
                        line = line.split(";")
                        resultsBox = "ID: "+line[0] + \
                                     " - Fecha: "+line[2] + \
                                     "\n"
                        self.textBox.insert(tkinter.INSERT, resultsBox, 'lightblue')


if __name__ == "__main__":
    Interface()
