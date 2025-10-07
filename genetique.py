import time

from tour import *
from villes import *


def algorithme_genetique(
            villes,
            taille_population: int,
            temps_dexecution: float,
            proba_mutation: float,
            selectionner,
            croiser,
            muter,
            montrer_evolution: bool
        ) -> tuple[list[int], float, int, list[tuple[list[int], float]]]:

    n = len(villes)
    population = [tour_aleatoire(n) for _ in range(taille_population)]

    start = time.perf_counter()
    generations = 0
    evolution = []
    while time.perf_counter() - start < temps_dexecution:
        selection = selectionner(villes, population)
        nouvelle_population = selection
        while len(nouvelle_population) < taille_population:
            parent1, parent2 = random.sample(selection, 2)
            enfant = croiser(villes, parent1, parent2)

            mutation = proba_mutation
            while mutation > 0:  # si proba_mutation > 1, faire plusieurs mutations
                if random.random() < mutation:
                    muter(villes, enfant)
                mutation -= 1

            nouvelle_population.append(enfant)

        population = nouvelle_population

        generations += 1

        if montrer_evolution:
            meilleur_tour = min(population, key=lambda tour: distance_totale(villes, tour))
            evolution.append((meilleur_tour, distance_totale(villes, meilleur_tour)))

        # si pas d'évolution depuis 10 générations, doubler la probabilité de mutation
        if len(evolution) > 10 and evolution[-1][1] >= evolution[-10][1]:
            proba_mutation *= 2

    meilleur_tour = min(population, key=lambda tour: distance_totale(villes, tour))
    return meilleur_tour, distance_totale(villes, meilleur_tour), generations, evolution
