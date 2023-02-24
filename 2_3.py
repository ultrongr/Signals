import matplotlib.pyplot as plt
import numpy as np

W1 = 125 * np.pi
W2 = 325 * np.pi
Fs = 1000
T = 1 / Fs
L = 200
time = np.linspace(0, (L - 1) * T, L)


def x(t):
    return np.cos(W1 * t) * np.cos(W2 * t)


def DFT(x_, N):
    out = [0. + 0.j for _ in range(N)]
    for k in range(N):
        for n in range(N):
            out[k] += x_[n] * np.e ** (-k * n * 2 * np.pi * 1.j / N)
    return out


def get_magnitude(X_):
    return [np.sqrt(np.real(z) ** 2 + np.imag(z) ** 2) for z in X_]


def get_phase(X_):
    return [np.arctan(np.imag(z) / np.real(z)) if np.real(z) != 0 else np.pi / 2 for z in X_]


x_n = x(time)

# for i in X:
#     print(i)
# print(get_magnitude(X))
# print(get_phase(X))

fig, axs = plt.subplots(3)
fig.suptitle('Άσκηση 2.3 A)')
axs[0].stem(range(0, 100), x_n[:100])
axs[0].set_title("A: x(n)", x=-0.1, y=0)

N = L
X = DFT(x_n, N=N)
axs[1].stem(range(0, (len(X) // 2) * Fs // N, Fs // N), get_magnitude(X[:len(X) // 2]))
axs[1].set_title("B: Magn", x=-0.09, y=0.17)

N = L // 2
X = DFT(x_n, N=N)
axs[2].stem(range(0, (len(X) // 2) * Fs // N, Fs // N), get_magnitude(X[:len(X) // 2]))
axs[2].set_title("Γ: Magn", x=-0.09, y=0.17)
plt.show()
