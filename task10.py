# Užduotis 6: Duomenų vizualizacija naudojant stulpelines, linijines ir išsklaidymo diagramas
# Sukurkite stulpelinę diagramą, kuri vaizduoja studento suminius rezultatus penkiose skirtingose pamokose.
# Naudokite linijinę diagramą, kad parodytumėte ryšį tarp studijų valandų ir rezultatų (galite extrapoliuoti įverčius gražesniam atvaizdavimui)
import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Science', 'History', 'Art', 'PE']
scores =      [85, 90, 78, 92, 88]
study_hours = [10, 15, 12, 18, 20]

bar_width = 0.4
x = np.arange(len(subjects))

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(subjects, scores, color='skyblue', label='scores')
ax1.set_xlabel('Pamokos', fontsize=12)
ax1.set_ylabel('Rezultatai', fontsize=12)

ax2 = ax1.twinx()
ax2.plot(subjects, study_hours, color='green', marker='o', label='Hours', linewidth=2)

plt.show()
