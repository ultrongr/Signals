import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

"""A"""
Fs, s = wavfile.read('myvoice.wav')

"""B"""
middle = len(s) // 2
T = round(40 * (10 ** -3) * Fs)
print("Fs = ", Fs)
seg = s[middle:middle + T]
max_seg = max(seg)
norm_seg = [i / max_seg for i in seg]  # normalizing the signal values

fig, axs = plt.subplots(2)
fig.suptitle('Άσκηση 2.4')

"""C"""
axs[0].plot(norm_seg)
axs[0].set_title("Speech signal")
print("\nExtracting F0 from speech signal:")
print("Points:", (837, 0.995), (1251, 0.898))
print("N0 = 1251-837 = 414 samples")
N0 = 414
F0 = Fs / N0
print("F0 = ", F0, "Hz")

"""D"""

auto_correlation = np.correlate(norm_seg, norm_seg, mode="full")
axs[1].plot([len(seg) - n for n in range(len(auto_correlation))], auto_correlation)
axs[1].set_title("Auto-correlation")

"""E"""
print("\nExtracting F0 from auto-correlation:")
print("Points:", (0, 131), (414, 99))
print("N0 = 414 samples")
F0 = Fs / N0
print("F0 = ", F0, "Hz")


print("\n Identical F0 from the two methodologies")
print("115.9Hz belongs in the male frequency range (70-150)")

fig.tight_layout(pad=1.0)
plt.show()
