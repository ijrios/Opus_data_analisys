from zipfile import ZipFile
import pandas as pd
import requests

url_stream = 'https://www.bl.uk/bibliographic/downloads/NationalParksResearcherFormat_202112_csv.zip'
my_stream_file = requests.get(url_stream, stream=True)
path = 'datos.zip'

with open(path, 'wb') as f:
    for ch in my_stream_file:
        f.write(ch)

with ZipFile('datos.zip', 'r') as zip:
    zip.extractall('datos')
    
datos = pd.read_csv('datos/topics.csv')
datos.head(10)

Topics = pd.pivot_table(datos,columns=['Topic'], aggfunc='size')
ordenado = dups_topics.sort_values(ascending = False).sort_values(ascending = False)

Tabla = pd.DataFrame()
Tabla['Nombre'] = ordenado.index
Tabla['Repeticiones'] = ordenado.values
Tabla.head()

