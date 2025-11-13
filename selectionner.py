import random

from tour import Tour


def selection_moitie(population: list[Tour], n: int):
    return sorted(population, key=lambda tour: tour.distance)[:n]


def selection_roulette(population: list[Tour], n: int):
    distances = [tour.distance for tour in population]
    fitness = [1 / d for d in distances]
    total_fitness = sum(fitness)
    probabilites = [f / total_fitness for f in fitness]

    selectionnes = random.choices(population, weights=probabilites, k=n)
    return selectionnes


def selection_tournoi(population: list[Tour], n: int):
    selectionnes = []
    while len(selectionnes) < n:
        candidat1, candidat2 = random.sample(population, 2)
        if candidat1.distance < candidat2.distance:
            selectionnes.append(candidat1)
        else:
            selectionnes.append(candidat2)

    return selectionnes


def selection_uniforme(population: list[Tour], n: int):
    return random.sample(population, n)
