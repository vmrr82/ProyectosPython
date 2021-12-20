import requests
from bs4 import BeautifulSoup
from time import sleep

class vehiculosRobados:

    def __init__(self,bastidor):
        
        self.bastidor = bastidor

    def rumania(self):
    
        cookies = dict(cookies_are='working')
        r = requests.get(f'https://www.politiaromana.ro/ro/auto-furate?marca=&serie={self.bastidor}&categorie=',cookies=cookies)
        soup = BeautifulSoup(r.text,'html.parser')
        matricula = soup.find("div",{"class":"listBoxLeft3"}).b.text
        marca = soup.find("a",{"class":"listBoxItem"}).text
        print("-----VEHÍCULO ENCONTRADO EN RUMANIA-----")
        print("\nBASTIDOR: " + self.bastidor + "\nMARCA: " + marca + "\nMATRICULA: " + matricula)
        
    
buscar = vehiculosRobados('WAUZZZ8E35A437815')
buscar.rumania()
