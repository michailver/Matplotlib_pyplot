# Sugeneruoti sąrašą x, turintį 101 elementą (nuo 0 iki 100).
import random
import matplotlib.pyplot as plt
import numpy as np

x = list(range(101))
# Sukurti antrą sąrašą, kuriame būtų skaičiai, pakelti kvadratu, iš
# pirmojo sąrašo (x*x)
y1 = [i ** 2 for i in x]
# Sukurti trečiąjį sąrašą, kuriame skaičiai būtų pakelti kvadratu ir
# padauginti iš atsitiktinai sugeneruoto skaičiaus (x2*a).
a = random.uniform(1, 2)
y2 = [i ** 2 * a for i in x]
# Sugeneruoti 100-to elementų ilgio sąrašą iš atsitiktinių skaičių.
y3 = [random.randint(1, 100) for _ in range(101)]

# Visus šiuos sąrašus atvaizduoti grafike.
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y1, label="x^2", color="blue")
ax.plot(x, y2, label=f"x^2 * {a:.2f}", color="green")
ax.plot(x, y3, label="Atsitiktiniai skaičiai", color="red", linestyle="--")

# Grafikas turi turėti pavadinimą, pavadintos ašys, pakeisti šriftų dydžiai.
ax.set_title("Grafinė duomenų analizė", fontsize=18)
ax.set_xlabel("x reikšmės", fontsize=14)
ax.set_ylabel("y reikšmės", fontsize=14)
ax.legend(fontsize=12)
ax.grid(True)
plt.show()
