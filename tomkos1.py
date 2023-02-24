import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(-20, 20, 1000)

a = 5
A = 1


def xa(t):
    return A * np.sin(t)


def xb(t):
    out = []
    for _t in t:
        out.append(A * ((1 if a + _t >= 0 else 0) - (1 if _t - a >= 0 else 0)))
    return out


def xc(t):
    return np.e ** (-a * abs(t))


def xd(t):
    out = []
    for _t in t:
        out.append(0 + (_t >= 0))
    return out


def xe(t):
    out = []
    for _t in t:
        out.append(_t * (_t >= 0))
    return out


def x2_2(t):
    w0 = 10
    return -0.5 * np.sin(a * t) * np.cos(w0 * t) / (np.pi ** 2 * t)


fig, axs = plt.subplots(1)
fig.suptitle('Άσκηση 2.2')
axs.plot(time, x2_2(time), color="blue", )
axs.set_title("χ(t)", x=-0.1, y=-0.1)

plt.show()
