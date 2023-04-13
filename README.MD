**-README**
Este repositorio contiene dos módulos para obtener los códigos postales de una lista de coordenadas y guardar los datos en una base de datos SQLite.

**-Modulo 1: codigo_postal**
La función codigo_postal(lon, lat) recibe dos parámetros, la longitud y latitud de una coordenada, y utiliza la API de https://api.postcodes.io/ para obtener el código postal más cercano a las coordenadas.

# -Uso de la función
Para utilizar esta función, es necesario importarla y pasar los parámetros de la longitud y latitud.

La función devuelve el código postal correspondiente a las coordenadas enviadas. En caso de que no se encuentre un código postal para las coordenadas, la función devuelve None.

**-Modulo 2: main**
Este módulo lee un archivo CSV con coordenadas y utiliza la función codigo_postal para obtener el código postal correspondiente a cada coordenada. Los datos se guardan en una base de datos SQLite y se genera un archivo CSV con las coordenadas que no tienen código postal.

# Requisitos
Para utilizar este módulo, se requiere tener instaladas las siguientes librerías de Python:
    pandas
    requests
    sqlite3

# Uso del módulo:
Para utilizar este módulo, es necesario ejecutar el archivo main.py. El programa leerá el archivo codesgeo.csv ubicado en la carpeta src, que debe contener las columnas lat y lon con las coordenadas.

Si el archivo postcodesgeo.csv existe y contiene datos, el programa generará un nuevo archivo coordenadas_sin_codigo_postal.csv con las coordenadas que no tienen código postal, otro archivo coordenadas.csv con las coordenadas que si tienen codigo postal y creará una base de datos SQLite llamada coordenadas.db con una tabla llamada coordenadas que contendrá los datos de todas las coordenadas, incluyendo el código postal.

En caso de que el archivo postcodesgeo.csv no exista o esté vacío, el programa mostrará un mensaje de error y se detendrá.

Si el archivo postcodesgeo.csv contiene filas con valores faltantes en las columnas lat y lon, el programa mostrará un mensaje de error y se detendrá.

# Para usarlo, deberá ejecutar el siguiente comando en la terminal

python main.py


**Diagrama de arquitectura**

Este diagrama muestra los dos módulos y cómo interactúan entre sí:

lua

              +-----------------+
              |                 |
              |    Modulo 1     |
              |                 |
              +-----------------+
              |  codigo_postal  |
              +-----------------+
              |      pandas     |
              |     requests    |
              +-----------------+
                       ^
                       |
                       |
                       |
+------------------+   |   +------------------+
|                  |   |   |                  |
|     Modulo 2     |---+---|     Archivo CSV   |
|                  |       |                  |
+------------------+       +------------------+
|      pandas      |       |                  |
|     requests     |       |                  |
|    sqlite3       |       |                  |
|       os         |       |                  |
|   codigo_postal  |       |                  |
+------------------+       +------------------+

El módulo 1 define la función codigo_postal que utiliza la librería requests para realizar solicitudes a una API y obtener información detallada del código postal más cercano a las coordenadas de cada fila. El módulo 2 importa la función codigo_postal desde el módulo 1 y la usa junto con la librería pandas para cargar un archivo CSV en un DataFrame. El módulo 2 también utiliza las librerías sqlite3 y os para interactuar con una base de datos SQLite y el sistema de archivos, respectivamente.

El diagrama muestra que ambos módulos utilizan las librerías pandas y requests, y que el módulo 2 también utiliza las librerías sqlite3 y os. El archivo CSV se utiliza como entrada para el módulo 2 y se procesa para obtener los códigos postales correspondientes a cada fila, los cuales se almacenan en una tabla en la base de datos SQLite.

