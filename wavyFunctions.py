import requests
from log import *
import json

def wavySendMessage(data):    
    log('***Invocando API send message de wavy***\n')
    url = 'https://api-messaging.wavy.global/v1/whatsapp/send'
    urlHeaders = {'Content-type': 'application/json','UserName': 'wa_telectronicperusac_pe','AuthenticationToken': 'nouxAVNgqztEWAgVyYfj1qI2i8g-DToSty6bGz1P'}
    response = requests.post(url, json.dumps(data), headers = urlHeaders)
    log(f'Json devuelto: {response.json()}')
    print(log('*Evento finalizado*\n'))


def wavySendJson(data):
    log('***Preparando JSON para wavy***\n')
    number = data['externalId']
    message = data ['text']
    correlationId = data['messageId']
    
    cjson =  {
            "destinations": [{
                "correlationId": f"{correlationId}",
                "destination": f"{number}"
            }],
            "message": {
                "messageText": f"{message}"
            }
        }
    log(f'Json a enviar: {cjson}\n')    
    wavySendMessage(cjson)

