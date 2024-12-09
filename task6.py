import matplotlib.pyplot as plt
import numpy as np

# Užduotis 2: Gyventojų palyginimas
# Sukurkite sugrupuotą stulpelinę diagramą, kuri palygina vyrų ir moterų gyventojų skaičius penkiose Lietuvos miestose.
# Pridėkite legendą, kad būtų galima atskirti grupes.


cities = ['Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', 'Panevėžys']
populations_men = [280000, 156800, 78500, 80587, 67395]
populations_women = [262366, 150000, 88500, 50587, 57395]
bar_width = 0.4
x = np.arange(len(cities))

fig, ax = plt.subplots(figsize=(10, 6))
men = ax.bar(x - bar_width / 2, populations_men, bar_width, color='red', label='men')
women = ax.bar(x + bar_width / 2, populations_women, bar_width, color='blue', label='women')
ax.set_xticks(x)
ax.set_xticklabels(cities)
ax.legend()
plt.show()
