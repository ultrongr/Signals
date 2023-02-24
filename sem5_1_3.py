import matplotlib.pyplot as plt
import numpy as np
import random
import math

plt.rcParams['agg.path.chunksize'] = 10000000000000000000
o = 10
repetitions = 30
phi = 0
time = np.linspace(-5 * np.pi, 5 * np.pi, 100)


def random_process(_t):
    return 10*np.cos(o * _t + phi)


values = {}  # values of X(t)

for i in range(repetitions):  # creating 10 instances of the random process
    phi = 2 * (0.5 - random.random()) * np.pi
    for t in time:
        if not values.get(t):
            values[t] = []
        values[t].append(random_process(t))

fxx_list = {}  # a dictionary of lists of values of X(t)*X(t+τ) as a function of τ

for index_m, m in enumerate(list(values.keys())):
    print(m)
    for index_n, n in enumerate(list(values.keys())):

        for Xm in values[m]:
            for Xn in values[n]:
                difference = math.floor(100 * (n - m)) / 100  # standardize the value
                if not fxx_list.get(difference):
                    fxx_list[difference] = []
                fxx_list[difference].append(Xm * Xn)
print(1)

fxx = []  # the expected value for each τ (aka φχχ(τ))
keys = list(fxx_list.keys())

keys.sort()
print(keys)
for key in keys:
    values_list = fxx_list[key]
    # print(type(values_list), values_list)
    fxx.append(sum(values_list) / len(values_list))
    print(key, len(values_list))

# print(len(fxx))
print(fxx[-1], fxx[0])
fig, axs = plt.subplots(1)
fig.suptitle('Άσκηση 1.3')
axs.plot(keys, fxx, color="blue")
# axs.set_title("Sxx(Ω)", x=-0.1, y=0)
plt.show()
