import requests
from bs4 import BeautifulSoup


class vehiculosRobados:

    def __init__(self,bastidor):
        
        self.bastidor = bastidor

    def rumania(self):
    
        cookies = dict(cookies_are='working')
        r = requests.get(f'https://www.politiaromana.ro/ro/auto-furate?marca=&serie={self.bastidor}&categorie=',cookies=cookies)
        soup = BeautifulSoup(r.text,'html.parser')
        while True:
            try:
                matricula = soup.find("div",{"class":"listBoxLeft3"}).b.text
                marca = soup.find("a",{"class":"listBoxItem"}).text
                print("-----RUMANIA------VEHÍCULO ENCONTRADO-----")
                print("\nBASTIDOR: " + self.bastidor + "\nMARCA: " + marca + "\nMATRICULA: " + matricula)
                
            except (AttributeError,TypeError):
                print("-----RUMANIA------VEHÍCULO NO ENCONTRADO-----")
                break

    def hungria(self):
        cookies = dict(cookies_are='working')
        r = requests.get(f'http://www.police.hu/hu/koral/kozutijarmu-korozesek?ent_jarmu_kozuti_alvazszam={self.bastidor}&ent_jarmu_kozuti_rendszam=&ent_jarmu_kozuti_kore_szerv=All&ent_jarmu_kozuti_kori_szerv=All&ent_jarmu_kozuti_fajta=All&ent_jarmu_kozuti_gyartmany=All&ent_jarmu_kozuti_forgalomba_helyezo_orszag=All&ent_jarmu_kozuti_szin=All',cookies=cookies)
        soup = BeautifulSoup(r.text,'html.parser')
        
        while True:
            try:
                localizado = soup.find("div",{"class":"flex-grid table"}).text.split()
                matricula = localizado[2]
                bastidor = localizado[4]
                tipo_vehiculo = localizado[7]
                marca = localizado[9]
                color = localizado[-1]
                print("-----HUNGRIA------VEHÍCULO ENCONTRADO-----")
                print("\nBASTIDOR: " + self.bastidor + "\nMARCA: " + marca + "\nMATRICULA: " + matricula + "\nCOLOR: " + color)
                break
            except(AttributeError,TypeError):
                print("-----HUNGRIA------VEHÍCULO NO ENCONTRADO-----")
                break
        
#Bastidor RUMANIA ---'WADKJNCKJDSNC'
#Bastidor HUNGRIA ---'TSMMMA53S00189267'      

    
buscar = vehiculosRobados('TSMMMA53S00189267')
buscar.rumania()
buscar.hungria()
