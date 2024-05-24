#%%

# se importan las librerías necesarias
import requests
from bs4 import BeautifulSoup
import pandas as pd



# se crean listas vacías para almacenar los datos
restaurants = []
link = []
address = []
contact = []
rating = []
city = []

# aquí se ingresan las url, restaurante por restaurante
url_other_data = []


# aquí se ingresan las url de los restaurantes
url_retsaurants = []

# direccion de tu archivo txt
path = "C:/Users/heber/OneDrive/Documentos/restaurantes_zonas.txt"

# parámetros función other_data
# param = etiqueta html y param0 = clase
param = 'a'
param0 = 'list-rst__name-main js-detail-anchor'

# parámetros función restaurants_name
# param1 = etiqueta html y param2 = clase
param1 = 'a'
param2 = 'list-rst__name-main js-detail-anchor'

# parámetros función restaurant_address
# param3 = etiqueta html y param4 = clase
param3 = 'p'
param4 = 'rd-detail-info__rst-address'

# parámetros función restaurant_contact
# param5 = etiqueta html y param6 = clase
param5 = 'p'
param6 = 'rd-detail-info__rst-tel'

# parámetros función restaurants_rating
# param7 = etiqueta html y param8 = clase
param7 = 'b'
param8 = 'c-rating__val c-rating__val--strong'

# parámetros función restaurants_rating
# param7 = etiqueta html y param8 = clase
param9 = 'a'
param10 = 'rd-header__linktree-parent-target gly-a-arrowdown'

# la siguiente funcion obtiene la informacion de tu archivo txt
# variable datos es una lista que almacena los datos del archivo
datos = []
def text(ruta_archivo):
    archivo = open(ruta_archivo, "r")
    for line in archivo:
        for word in line.split(','):
            datos.append(word)
    archivo.close()

# la siguiente función depura los datos obtenidos del archivo txt
def clean(data):
    for i in data:
        if i.startswith("https"):
            url_retsaurants.append(i)

# la siguiente función obtiene los nombres de los restaurantes de las url de yelp que se ingresen
def restaurants_name (url, label, class_):
    for i in url:
        res = requests.get (i)
        soup = BeautifulSoup (res.text, 'html.parser')
        
        # este ciclo for busca los nombres de los restaurantes en la url y los agrega a la lista restaurantes         
        for element in soup.find_all (label, class_ ):
            
            # si no se encuentra un dato se arrojará 'No encontrado'
            if element:
                restaurants.append (element.text.strip())
            else:
                restaurants.append ('No encontrado')

# función para obtener la dirección de los restaurantes para url_other_data
def other_data (url, label, class_):
    for i in url:
        res = requests.get (i)
        soup = BeautifulSoup (res.text, 'html.parser')
        url_1 = soup.find_all (label, class_)
        
        for i in url_1:
            url_other_data.append(i['href'])

# la siguiente función obtiene el link de los restaurantes en yelp
def restaurant_link (url):
    for i in url:
        link.append (i)

# la siguiente función obtiene las direcciones de los resaurantes
def restaurant_address (url, label, class_):
    for i in url:
        res = requests.get (i)
        soup = BeautifulSoup (res.text, 'html.parser')
        adress1 = soup.find (label, class_)
        address.append (adress1.text.strip())

# la siguiente función obtiene el contacto de los restaurantes registrado en la página
def restaurant_contact (url, label, class_):
    for i in url:
        res = requests.get (i)
        soup = BeautifulSoup (res.text, 'html.parser')
        contact1 = soup.find (label, class_)
        if contact1 is not None: 
            first_part = contact1.text.strip().split('\n')[0]
            contact.append(first_part)
        else:
            contact.append(None)

# la siguiente función obtiene las valoraciones de los restaurantes       
def restaurant_rating (url, label, class_):
    for i in url:
        res = requests.get (i)
        soup = BeautifulSoup (res.text, 'html.parser')
        rating1 = soup.find (label, class_)
        if rating1 is not None: 
            rating.append (rating1.text.strip())
        else:
            contact.append(None)

# la siguiente función obtiene las valoraciones de las ciudades       
def restaurant_city (url, label, class_):
    for i in url:
        res = requests.get (i)
        soup = BeautifulSoup (res.text, 'html.parser')
        city1 = soup.find (label, class_)
        if city1 is not None: 
            city.append (city1.text.strip())
        else:
            contact.append(None)

# llamar a las funciones
text (path)
clean (datos)
restaurants_name (url_retsaurants, param1, param2)
other_data (url_retsaurants, param, param0)
restaurant_link (url_other_data)
restaurant_address (url_other_data, param3, param4)
restaurant_contact (url_other_data, param5, param6)
restaurant_rating (url_other_data, param7, param8)
restaurant_city (url_other_data, param9, param10)

# se crea un dataframe con los datos obtenidos
df = pd.DataFrame({
    'Restaurantes': restaurants,
    'Direccion': address,
    'Link': link,
    'Contacto' : contact,
    'Rating' : rating,
    'Ciudad' : city
})

# se imprime el dataframe
print (df)

# se exporta el dataframe a un archivo csv
#df.to_csv('yelp_mexican_restaurants.csv', index=False, path_or_buf='donde se guarda')

# %%
