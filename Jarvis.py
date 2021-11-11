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
    tempo(Tempo)