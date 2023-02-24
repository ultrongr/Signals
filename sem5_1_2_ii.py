import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(-200, 200, 1000)


def Sxx(O):
    return 576 / (324 + O ** 2)


def Syy(O):
    return (576 * O ** 2) / (324 + O ** 2)


def IHI(O):
    return O


fig, axs = plt.subplots(3)
fig.suptitle('Άσκηση 1.2 ii)')
axs[0].plot(time, Sxx(time), color="blue", )
axs[0].set_title("Sxx(Ω)", x=-0.1, y=0)
axs[1].plot(time, Syy(time), color="red")
axs[1].set_title("Syy(Ω)", x=-0.1, y=0.2)
axs[2].plot(time, IHI(time), color="yellow")
axs[2].set_title("<H(Ω)", x=-0.1, y=0.2)
plt.show()
