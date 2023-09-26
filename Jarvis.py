import pyttsx3
import datetime
import pygame

# Inicializa a engine de texto para fala
texto_fala = pyttsx3.init()

# Inicializa o mixer do pygame
pygame.mixer.init()

def falar(audio):
    # Configurações da voz
    texto_fala.setProperty("rate", 170)  # Alterar a velocidade da fala
    voz = texto_fala.getProperty('voices')[2]  # Seleciona uma voz (ajuste conforme necessário)
    texto_fala.setProperty('voice', voz.id)
    texto_fala.say(audio)
    texto_fala.runAndWait()

def cumprimento():
    hora = datetime.datetime.now().hour
    if 6 <= hora < 12:
        return "bom dia"
    elif 12 <= hora < 18:
        return "boa tarde"
    elif 18 <= hora <= 24:
        return "boa noite"
    else:
        return "boa madrugada"

def bem_vindo():
    falar("Olá J.T., " + cumprimento() + "!")
    agora = datetime.datetime.now()
    falar("Agora são " + agora.strftime("%H:%M") + " horas, do dia " + agora.strftime("%d de %B de %Y"))
    falar("Jarvis está à sua disposição. Como posso te ajudar?")

def reproduzir_musica(musica):
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()

if __name__ == "__main__":
    bem_vindo()

    # Exemplo de reprodução de música
    musica = "caminho/para/sua/musica.mp3"
    reproduzir_musica(musica)
