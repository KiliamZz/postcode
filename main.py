# Librerias a usar
import pandas as pd
import requests
import sqlite3
import os
from src.Solicitud import codigo_postal

"""Carga del archivo a un DataFrame
Validamos que el archivo exista y contenga informaciòn
verifica si un archivo CSV existe, si no está vacío y si no 
contiene valores faltantes en las columnas 'lat' y 'lon'. 
Si alguna de estas condiciones no se cumple, el programa 
se detiene y muestra un mensaje de error."""

#Valida que el archivo exista y contenga informaciòn
if os.path.exists('data/postcodesgeo.csv') and os.stat('data/postcodesgeo.csv').st_size != 0:
    coordenadas = pd.read_csv('data/postcodesgeo.csv') # Carga archivo a un DF 
elif os.path.exists('data/postcodesgeo.csv'):
    coordenadas = pd.read_csv('data/postcodesgeo.csv')
    if coordenadas[['lat', 'lon']].isnull().values.any():
        print('El archivo csv contiene filas con valores faltantes en las columnas.')
        exit(1)  # Detener la ejecución del programa 
else:
    print("El archivo no existe o está vacío.")
    exit(1)  # Detener la ejecución del programa    

# Uso de metodo apply de pandas y lambda para invocar la función y enviar los parametros
coordenadas['Cod_Postal'] = coordenadas.apply(lambda row: codigo_postal(row['lon'], row['lat']), axis=1) 

# Identificar las filas que no tienen un código postal
no_cod_postal = coordenadas[coordenadas['Cod_Postal'].isna()]

# Guardar la lista de las coordenas que no tienen un codigo postal en un archivo CSV
no_cod_postal[['lat', 'lon']].to_csv('entregables/coordenadas_sin_codigo_postal.csv', index=False)
#Guardar coordenadas en csv
coordenadas.to_csv('entregables/coordenadas.csv', index=False)
# Conectar con la base de datos
conn = sqlite3.connect('coordenadas.db')

# Crear una tabla en la base de datos con la misma estructura que el DataFrame
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS coordenadas
             (id INTEGER PRIMARY KEY,
              lat REAL,
              lon REAL,
              Cod_Postal TEXT)''')

# Insertar los datos del DataFrame en la tabla
coordenadas.to_sql('coordenadas', conn, if_exists='replace', index=False)
# Cerrar la conexión
conn.close()
