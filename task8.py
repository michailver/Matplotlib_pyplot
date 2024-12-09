# Užduotis 4: Pyrago diagramos pritaikymas
# Sukurkite pyrago diagramą, atlikdami apklausą apie mėgstamiausius augintinius (pvz., šuo, katė, triušis, paukštis).
# Išryškinkite tą skiltelę, kuri turi didžiausią procentą, naudodami explode parametrą.
pets = ['Dog', 'Cat', 'Rabbit', 'Bird']
votes = [50, 30, 10, 10]
import matplotlib.pyplot as plt

max_vote = votes.index(max(votes))

explode= [0.05 if i == max_vote else 0 for i in range(len(votes))]

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(votes, labels=pets, explode=explode, autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'orange', 'red', 'purple'])

ax.legend()
plt.show()