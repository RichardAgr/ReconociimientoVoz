import numpy as np
import scipy.io.wavfile as waves
import librosa
import librosa.display
import numpy as np

# obtener informacion del audio
def get_audio_data(filename):
    sample_rate, sound = waves.read(filename)
    length = np.shape(sound)
    return (sample_rate, sound, length)

# Eliminacion de ruido
def get_audio_signal_bounded(filename):
    sound, sample_rate = librosa.load(filename, sr=None)
    energy_threshold = 0.005 
    energy = librosa.feature.rms(y=sound)[0]
    voice_index = np.where(energy > energy_threshold)
    sound_trimmed = sound[voice_index]
    return sound_trimmed

# Normalizar la senal
def normalize(sound_trimmed):
    sound_nomalized = librosa.util.normalize(sound_trimmed)
    return sound_nomalized

# Extraccion de los coeficientes LPC
def get_lpc_coefficients(sound, order):
    lpc_coefficients = librosa.lpc(order=order, y=sound)
    return lpc_coefficients
