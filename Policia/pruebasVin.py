import requests
from bs4 import BeautifulSoup
import json

def eslovenia(bastidor):
        
        with open('Policia/ukrvoz.json') as file:
                data = json.load(file).values()
                for lista in data:
                    for item in lista:
                        marca = item['znamka']
                        modelo = item['tip']
                        matricula = item['registrska']
                        bastidorCoche = item['sasija']
                        color = item['barva']
                        fecha = item['datumodvzema']
                        if (bastidor in bastidorCoche):
                                try:
                                        print('-----ESLOVENIA------VEHÍCULO ENCONTRADO-----')
                                        print("\nBASTIDOR: " + bastidor + "\nMARCA: " + marca + "\nMATRICULA: " + matricula + "\nCOLOR: " + color + "\nFECHA: " + fecha)

                                        break
                                except(KeyError()):
                                        print("-----ESLOVENIA------VEHÍCULO NO ENCONTRADO-----")
                                        break

                        
        
        
        
                
        
eslovenia('ZZ1A8GBAP00842109')

