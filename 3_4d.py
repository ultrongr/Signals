import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile

sample_size = 80

fs, data = wavfile.read('recordingX.wav')
T = 1 / fs
signal_data = data.T


def calculate_y(n):
    return b0 * x_dict[n] + b1 * x_dict[n - 1] + b2 * x_dict[n - 2] + a1 * y_dict[n - 1] + a2 * y_dict[n - 2]


b0 = 1
b1 = -1.9999
b2 = 1
a1 = 1.8999
a2 = -0.9025

y = []
x = []
y_dict = {-2: 0, -1: 0}
x_dict = {-2: 0, -1: 0}

for i in range(len(signal_data)):
    x_dict[i] = signal_data[i]
    x.append(signal_data[i])

for i in range(len(signal_data)):
    y_dict[i] = calculate_y(i)
    y.append(y_dict[i])

y_fft_data = fft(y, fs)
x_fft_data = fft(x, fs)
sample = [i for i in range(sample_size)]

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Άσκηση 3.4δ ')
axs[0][0].stem(sample, x[:sample_size], 'r')
axs[0][0].set_title("x")
axs[0][1].plot(abs(x_fft_data), 'b')
axs[0][0].set_title("FFT(x)")
axs[1][0].stem(sample, y[:sample_size], 'r')
axs[1][0].set_title("y")
axs[1][1].plot(abs(y_fft_data), 'b')
axs[1][1].set_title("FFT(y)")
plt.subplots_adjust(hspace=0.5)
plt.show()

# fig, axs = plt.subplots(2, 2)
# axs[0, 0].plot(x, y)
# axs[0, 0].set_title('Axis [0, 0]')
# axs[0, 1].plot(x, y, 'tab:orange')
# axs[0, 1].set_title('Axis [0, 1]')
# axs[1, 0].plot(x, -y, 'tab:green')
# axs[1, 0].set_title('Axis [1, 0]')
# axs[1, 1].plot(x, -y, 'tab:red')
# axs[1, 1].set_title('Axis [1, 1]')
#
# for ax in axs.flat:
#     ax.set(xlabel='x-label', ylabel='y-label')
#
# # Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()
