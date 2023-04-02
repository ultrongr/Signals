import pandas as pd
import matplotlib.pyplot as plt

volt1, volt2 = 92, 91

# Read the CSV file into a pandas dataframe
df1 = pd.read_csv('team7/tek00000.csv')
df2 = pd.read_csv('team7/tek00001.csv')

x1 = df1["-9.240e-06"]
y1 = df1['-8']
x2 = df2["-9.240e-06"]
y2 = df2['-20']
max1 = max(y1)
max2 = max(y2)
print("ΥΠΟΛΟΓΙΣΜΟΣ ΕΥΡΟΥΣ\n")
print("\tΠΡΑΓΜΑΤΙΚΗ ΜΕΤΡΗΣΗ")
print(f"\tΜέγιστη ένδειξη παλμογράφου για πρώτο πείραμα:   {max1}V")
print(f"\tΜέγιστη ένδειξη βολτομέτρου για πρώτο πείραμα:   {volt1}V")
print(f"\tΜέγιστη ένδειξη παλμογράφου για δεύτερο πείραμα: {max2}V")
print(f"\tΜέγιστη ένδειξη βολτομέτρου για δεύτερο πείραμα: {volt2}V")
print(f"\n\tΣΥΝΥΠΟΛΟΓΙΖΟΝΤΑΣ ΤΟΝ ΥΠΟΒΙΒΑΣΜΟ")
print(f"\tΜέτρηση παλμογράφου πρώτου πειράματος συνυπολιγίζοντας τον υποβιβασμό:   {max1 * 241 / 1000:.2f}kV")
print(f"\tΜέτρηση βολτομέτρου πρώτου πειράματος συνυπολογίζοντας τον υποβιβασμό:   {volt1 * 4 * 241 / 1000:.2f}kV")
print(f"\tΜέτρηση παλμογράφου δεύτερου πειράματος συνυπολιγίζοντας τον υποβιβασμό: {max2 * 241 / 1000:.2f}kV")
print(f"\tΜέτρηση βολτομέτρου δεύτερου πειράματος συνυπολογίζοντας τον υποβιβασμό: {volt2 * 4 * 241 / 1000:.2f}kV")

print("\n\nΥΠΟΛΟΓΙΣΜΟΣ ΧΑΡΑΚΤΗΡΙΣΤΙΚΩΝ ΣΤΟΙΧΕΙΩΝ")

"""ΥΠΟΛΟΓΙΣΜΟΣ ΧΡΟΝΩΝ ΣΕ ΠΕΙΡΑΜΑ ΧΩΡΙΣ ΔΙΑΣΠΑΣΗ"""
times = {
    "100%": 0,
    "90%": 0,
    "30%": 0,
    "50%'": 0,
}

err = 2
for i in range(len(x2)):
    if abs(y2[i] - 0.9 * max2) < err and not times["90%"]:
        times["90%"] = x2[i]
    if abs(y2[i] - 0.3 * max2) < err and not times["30%"]:
        times["30%"] = x2[i]
    if y2[i] == max2 and not times["100%"]:
        times["100%"] = x2[i]

T = times["90%"] - times["30%"]
slope = 0.6 / T  # y = slope*t+b
b = 0.3 - slope * times["30%"]
T0 = -b / slope
T_tone = times["30%"] - T0
T1 = (1 - b) / slope  # Ανόδου
T2 = x1[len(x1) - 1] - T0  # Ουράς (Θεωρούμε ότι η τελευταία μέτρηση ειναι 50% του μεγίστου)
print(f"\tΧρόνος ανόδου (μέτωπο): {T1:.3E}s")
print(f"\tΧρόνος ουράς: {T2:.3E}s")

"""ΥΠΟΛΟΓΙΣΜΟΣ ΧΡΟΝΩΝ ΣΕ ΠΕΙΡΑΜΑ ΜΕ ΔΙΑΣΠΑΣΗ (χρόνος διάσπασης)"""

t50 = 0
t50_tone = 0
err = 5
for i in range(len(x1)):
    if abs(y1[i] - 0.5 * max1) < err:
        t50 = x1[i]
        break
for i in range(len(x1)-1, 0, -1):
    if abs(y1[i] - 0.5 * max1) < err:
        t50_tone = x1[i]
        break
print(f"\tΧρόνος διάσπασης: {t50_tone - t50:.3E}s")
print(f"\tΕύρος: {max1 * 241 / 1000:.2f}kV")

fig, axs = plt.subplots(2)
fig.set_figwidth(10)
fig.set_figheight(10)
fig.tight_layout(pad=3.0)
axs[0].plot(x1, y1, linewidth=0.25)
axs[0].set_title("Με διάσπαση")
axs[0].set_ylabel("Τάση (kV)")
axs[0].set_xlabel("Χρόνος (s)")
axs[1].plot(x2, y2, linewidth=0.25)
axs[1].set_title("Χωρίς διάσπαση")
axs[1].set_ylabel("Τάση (kV)")
axs[1].set_xlabel("Χρόνος (s)")

# Display the plot
plt.show()
