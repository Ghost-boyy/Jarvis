import pyttsx3
import datetime

texto_fala = pyttsx3.init()

def falar(audio):
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate",170)# Alterar a velocidade da fala
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice',voices[2].id)
    texto_fala.say(audio)
    texto_fala.runAndWait()

def tempo():
    Tempo = datetime.datetime.now().strftime("%I:%M")
    falar("Agora são")
    falar(Tempo)
    
def data():
    ano = str(datetime.datetime.now().year)
    mes = str(datetime.datetime.now().month)
    dia = str(datetime.datetime.now().day)
    falar("a data atual é: ")
    falar(dia)
    falar("de" + mes)
    falar("de"+ ano)

def bem_vindo():
    falar("olá jhon oliveira . seja bem vindo de volta!")
    tempo()
    data()
    
    hora = datetime.datetime.now().hour

bem_vindo()