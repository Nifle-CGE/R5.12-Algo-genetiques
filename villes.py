import math
import random
import time

import matplotlib.pyplot as plt
from numba import jit


def villes_aleatoires(n: int, seed=None) -> list[tuple[float, float]]:
    if seed is not None:
        random.seed(seed)

    villes = []
    for _ in range(n):
        ville = (random.random(), random.random())
        villes.append(ville)

    return villes


def villes_en_cercle(n: int) -> list[tuple[float, float]]:
    villes = []
    radius = 0.5
    for i in range(n):
        angle = 2 * math.pi * i / n
        ville = (0.5 + radius * math.cos(angle), 0.5 + radius * math.sin(angle))
        villes.append(ville)

    return villes


def villes_defi_250() -> list[tuple[float, float]]:  # a battre 12.130 en 2mn avec 5 * nb_villes
    villes = []
    with open("defi250.csv", "r") as f:
        data = f.readlines()

    for line in data[1:]:
        x, y = map(float, line.strip().split(";"))
        villes.append((x, y))

    return villes


def visualiser_villes(villes, tour=None, nom_fichier=None):
    x = [ville[0] for ville in villes]
    y = [ville[1] for ville in villes]

    plt.figure(figsize=(8, 8))
    plt.scatter(x, y, color='blue')

    if tour is not None:
        tour_x = [villes[i][0] for i in tour] + [villes[tour[0]][0]]
        tour_y = [villes[i][1] for i in tour] + [villes[tour[0]][1]]
        plt.scatter(tour_x[0], tour_y[0], color='red', s=100, label='Départ/Arrivée')
        plt.plot(tour_x, tour_y, color='red')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()

    if nom_fichier is not None:
        plt.title(nom_fichier)
        plt.savefig(f"./images/figure_{int(time.time())}.png")
    else:
        plt.title('Visualisation des villes et du tour')
        plt.show()


def distance(ville1, ville2) -> float:
    return ((ville1[0] - ville2[0]) ** 2 + (ville1[1] - ville2[1]) ** 2) ** 0.5
