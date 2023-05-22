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

fig1, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig1.tight_layout(pad=4.0)
fig2, ax4 = plt.subplots(1, 1)

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax1.plot(N, S, 'r', label='S')
ax1.plot(N, Pen, 'b', label='Pen')
ax1.plot(N, Pmech, 'g', label='Pmech')
ax1.set_xlabel('N(rpm)')
ax1.set_ylabel('S(VA), Pen(W), Pmech(W)')
ax1.legend()
ax2.plot(N, M, 'r', label='M')
ax2.set_xlabel('N(rpm)')
ax2.set_ylabel('M(Nm)')
ax2.legend()
ax3.plot(N, Is, 'r', label='Is')
ax3.set_xlabel('N(rpm)')
ax3.set_ylabel('Is(A)')
ax3.legend()
ax4.plot(N, n, 'r', label='n')
ax4.plot(N, cosphi, 'b', label='cosphi')
ax4.plot(N, [n[i] * cosphi[i] for i in range(len(n))], 'g', label='n*cosphi')
ax4.set_xlabel('N(rpm)')
ax4.set_ylabel('n, cosphi, n*cosphi')
ax4.legend()
plt.show()

