import requests
from datetime import *


def sign_attendance_sheet(materia):
    
    URL = ""
    
    data = {
    "entry.2136258989":     "",  # Nome   
    "entry.444597552":      0000,       # Número 
    "entry.337721011":      materia,
    "entry.1762880222":     000,        # turma
    "entry.121857887":      "",        # intinerario (A ou B)
    "emailAddress":         "" # email
    }
    
    if requests.post(url=URL, data=data).status_code == 200:
        return "Sua presenca na aula de {} foi marcada com sucesso ".format(materia)
    else:
        return "algo deu errado durante a requisicao"


def current_weekday():
    today = datetime.today().weekday();
    return today; 


def current_time(): 
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    return current_time


def start_signing(classes_time, subjects):
    classes = []
    for x in range(len(subjects)):
        classes.append({"time": classes_time[x], "subject": subjects[x]})
        print(classes[x])
        
    i = 0
    while i <= len(subjects) - 1:
        while current_time() == classes[i]["time"]:
            response = sign_attendance_sheet(classes[i]["subject"])
            i += 1 
            print(response, current_time(), i)
            break
        