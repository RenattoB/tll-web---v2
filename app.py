from flask import Flask, request, Response
import requests
import json 
from datetime import datetime
import threading
from log import *
from wavyFunctions import *

app = Flask(__name__)

#Notificación de mensaje
@app.route('/web-hook/conversations/<tokenId>/message', methods = ['POST'])
def messages(tokenId):
    fechaInicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log(f'***Se llamo al notification event de mensaje***\n')
    if 'application/json' in request.headers['content-type']:        
        thread = threading.Thread(target = wavySendJson, args = (request.json,))
        thread.start()
        return Response(status = 200)
    else:
        return Response(status = 526)

#Notificacion de conversacion creada
@app.route('/web-hook/conversations/<tokenId>/create', methods = ['POST'])
def createConversation(tokenId):
    fechaInicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log(f'***Se llamo al notification event de conversación creada***\n')
    if 'application/json' in request.headers['content-type']:
        thread = threading.Thread(target = mensajeria, args = ('Notificacion de conversación creada', tokenId, request.json,fechaInicio,))
        thread.start()
        return Response(status = 200)
    else:
        return Response(status = 526)   

#Notificacion de conversacion terminada
@app.route('/web-hook/conversations/<tokenId>/terminate', methods = ['POST'])
def terminateConversation(tokenId):
    fechaInicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log(f'***Se llamo al notification event de conversación creada***\n')
    if 'application/json' in request.headers['content-type']:
        thread = threading.Thread(target = mensajeria, args = ('Notificacion de conversación terminada', tokenId, request.json,fechaInicio,))
        thread.start()
        return Response(status = 200)
    else:
        return Response(status = 526)   

#Notificacion de conversación aceptada
@app.route('/web-hook/conversations/<tokenId>/accept', methods = ['PUT'])
def conversationAccepted(tokenId):
    fechaInicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log(f'***Se llamo al notification event de conversación aceptada***\n')
    if 'application/json' in request.headers['content-type']:
        thread = threading.Thread(target = mensajeria, args = ('Notificacion de conversación aceptada', tokenId, request.json,fechaInicio,))
        thread.start()
        return Response(status = 200)
    else:
        return Response(status = 526)

#Notificacion de conversación aceptada
@app.route('/web-hook/conversations/<tokenId>/typing', methods = ['PUT'])
def agentTyping(tokenId):
    fechaInicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log(f'***Se llamo al notification event de typing***\n')
    if 'application/json' in request.headers['content-type']:
        thread = threading.Thread(target = mensajeria, args = ('Notificacion de tipeo', tokenId, request.json,fechaInicio,))
        thread.start()
        return Response(status = 200)
    else:
        return Response(status = 526)

def mensajeria(notification, tokenId, data, fechaInicio):
    fechaFin = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    url = 'https://api-messaging.wavy.global/v1/whatsapp/send'
    urlHeaders = {'Content-type': 'application/json','UserName': 'wa_telectronicperusac_pe','AuthenticationToken': 'nouxAVNgqztEWAgVyYfj1qI2i8g-DToSty6bGz1P'}
    json_p = {"destinations": [{"destination": "51995736457"}],"message": {"messageText": f"Se invoco el webhook a las: {fechaInicio}\nSe termino en: {fechaFin}\nNotificacion: {notification}\nToken{tokenId}\n JSON: {data}"}}
    json_r = {"destinations": [{"destination": "51912738120"}],"message": {"messageText": f"Se invoco el webhook a las: {fechaInicio}\nSe termino en: {fechaFin}\nNotificacion: {notification}\nToken{tokenId}\n JSON: {data}"}}

    response_p = requests.post(url,data = json.dumps(json_p), headers = urlHeaders)
    response_r = requests.post(url,data = json.dumps(json_r), headers = urlHeaders)
    print(log('*Evento finalizado*\n'))



if __name__ == '__main__':
    app.run()