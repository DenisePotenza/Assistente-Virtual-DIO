import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import os

# Inicializa o motor de fala
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # velocidade da fala
engine.setProperty("volume", 1.0)  # volume máximo

def falar(texto):
    """Transforma texto em fala."""
    engine.say(texto)
    engine.runAndWait()

def ouvir_microfone():
    """Captura o áudio do microfone e transforma em texto."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ouvindo...")
        r.adjust_for_ambient_noise(source)  # ajusta para ruídos do ambiente
        audio = r.listen(source)

    try:
        comando = r.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        falar("Desculpe, não entendi.")
        return ""
    except sr.RequestError:
        falar("Erro ao se conectar ao serviço de reconhecimento de voz.")
        return ""

def executar_comando(comando):
    """Executa ações baseadas no comando de voz."""
    if "wikipedia" in comando:
        falar("O que você deseja pesquisar no Wikipedia?")
        termo = ouvir_microfone()
        if termo:
            try:
                resumo = wikipedia.summary(termo, sentences=2, auto_suggest=True, redirect=True)
                print(resumo)
                falar(resumo)
            except:
                falar("Não consegui encontrar nada no Wikipedia.")

    elif "youtube" in comando:
        falar("Abrindo o YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "farmácia" in comando:
        falar("Procurando a farmácia mais próxima no Google Maps.")
        webbrowser.open("https://www.google.com/maps/search/farmácia+próxima")

    elif "sair" in comando or "encerrar" in comando:
        falar("Até logo!")
        exit()

    else:
        falar("Não reconheci o comando, pode repetir?")

def assistente_virtual():
    falar("Olá, eu sou sua assistente virtual. O que deseja fazer?")
    while True:
        comando = ouvir_microfone()
        if comando:
            executar_comando(comando)

if __name__ == "__main__":
    wikipedia.set_lang("pt")  # Configura Wikipedia em português
    assistente_virtual()
