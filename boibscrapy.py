import requests

def boib(anio):
    r = requests.get(f'https://intranet.caib.es/eboibfront/ca/{anio}/') #Desde 02/10/2012
    print(r.content)
boib(2018)

