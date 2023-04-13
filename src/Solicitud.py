# Variables para limitar la frecuencia de las solicitudes
requests_count = 0
request_limit = 200
request_interval = 60 # segundos 

#Función para obtener el codigo postal
def codigo_postal(lon, lat):  

    import requests
    import time 
    global requests_count # Se accede a la variable global requests_count
    global last_request_time # Se accede a la variable global last_request_time

    # Se verifica si se ha alcanzado el límite de solicitudes en el intervalo de tiempo
    current_time = time.time()
    if requests_count >= request_limit and current_time - last_request_time < request_interval:
        time.sleep(request_interval - (current_time - last_request_time))
        last_request_time = time.time()
        requests_count = 0

    # Se impporta la libreria request para realizar la solicitud a la API
    
    #Url de la API para para obtener la información detallada del código postal más cercano a las coordenadas de cada fila
    url_API = 'https://api.postcodes.io/postcodes?lon={}&lat={}'  
    # Se comparten los parametros de la longitud y Latitud a la URL 
    url = url_API.format(lon, lat) 
    # Retiramos todos los /n de altos de linea
    url = url.rstrip() 
    #Obtenemos el resultado del request
    data = requests.get(url) 
    # Validamos que el codigo sea 200 lo que significa que es una respuesta exitosa
    if data.status_code == 200:   
        #Convertimos a Json los datos obtenidos con el request
        data = data.json()  
        # Se realiza un try except para las posibles longitudes y latitudes que no encuentren un posible codigo postal
        try:   
            data = data['result'][0]['postcode'] #Si encuentra la longitud y latitud envia el codigo postal
        except TypeError:
            data = None  # Si no la encuentra envia None para despues lograr realizar la 
        requests_count += 1 # Se incrementa el contador de solicitudes
        # Retorna en la variable data el valor del codigo postal o Nan en caso de que no encuentre la ubicación
        return data  
    else:
        # Si el codigo da error envia un None
        return None 