from typing_extensions import Annotated
import pyttsx3
import datetime
texto_fala = pyttsx3.init()

def falar(audio):
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate",170)# Alterar a velocidade da fala
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice',voices[0].id)
    texto_fala.say(audio)
    texto_fala.runAndWait()

def tempo():
    Tempo = texto_fala.getProperty("%I:%M")
    
    falar(Tempo)
    

def data():
    ano = str(datetime.datetime.now().year)
    mes = str(datetime.datetime.now().month)
    dia = str(datetime.datetime.now().day)
    falar("a data atual é: ")
    falar(dia)