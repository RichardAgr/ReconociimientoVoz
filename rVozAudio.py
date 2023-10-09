import os
import speech_recognition as sr
import ffmpeg

input_file = "audio.mp3"
output_file = "temp.wav"

# Convertir el archivo MP3 a WAV utilizando ffmpeg-python
ffmpeg.input(input_file).output(output_file).run()

r = sr.Recognizer()

with sr.AudioFile(output_file) as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio, language='es-ES')
    print("El texto generado para el archivo es:\n" + text)
except sr.UnknownValueError:
    print("Lo siento, no se pudo reconocer la voz del archivo")
except sr.RequestError as e:
    print("Error en la solicitud: {0}".format(e))

# Eliminar el archivo temporal WAV
os.remove(output_file)