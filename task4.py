import matplotlib.pyplot as plt
# Turimos vidutinės mėnesių temparatūros
# tC=[-3.2, -3.2, +0.4, +6.7, +12.4, +15.4, +17.9, +17.1, +12.3,
# ↪ +7.2, +1.9, -1.9]
# Nubraižykite stulpelinę diagramą. Neigiamas temperatūras
# rodantys stulpeliai turi būti mėlyni, o teigiamas - žali. x ašyje
# turi būti rodomi mėnesių pavadinimai.
tC=[-3.2, -3.2, +0.4, +6.7, +12.4, +15.4, +17.9, +17.1, +12.3,+7.2, +1.9, -1.9]
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
        ]
colors1 =[]
for el in tC:
    if el <0:
        colors1.append('blue')
    else:
        colors1.append('green')
# Kita budas uzrasyti cikla:
colors2 = ['green' if t >= 0 else 'blue' for t in tC]

fig, ax = plt.subplots()
fig.set_size_inches(10,5)
ax.bar(months,tC,color=colors2)
ax.set_ylabel('Temperature', fontsize=16)
ax.set_xlabel('Month', fontsize=16)
ax.tick_params(axis='x', labelsize=8)
plt.show()