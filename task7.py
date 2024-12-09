import matplotlib.pyplot as plt
# Užduotis 3: Išlaidų pasiskirstymo pyrago diagrama
# Sukurkite pyrago diagramą, rodydami mėnesinių išlaidų (pvz., nuoma, maistas, transportas, pramogos) procentinį pasiskirstymą.
# Pridėkite procentus pyrago skiltelėms, naudodami autopct='%1.1f%%'.


categories = ['Rent', 'Food', 'Transport', 'Entertainment', 'Others']
expenses = [40, 25, 15, 10, 10] # In percentages

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'orange', 'red', 'purple'])

ax.legend()
plt.show()
