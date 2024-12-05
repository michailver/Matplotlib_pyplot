# A) Duotas sąrašas x=[1,2,3,4,5,6,7,8,9]
# Viename lange, skirtinguose grafikuose atvaizduokite x*x, x * 3, x * a, čia a - įvedamas vartotojo.
# Panaudokite skirtingas spalvas, linijų tipus.
import matplotlib.pyplot as plt

x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 10  # int(input('iveskit a reik6me: '))

y0_list = [x * x for x in x_list]  # x*x
y1_list = [x * 3 for x in x_list]  # x*3
y2_list = [2 / x * a for x in x_list]  # x*a


def three_different_graphs(x_list, y0_list, y1_list, y2_list):
    fig, ax = plt.subplots(3, figsize=(8, 6))
    # čia būtų braižymo komandos
    ax[0].plot(x_list, y0_list, label='x^2', color='blue', linewidth=2.0)
    ax[1].plot(x_list, y1_list, label='x * 3', color='green', linewidth=5.0)
    ax[2].plot(x_list, y2_list, label=f'x * {a}', color='red')
    plt.tight_layout()
    plt.show()


def all_in_one_graphs(x_list, y0_list, y1_list, y2_list):
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(x_list, y0_list, label='y = x^2', color='blue', marker='v')
    ax.plot(x_list, y1_list, label='y = x * 3', color='green', marker='2')
    ax.plot(x_list, y2_list, label=f'y = x * {a}', color='red', marker='x')

    ax.set_title('Visi grafikai viename', fontsize=16)
    ax.set_xlabel('x reikšmės', fontsize=12)
    ax.set_ylabel('y reikšmės', fontsize=12)
    ax.legend()
    ax.grid(True)
    plt.show()


three_different_graphs(x_list, y0_list, y1_list, y2_list)
all_in_one_graphs(x_list, y0_list, y1_list, y2_list)
