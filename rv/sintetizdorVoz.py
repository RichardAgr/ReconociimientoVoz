from gtts import gTTS
import pygame
from io import BytesIO

class TextToSpeech:
    def __init__(self):
        pygame.mixer.init()

    def reproducir_audio(self, texto):
        tts = gTTS(text=texto, lang='es')

        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        pygame.mixer.music.load(audio_bytes)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

# Uso
if __name__ == "__main__":
    tts_objeto = TextToSpeech()
    tts_objeto.reproducir_audio("Hola, esto es una prueba de texto a voz.")
