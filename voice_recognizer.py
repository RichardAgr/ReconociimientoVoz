# %%
# Abrir un archivo de audio .wav
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

# INGRESO
# filename = 'output.wav'
# filename = 'zoologico-1.wav'
# filename = 'zoologico-2.wav'
# filename = 'zoologico-3.wav'
filename = 'zoologico-4.wav'
sample_rate, sound = waves.read(filename)

# %%
sample_rate # velocidad de muestreo Hz

# %%
sound

# %%
length = np.shape(sound)
channels = len(length)

# %%
length

# %%
channels

# %%
type_audio = 'stereo'

if channels < 2:
    type_audio = 'monophonic'

duration = len(sound) / sample_rate

# %%
duration

# %%
plt.plot(sound)
plt.show()

# %%
# Acotamiento de la senal

import librosa
import librosa.display
# import matplotlib.pyplot as plt
# import numpy as np

y, sample_rate = librosa.load(filename, sr=None)

# %%
y

# %%
sample_rate

# %%
energy_threshold = 0.005

energy = librosa.feature.rms(y=y)[0]

# %%
energy

# %%
voice_index = np.where(energy > energy_threshold)

# %%
voice_index

# %%
y_trimmed = y[voice_index]

# %%
y_trimmed

# %%
plt.plot(y_trimmed)
plt.show()

# %%
import pywt
import numpy as np

wavelet = 'db4' # Daubechies - 4 coeficentes
coefficients = pywt.wavedec(y_trimmed, wavelet=wavelet)

# %%
coefficients

# %%
for i in range(1, len(coefficients) + 1):
    plt.subplot(len(coefficients), 1, i)
    plt.plot(coefficients[i - 1])

plt.show()

# %%
y_normalized = librosa.util.normalize(y_trimmed)

# %%
y_normalized

# %%
plt.plot(y_normalized)
plt.show()

# %%
order = 25
lpc_coefficients = librosa.lpc(order=order, y=y_normalized)

# %%
lpc_coefficients

# %%
plt.plot(lpc_coefficients)
plt.xlabel('Numero de coeficientes')
plt.ylabel('Valor')
plt.grid(True)
plt.show()


