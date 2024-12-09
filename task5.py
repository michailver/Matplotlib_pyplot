# Užduotis 5: Pardavimų duomenų stulpelinė diagrama

# Nubraižykite stulpelinę diagramą, kurioje pateikiami įmonės mėnesiniai pardavimai.
# Pridėkite etiketes kiekvienai juostai ir pritaikykite juostų spalvas.
# Įrašykite diagramai pavadinimą ir pažymėkite ašių pavadinimus.
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May']
sales = [1500, 2000, 1800, 2200, 2100]
colors = ['blue', 'gray', 'orange', 'red', 'green' ]

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
bars = ax.bar(months, sales, color = colors)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

ax.set_title('Sales data bar chart', fontsize=20)
ax.set_ylabel('Sales', fontsize=10)
ax.set_xlabel('Month', fontsize=10)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
plt.show()
