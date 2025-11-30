import random

from tour import Tour


def selection_moitie(population: list[Tour], n: int):
    """Sélection par tri : renvoie les `n` meilleurs individus (plus petits distances)."""
    return sorted(population, key=lambda tour: tour.distance)[:n]


def selection_roulette(population: list[Tour], n: int):
    """Sélection proportionnelle (roulette) basée sur le fitness = 1/distance.

    Les probabilités sont normalisées pour former une distribution de poids.
    """
    distances = [tour.distance for tour in population]
    fitness = [1 / d for d in distances]
    total_fitness = sum(fitness)
    probabilites = [f / total_fitness for f in fitness]

    selectionnes = random.choices(population, weights=probabilites, k=n)
    return selectionnes


def selection_1v1(population: list[Tour], n: int):
    """Sélection par tournoi 1 contre 1."""
    selectionnes = []
    for _ in range(n):
        candidat1, candidat2 = random.sample(population, 2)
        if candidat1.distance < candidat2.distance:
            selectionnes.append(candidat1)
        else:
            selectionnes.append(candidat2)

    return selectionnes


def selection_uniforme(population: list[Tour], n: int):
    """Sélection aléatoire uniforme sans remise (échantillonnage simple)."""
    return random.sample(population, n)
