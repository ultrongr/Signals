import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile  # get the api

sample_size = 80
multiplier = 4

fs, data = wavfile.read('recordingX.wav')
fs = int(fs / multiplier)
T = 1 / fs
signal_data = data.T[::multiplier]
fft_data = fft(signal_data, fs)

sample = [i for i in range(int(sample_size/multiplier))]

fig, axs = plt.subplots(2)
fig.suptitle('Άσκηση 3.4γ ')
axs[0].stem(sample, signal_data[:int(sample_size/multiplier)], 'r')
axs[1].plot(abs(fft_data), 'b')
plt.subplots_adjust(hspace=0.5)
plt.show()
