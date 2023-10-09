#para esto necesitamos dos librerias que son SpeechRecognition


import speech_recognition as sr
 
r = sr.Recognizer()

with sr.Microphone() as source:

    print("Di algo: ")

    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='es-ES')
    print("Has dicho: " + text)
except:
    print("Lo siento, no te he entendido")