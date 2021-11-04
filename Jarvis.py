import pyttsx3

texto_fala = pyttsx3.init()

def falar(audio):
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate",170)
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice',voices[0].id)
    texto_fala.say(audio)
    texto_fala.runAndWait()

falar("olá a todos. o meu nome é Live.")

