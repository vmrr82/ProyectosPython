import logging
from tokenApi import tokenApi
import pandas as pd
import telegram
from telegram.ext import CallbackContext, CommandHandler, Updater, ConversationHandler, MessageHandler, Filters


INPUT_TEXT = 0

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO) #Función rescata errores


def start(update: Updater, context: CallbackContext):
    start_text = "Bienvenido al Codificado de Tráfico NO OFICIAL de la DGT.\nEstos son los comandos disponibles: \n\n/help - Ayuda. \n/consulta - búsqueda de definiciones.\n/contacto - Contacto con administrador del bot.\n\nEsto es un proyecto puramente altruista, no se recopila ningún tipo de datos de los usuarios.\nEl código fuente está disponible en GitHub para quien le interese."
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text) #Mensaje /Start

def help(update:Updater,context: CallbackContext): 
    help_text = "Para usar este buscador realiza la siguiente búsqueda.\nEj.: /consulta cinturón.\nDe momento el bot sólo devuelve un máximo de 10 resultados.\nIntente introducir búsquedas concretas.\nPara cada consulta deberá introducir el comando /consulta.\nMuchas gracias."
    context.bot.send_message(chat_id= update.effective_chat.id,text=help_text) #Mensaje /help

def contacto(update: Updater, context: CallbackContext):
    contacto_text = "Si quiere hacer alguna consulta o encuentra algún fallo en el bot, por favor diríjase al administrador, @Dash56_3"
    context.bot.send_message(chat_id=update.effective_chat.id, text=contacto_text) #Mensaje /contacto

def consulta(update,context):
    update.message.reply_text('Introduce la consulta, por favor')

    return INPUT_TEXT
    
def buscarInfraccion(update: Updater,context: CallbackContext): #Funcion /consulta

    df = pd.read_csv('botTelegram/files/Codificado-DGT-3-de-septiembre-de-2021.csv',delimiter=',',encoding='utf-8').fillna(value=0)
    
    consultaUsuario = update.message.text
    buscarInfraccion = df.loc[df.INFRACCION.str.contains(consultaUsuario,case=False,na=False)].to_dict(orient='index')
    infraccionesKeys = []
    for x in buscarInfraccion.keys():
        infraccionesKeys.append(x)
    
    descripInfraccion = iter(list(map(lambda x: "<b>NORMA</b> = " + str(x['NORMA']) +"\n" \
                                                        "<b>ART</b> = " + str(x['ART']) +"\n"\
                                                        "<b>APT</b> = " + str(x['APT']) + "\n"\
                                                        "<b>OPC</b> = " + str(x['OPC']) + "\n"\
                                                        "<b>PTOS</b> = " + str(x['PTOS']) + "\n"\
                                                        "<b>CALIF</b> = " + str(x['CALIF']) + "\n"\
                                                        "<b>INFRACCION</b> = " + str(x['INFRACCION']) + "\n"\
                                                        "<b>MULTA</b> = " + str(x['MULTA']) + "\n"\
                                                        "<b>RESPONS</b> = " + str(x['RESPONS']) + "\n"\
                                                        "<b>COMENTARIO</b> = " + str(x['COMENTARIO']),buscarInfraccion.values())))
    contadorClaves = 1
    if buscarInfraccion:
        if len(buscarInfraccion) > 10:
            context.bot.send_message(text=f"La búsqueda que has solicitado devuelve más de 10 resultados. Introduce otro término para realizar la búsqueda, por favor.", chat_id =update.effective_chat.id )
        else:
            for i in infraccionesKeys:
                update.message.reply_text(text=next(descripInfraccion),parse_mode ='html')
                
                context.bot.send_message(text=f"Resultado nº {contadorClaves} de {len(buscarInfraccion)}.", chat_id =update.effective_chat.id )
                contadorClaves +=1
            print(len(buscarInfraccion)) 
    else:
        context.bot.send_message(text="Consulta no encontrada, inténtelo de nuevo. ",chat_id = update.effective_chat.id)              
    print(consultaUsuario)
  
    return ConversationHandler.END

def main():

    updater = Updater(token=tokenApi,use_context= True) #Actualizaciones
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help',help))
    dispatcher.add_handler(CommandHandler('contacto',contacto))
    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('consulta',consulta)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, buscarInfraccion)]
        },
        fallbacks=[]
    ))
    
    
    updater.start_polling() #Inicia Bot
    updater.idle()

if __name__ == "__main__":
    bot = telegram.Bot(token=tokenApi)
    print(bot.getMe())
    main()
    
    