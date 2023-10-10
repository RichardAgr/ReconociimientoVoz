import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, os
from pygame import mixer

name = "Eva"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Se selecciona una voz en español

sites = {
    "google": "google.com",
    "youtube": "youtube.com",
    "facebook": "facebook.com",
    "whatsapp": "web.whatsapp.com",
    "cursos": "freecodecamp.org/learn",
}

files = {
    "reconocimiento de voz": "Reconocimiento de Voz.pdf",
    "sistema de antirobo": "SistemaAntiRobo.pdf",
}


def talk(text):
    engine.say(text)  # La computadora habla
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(
                pc, language="es"
            )  # ayuda a reconocer la voz en español
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, "")
    except:
        pass
    return rec


def run_eva():
    while True:
        rec = listen()
        if "reproduce" in rec:
            music = rec.replace("reproduce", "")
            print("Reproduciendo" + music)
            talk("Reproduciendo" + music)
            pywhatkit.playonyt(music)
        elif "busca" in rec:
            search = rec.replace("busca", "")
            wikipedia.set_lang("es")  # las busquedas realizadas seran en español
            wiki = wikipedia.summary(
                search, 2
            )  # summary resume la informacion el numero indica que tan detallado sera el resumen a mayor numero mayor resumen
            print(search + ": " + wiki)
            talk(wiki)
        elif "alarma" in rec:
            num = rec.replace("alarma", "")
            num = num.strip()
            print(num)
            talk("Alarma activada a las " + num + " horas")
            while True:
                if datetime.datetime.now().strftime("%H:%M") == num:
                    print("DESPIERTA::!!")
                    mixer.init()
                    mixer.music.load("Megumin.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif "abre" in rec:
            for site in sites:
                if site in rec:
                    sub.call(f"start chrome.exe {sites[site]}", shell=True)
                    talk(f"Abriendo {site}")
        elif "archivo" in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True)
                    talk(f"Abriendo {file}")
        elif "escribe" in rec:
            try:
                with open("nota.txt", "a") as f:
                    write(f)
            except FileNotFoundError as e:
                file = open("nota.txt", "w")
                write(file)
        elif "adiós" in rec:
            talk("adiós")
            break


def write(f):
    talk("¿Qué quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Lista, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)


if __name__ == "__main__":
    run_eva()
