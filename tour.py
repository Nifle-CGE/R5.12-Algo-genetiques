import random

from numba import jit

from villes import distance


def distance_totale(villes, tour) -> float:
    total = 0.
    for i in range(len(tour)):
        ville1 = villes[tour[i]]
        ville2 = villes[tour[(i + 1) % len(tour)]]
        total += distance(ville1, ville2)

    return total


def tour_aleatoire(n) -> list[int]:
    tour = list(range(n))
    random.shuffle(tour)
    return tour
