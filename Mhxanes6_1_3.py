from numpy import pi
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib as mpl

d = 0.231  # Απόσταση δυναμομέτρου από τον άξονα
Vs = 380  # Τάση στάτορα
F = [0, 10, 20, 30, 40, 50, 56]  # Δύναμη στο δυναμόμετρο
N = [1499, 1485, 1480, 1470, 1462, 1454, 1446]  # Στροφές ανά λεπτό
Is = [5.2, 5.4, 5.5, 5.8, 6.2, 6.5, 6.9]  # Ρεύμα στάτη
Pen = list(120 * p for p in [4, 7, 10.5, 14.5, 18.2, 21.5, 24.5])  # Ενδείξεις βαττομέτρου μετατρέπονται σε Watts
M = list(f * d for f in F)  # Ροπή

S = []
Pmech = []
cosphi = []
Q = []
n = []


for i in range(len(F)):
    S.append(sqrt(3) * Is[i] * Vs)
    Pmech.append(M[i] * 2 * pi * N[i] / 60)
    cosphi.append(Pen[i] / S[i])
    Q.append(sqrt(S[i] ** 2 - Pen[i] ** 2))
    n.append(Pmech[i] / Pen[i])


mpl.rcParams['figure.dpi'] = 150
plt.rcParams["figure.figsize"] = (8, 8)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1twin = ax1.twinx()
ax1.plot(N, S, label='S')
ax1.plot(N, Pen, label='Pen')
ax1.plot(N, Pmech, label='Pmech')
ax1.set_xlabel('N(rpm)')
ax1.set_ylabel('S(VA), Pen(W), Pmech(W)')

ax1twin.set_ylabel('Is(A), M(Nm)', color = "black")
ax1twin.plot(N, Is, label='Is', color = "black")
ax1twin.plot(N, M, label='M', color = "red")
ax1twin.tick_params(axis='y', labelcolor='black')



ax1.legend()
ax1twin.legend()
ax2.plot(N, n, label='n')
ax2.plot(N, cosphi, label='cosphi')
ax2.plot(N, [n[i] * cosphi[i] for i in range(len(n))], label='n*cosphi')
ax2.set_xlabel('N(rpm)')
ax2.set_ylabel('n, cosphi, n*cosphi')
ax2.legend()
plt.show()
