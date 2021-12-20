import requests
from bs4 import BeautifulSoup

def hungria(bastidor):
        cookies = dict(cookies_are='working')
        r = requests.get(f'http://www.police.hu/hu/koral/kozutijarmu-korozesek?ent_jarmu_kozuti_alvazszam={bastidor}&ent_jarmu_kozuti_rendszam=&ent_jarmu_kozuti_kore_szerv=All&ent_jarmu_kozuti_kori_szerv=All&ent_jarmu_kozuti_fajta=All&ent_jarmu_kozuti_gyartmany=All&ent_jarmu_kozuti_forgalomba_helyezo_orszag=All&ent_jarmu_kozuti_szin=All',cookies=cookies)
        soup = BeautifulSoup(r.text,'html.parser')
        valores = []
        localizado = soup.find("div",{"class":"flex-grid table"}).text.split()
        matricula = localizado[2]
        bastidor = localizado[4]
        tipo_vehiculo = localizado[7]
        marca = localizado[9]
        color = localizado[-1]
        print(matricula)
        
        
        
                
        
hungria('TSMMMA53S00189267')

