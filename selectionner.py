import random

from tour import distance_totale


def selection_moitie(villes, population, n):
    return sorted(population, key=lambda tour: distance_totale(villes, tour))[:n]


def selection_roulette(villes, population, n):
    distances = [distance_totale(villes, tour) for tour in population]
    fitness = [1 / d for d in distances]
    total_fitness = sum(fitness)
    probabilites = [f / total_fitness for f in fitness]

    selectionnes = random.choices(population, weights=probabilites, k=n)
    return selectionnes


def selection_tournoi(villes, population, n):
    selectionnes = []
    while len(selectionnes) < n:
        candidat1, candidat2 = random.sample(population, 2)
        if distance_totale(villes, candidat1) < distance_totale(villes, candidat2):
            selectionnes.append(candidat1)
        else:
            selectionnes.append(candidat2)

    return selectionnes


def selection_uniforme(villes, population, n):
    return random.sample(population, n)
