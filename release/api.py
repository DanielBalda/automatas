
import requests
from datetime import date
import pandas as pd


class Api():
    def __init__(self):
        self.dataApi = []
        self.reason = []
        self.dataPd = []
        self.startYear = 2011

    def get_data(self):
        count = 0
        for anio in range(self.startYear, date.today().year+1):
            url = 'http://nolaborables.com.ar/api/v22/feriados/'+str(anio)
            response = requests.get(url)
            if(response.status_code == 200):
                for element in response.json():
                    self.dataApi.append(f'{element["dia"]:02d}/' +
                                        f'{element["mes"]:02d}/' +
                                        str(anio))
                    self.reason.append(element["motivo"])
                count += 1
        if(count == date.today().year+1 - self.startYear):
            with open("feriados.txt", "w", encoding="utf-8") as file:
                for i in range(len(self.dataApi)):
                    file.write(f'{self.dataApi[i]}\t{self.reason[i]}\n')
        else:
            try:
                with open("feriados.txt", "r", encoding="utf-8") as file:
                    for line in file:
                        self.dataApi.append(line.split('\t')[0])
                        self.reason.append(line.split('\t')[1])
            except Exception:
                print("No se pudo leer el archivo")
        return self.dataApi, self.reason

    def get_weekends(self):
        zone = 'America/Argentina/Buenos_Aires'
        self.dataPd = pd.bdate_range(start=str(self.startYear),
                                     end=str(date.today().year+1),
                                     freq="C",
                                     weekmask="Sat Sun",
                                     tz=zone).strftime('%d/%m/%Y').tolist()
        return self.dataPd
