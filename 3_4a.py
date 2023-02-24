import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile  # get the api

sample_size = 80

fs, data = wavfile.read('recordingX.wav')
T = 1 / fs
signal_data = data.T
fft_data = fft(signal_data, fs)

sample = [i for i in range(sample_size)]

fig, axs = plt.subplots(2)
fig.suptitle('Άσκηση 3.4α ')
axs[0].stem(sample, signal_data[:sample_size], 'r')
axs[1].plot(abs(fft_data), 'b')
plt.subplots_adjust(hspace=0.5)
plt.show()
