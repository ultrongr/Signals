import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(-10, 10, 100)


def x1(t):
    return abs(t)/(t*t+1)**0.5


def x2(t):

    return np.arctan(1/t)


fig, axs = plt.subplots(2)
fig.suptitle('Άσκηση 2.2 β)')
axs[0].plot(time, x1(time), color="blue", )
axs[0].set_title("|H(ω)|", x=0.022, y=0.2)
axs[1].plot(time, x2(time), color="red")
axs[1].set_title("<H(ω)", x=0.022, y=0.2)
plt.show()