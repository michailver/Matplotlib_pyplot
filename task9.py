# Užduotis 5: Stulpelinė diagrama su anotacijomis
# Nubraižykite stulpelinę diagramą, kurioje pateikiami studentų rezultatai penkiose pamokose.
# Pridėkite anotacijas ant stulpelių, rodančias tikslius rezultatus, naudodami ax.annotate().
subjects = ['Math', 'Science', 'History', 'Art', 'PE']
scores = [85, 90, 78, 92, 88]

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
bars = ax.bar(subjects, scores, color=['blue', 'gray', 'orange', 'red', 'green'])

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

plt.show()
