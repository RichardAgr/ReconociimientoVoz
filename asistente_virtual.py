import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, os
from pygame import mixer

name = "sabina"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices") # obtener la propiedad de voices
engine.setProperty("voice", voices[0].id)  # Se selecciona una voz en español sabina y la de ingles Zira
engine.setProperty('rate', 145)

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
    "imagen":"phyton.png"
}


def talk(text):
    engine.say(text)  # La computadora habla
    engine.runAndWait() # permite que la voz sintetizada funcione de manera sincronica 


def listen():
    try:
        with sr.Microphone() as source: # se configura el microfono para la grabacion de audio
            print("Escuchando...")
            pc = listener.listen(source) # grabar el audio del microfono
            rec = listener.recognize_google(
                pc, language="es"
            )  # transcribe el audio a texto procesable especificando el lenguaje en español
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, "")
    except:
        pass
    return rec


def run_sabina():
    while True:
        rec = listen()
        if "reproduce" in rec:
            music = rec.replace("reproduce", "")
            print("Reproduciendo" + music)
            talk("Reproduciendo" + music)
            pywhatkit.playonyt(music) # abre you tube en el navegador y busca lo que le dijiste
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
                    mixer.music.load("yoasobi.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif "abre" in rec:
            for site in sites:
                if site in rec:
                    sub.call(f"start chrome.exe {sites[site]}", shell=True) #call permite ejecutar comandos y programas desde python
                    talk(f"Abriendo {site}")
        elif "archivo" in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True) # popen funciona de manera similar a call pero lo que hace es abrir archivos con el programa determinado para ese tipo en windows
                    talk(f"Abriendo {file}")
        elif "escribe" in rec:
            try:
                with open("nota.txt", 'a') as f: # abre el archivo y ni no existe lo creara y si existe texto previo lo que hara sera escribir al final del archivo
                    write(f)
            except FileNotFoundError as e:
                file = open("nota.txt", 'w') # el parametro 'w' indica que si existe texto previo este sera eliminado y escribira al principio del archivo 
                write(file)
        elif "adiós" in rec:
            talk("adiós")
            break

def write(f):
    talk("¿Qué quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)


if __name__ == "__main__":
    run_sabina()
