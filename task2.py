# B) Duoti sąrašai x = [1,2,3,4,5], y1=[2,2,0,0,2], y2 = [4,3,2,1,-1],
# y3 =[2,4,9,16,25], y4 = [-1,1,-1,1,-1]
# Atvaizduokite viename lange, skirtinguose grafikuose x~y1, x~y2,
# x~y3, x~y4 grafikus. Pirmasis grafikas - linijinis, antrasis - taškinis,
# trečiasis - linija su duomenų taškais, ketvirtasis - brūkšninis.
# Spalvos visų turi būti skirtingos. Grafikai, ašys turi turėti pavadinimus.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y0 = [2, 2, 0, 0, 2]
y1 = [4, 3, 2, 1, -1]
y2 = [2, 4, 9, 16, 25]
y3 = [-1, 1, -1, 1, -1]


def all_in_one_graphs(x_list, y0_list, y1_list, y2_list, y3_list):
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(x_list, y0_list, label='x~y0 linijinis', color='blue')
    ax.scatter(x_list, y1_list, label='x~y1 taškinis', color='green', marker='o')
    ax.plot(x_list, y2_list, label='x~y2 linija su duomenų taškais', color='red', marker='x',linestyle="-")
    ax.plot(x_list, y3_list, label='x~y3 brūkšninis', color='black', linestyle = '--')

    ax.set_title('Visi grafikai viename', fontsize=16)
    ax.set_xlabel('x reikšmės', fontsize=12)
    ax.set_ylabel('y reikšmės', fontsize=12)
    ax.legend()
    ax.grid(True)
    plt.show()


all_in_one_graphs(x, y0, y1, y2, y3)
