import random

correos = {'Akanne':'akanne@gmail.com','Antonio':'antonio@gmail.com','Pedro':'pedro@gmail.com'}


def mix_names():
    correcto = 1
    while correcto == 1:
        lista_adjudicaciones = {}
        listaNombres = ['Akanne','Antonio','Pedro'] 
        listaAsignaciones = ['Akanne','Antonio','Pedro']
        mezclador = {}   
        mezclador = dict(zip(listaNombres,random.sample(listaAsignaciones,k=len(listaAsignaciones))))
        for x,k in mezclador.items():
                listaNombres.remove(x)
                listaAsignaciones.remove(k)
                lista_adjudicaciones.update(mezclador)
        
        if lista_adjudicaciones['Antonio'] == 'Antonio' or lista_adjudicaciones['Akanne'] == 'Akanne' or lista_adjudicaciones['Pedro'] == 'Pedro':
            correcto = 1
            #Bprint("Prueba otra vez ".upper() + str(lista_adjudicaciones))
        else:
            correcto += 1
            print("Proceso finalizado ".upper() + str(lista_adjudicaciones))          
            break    
   
mix_names()










 


#correos = ['vm.rruiz@gmail.com','gimenezr.isabel@gmail.com']
