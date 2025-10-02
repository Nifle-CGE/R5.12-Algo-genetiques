import random


def muter_echange(villes, tour: list[int]) -> None:
    i, j = random.sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]
