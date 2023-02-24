import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile  # get the api


def seperate(v):
    return None, None


fs, data = wavfile.read('recordingX.wav')  # load the data
a = data.T[1:data.size]  # this is a two channel soundtrack, I get the first track
b = [(ele / 2 ** 8.) * 2 - 1 for ele in a]  # this is 8-bit track, b is now normalized on [-1,1)
c = fft(b)  # calculate fourier transform (complex numbers list)
d = len(c)  # you only need half of the fft list (real signal symmetry)

IcI = list(((value.real ** 2 + value.imag ** 2) ** 0.5 for value in c))
# plt.plot(IcI, 'r')
# plt.show()



