import speech_recognition as sr

class ReconocedorVoz:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def reconocer_audio(self):
        with sr.Microphone() as source:
            print("Di algo...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Reconociendo...")
            texto = self.recognizer.recognize_google(audio, language="es-ES")
            texto = texto.lower()
            print(f"Texto reconocido: {texto}")
            return texto
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"Error en la solicitud al servicio de reconocimiento de voz; {e}")
        return None

if __name__ == "__main__":
    reconocedor = ReconocedorVoz()
    texto_reconocido = reconocedor.reconocer_audio()

    if texto_reconocido:
        # Hacer algo con el texto reconocido, por ejemplo, imprimirlo
        print("Texto reconocido fuera de la clase:", texto_reconocido)
