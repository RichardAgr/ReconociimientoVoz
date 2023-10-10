import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard
from pygame import mixer

name = "Eva"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Se selecciona una voz en español


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
            wiki = wikipedia.summary(search, 2) # summary resume la informacion el numero indica que tan detallado sera el resumen a mayor numero mayor resumen
            print(search + ": " + wiki)
            talk(wiki)
        elif "alarma" in rec:
            num = rec.replace("alarma", '')
            num = num.strip()
            print(num)
            talk("Alarma activada a las " + num + " horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print("DESPIERTA::!!")
                    mixer.init()
                    mixer.music.load("Megumin.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break


if __name__ == "__main__":
    run_eva()
