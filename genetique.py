import random
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
    """Exécute l'algorithme génétique.

    Paramètres:
    - `taille_population`: nombre d'individus dans la population
    - `temps_dexecution`: durée maximale d'exécution (en secondes)
    - `proba_mutation`: probabilité de mutation (peut être supérieuse à 1
      pour indiquer plusieurs mutations)
    - `selectionner`, `croiser`, `muter`: fonctions fournies par l'appelant

    Retourne `(meilleur_tour, generations, evolution)`.
    """

    # initialiser la population avec des tours aléatoires
    population = [Tour(tour_aleatoire(Villes().n)) for _ in range(taille_population)]

    start = time.perf_counter()
    generations = 0
    evolution: list[Tour] = []

    # boucle principale : s'exécute pendant `temps_dexecution` secondes
    while time.perf_counter() - start < temps_dexecution:
        # sélection des parents selon la stratégie fournie
        selection: list[Tour] = selectionner(population)
        nouvelle_population = selection

        # remplir la nouvelle population par croisements et mutations
        while len(nouvelle_population) < taille_population:
            parent1, parent2 = random.sample(selection, 2)
            enfant = croiser(parent1, parent2)

            # si `proba_mutation` > 1, appliquer potentiellement plusieurs mutations
            mutation = proba_mutation
            while mutation > 0:
                if random.random() < mutation:
                    muter(enfant)
                mutation -= 1

            nouvelle_population.append(enfant)

        population = nouvelle_population

        generations += 1

        # enregistrer le meilleur individu de la génération
        meilleur_tour = min(population, key=lambda tour: tour.distance)
        evolution.append(meilleur_tour)

        # simple heuristique : si aucune amélioration depuis 10 générations,
        # augmenter la probabilité de mutation (exploration accrue)
        if len(evolution) > 10 and evolution[-1].distance >= evolution[-10].distance:
            proba_mutation *= 2

    meilleur_tour = min(population, key=lambda tour: tour.distance)
    return meilleur_tour, generations, evolution
