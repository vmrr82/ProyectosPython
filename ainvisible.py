import random

correos = {'Akanne':'gimenezr.isabel@gmail.com','Patri':'patri@gmail.com','Xisca':'xisca@gmail.com','Meme':'meme@gmail.com','Victor':'vm.rruiz@gmail.com'}


def mix_names():
    correcto = 1
    while correcto == 1:
        lista_adjudicaciones = {}
        listaNombres = ['Akanne','Patri','Xisca','Meme','Victor'] 
        listaAsignaciones = ['Akanne','Patri','Xisca','Meme','Victor']
        mezclador = {}   
        mezclador = dict(zip(listaNombres,random.sample(listaAsignaciones,k=len(listaAsignaciones))))
        for x,k in mezclador.items():
                listaNombres.remove(x)
                listaAsignaciones.remove(k)
                lista_adjudicaciones.update(mezclador)
        
        if lista_adjudicaciones['Victor'] == 'Victor' or lista_adjudicaciones['Akanne'] == 'Akanne' or lista_adjudicaciones['Patri'] == 'Patri' or lista_adjudicaciones['Xisca'] == 'Xisca' or lista_adjudicaciones['Meme'] == 'Meme':
            correcto = 1
            #Bprint("Prueba otra vez ".upper() + str(lista_adjudicaciones))
        else:
            correcto += 1
            print("Proceso finalizado ".upper() + str(lista_adjudicaciones))          
            break    
   
mix_names()










 


#correos = ['vm.rruiz@gmail.com','gimenezr.isabel@gmail.com']
