import matplotlib.pyplot as plt
import numpy as np

signal_in = [1, -2, 2, -1]
N = len(signal_in)


def DFT(x):
    out = [0. + 0.j for _ in range(N)]
    for k in range(N):
        for n in range(N):
            out[k] += x[n] * np.e ** (-k * n * 2 * np.pi * 1.j / N)
    return out


def get_magnitude(x):
    return [np.sqrt(np.real(z) ** 2 + np.imag(z) ** 2) for z in x]


def get_phase(x):
    return [np.arctan(np.imag(z) / np.real(z)) if np.real(z) != 0 else np.pi / 2 for z in x]


X = DFT(signal_in)
# for i in X:
#     print(i)
# print(get_magnitude(X))
# print(get_phase(X))

fig, axs = plt.subplots(3)
fig.suptitle('Άσκηση 2.2 A.b)')
axs[0].stem(range(0, N), signal_in, )
axs[0].set_title("In", x=-0.1, y=0)
axs[1].stem(range(0, N), get_magnitude(X), )
axs[1].set_title("Magn", x=-0.1, y=0.2)
axs[2].stem(range(0, N), get_phase(X), )
axs[2].set_title("Phase", x=-0.1, y=0.2)

fig.tight_layout(pad=2)
plt.show()
