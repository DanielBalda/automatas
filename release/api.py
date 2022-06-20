
import requests
from datetime import date
import pandas as pd


class Api():
    def __init__(self):
        self.dataApi = []
        self.reason = []
        self.dataPd = []

    def get_data(self):
        for anio in range(2011, date.today().year+1):
            url = 'http://nolaborables.com.ar/api/v2/feriados/'+str(anio)
            response = requests.get(url)
            if(response.status_code == 200):
                for element in response.json():
                    self.dataApi.append(f'{element["dia"]:02d}/' +
                                        f'{element["mes"]:02d}/' +
                                        str(anio))
                    self.reason.append(element["motivo"])
            else:
                print("Error al obtener los datos")
                # Aca deberiamos tener un archivo con los feriados
                # en caso de que la API no responda
                # o tener una exepcion ante el error y reintentar unas 3 veces
                pass
        return self.dataApi, self.reason

    def get_weekends(self):
        zone = 'America/Argentina/Buenos_Aires'
        self.dataPd = pd.bdate_range(start=str(2011),
                                     end=str(date.today().year+1),
                                     freq="C",
                                     weekmask="Sat Sun",
                                     tz=zone).strftime('%d/%m/%Y').tolist()
        return self.dataPd
