from datetime import datetime
from datetime import timedelta

log1 = '\n'

def log(text):
    global log1
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    if (type(text) == str):
        log1 = log1 + f'{fecha}: {text}\n'
    else:
        log1 = log1 + f'{fecha}: {str(text)}\n'
    return log1