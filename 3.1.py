import matplotlib.pyplot as plt
import numpy as np

time1 = np.linspace(0, 2 * np.pi, 50)
time2 = np.linspace(0, 8 * np.pi, 50)
time3 = np.linspace(0, 4 * np.pi, 50)


def x1(n):
    return np.cos(6 * np.pi * n / 7 + 1)


def x2(n):
    return np.cos(np.pi * n / 8) * np.cos(np.pi * n / 8)


def x3(n):
    return np.cos(np.pi * n / 2) * np.cos(np.pi * n / 4)


fig, axs = plt.subplots(3)
fig.suptitle('Άσκηση 3.1 ')
axs[0].stem(time1, x1(time1))
axs[0].set_title("x1", x=0.022, y=0.2)
axs[1].stem(time2, x2(time2))
axs[1].set_title("x2", x=0.022, y=0.2)
axs[2].stem(time3, x3(time3))
axs[2].set_title("x3", x=0.022, y=0.2)

plt.show()
