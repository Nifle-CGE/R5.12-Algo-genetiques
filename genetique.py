import time

from tour import *
from villes import *


def algorithme_genetique(
            taille_population: int,
            temps_dexecution: float,
            proba_mutation: float,
            selectionner,
            croiser,
            muter,
        ) -> tuple[Tour, int, list[Tour]]:

    population = [Tour(tour_aleatoire(Villes().n)) for _ in range(taille_population)]

    start = time.perf_counter()
    generations = 0
    evolution: list[Tour] = []
    while time.perf_counter() - start < temps_dexecution:
        selection: list[Tour] = selectionner(population)
        nouvelle_population = selection
        while len(nouvelle_population) < taille_population:
            parent1, parent2 = random.sample(selection, 2)
            enfant = croiser(parent1, parent2)

            mutation = proba_mutation
            while mutation > 0:  # si proba_mutation > 1, faire plusieurs mutations
                if random.random() < mutation:
                    muter(enfant)
                mutation -= 1

            nouvelle_population.append(enfant)

        population = nouvelle_population

        generations += 1

        meilleur_tour = min(population, key=lambda tour: tour.distance)
        evolution.append(meilleur_tour)

        # si pas d'évolution depuis 10 générations, doubler la probabilité de mutation
        if len(evolution) > 10 and evolution[-1].distance >= evolution[-10].distance:
            proba_mutation *= 2

    meilleur_tour = min(population, key=lambda tour: tour.distance)
    return meilleur_tour, generations, evolution
