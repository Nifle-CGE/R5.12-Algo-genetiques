import random

from tour import Tour
from villes import Villes


def croiser_ordre(tour1: Tour, tour2: Tour) -> Tour:
    """Order crossover (OX) : découpe et complète par ordre.

    - On choisit deux points i<j et on copie la sous-séquence de `tour1`.
    - On parcourt `tour2` dans l'ordre et on complète l'enfant par les
      villes manquantes en respectant l'ordre d'apparition dans `tour2`.
    """
    n = Villes().n
    # indices de découpe
    i, j = sorted(random.sample(range(n), 2))

    enfant = [-1] * n
    # copie de la tranche centrale depuis le parent1
    enfant[i:j] = tour1.sequence[i:j]

    # remplir le reste à partir de parent2 en conservant l'ordre
    pos = j
    for k in range(n):
        ville = tour2.sequence[(j + k) % n]
        if ville not in enfant:
            enfant[pos % n] = ville
            pos += 1

    return Tour(enfant)


def croiser_ordre_modifie(tour1: Tour, tour2: Tour) -> Tour:
    """Variante simple d'OX : on copie le préfixe d'un parent, puis on complète.

    Cette version choisit un point i et copie `tour1[:i]`, puis complète
    avec les villes de `tour2` dans leur ordre d'apparition.
    """
    n = Villes().n
    i = random.randint(0, n - 1)

    enfant = [-1] * n
    enfant[:i] = tour1.sequence[:i]

    pos = i
    for ville in tour2.sequence:
        if ville not in enfant:
            enfant[pos] = ville
            pos += 1

    return Tour(enfant)


def croiser_cycle(tour1: Tour, tour2: Tour) -> Tour:
    """Cycle Crossover (CX) : conserve des cycles d'indices entre parents.

    On suit les cycles d'indices pour copier des positions depuis `tour1`,
    puis on remplit les positions restantes depuis `tour2`.
    """
    n = Villes().n
    enfant = [-1] * n

    start = random.randint(0, n - 1)
    index = start

    # construire le cycle à partir de `start`
    while True:
        enfant[index] = tour1.sequence[index]
        index = tour1.sequence.index(tour2.sequence[index])
        if index == start:
            break

    # compléter les positions non assignées depuis le parent2
    for i in range(n):
        if enfant[i] == -1:
            enfant[i] = tour2.sequence[i]

    return Tour(enfant)


def croiser_grefenstette(tour1: Tour, tour2: Tour) -> Tour:
    """Greffenstette Crossover : utilise une liste d'arêtes pour construire l'enfant.

    - Pour chaque ville, on construit une liste d'arêtes possibles (voisins
      dans les deux parents).
    - On choisit un noeud de départ, puis on ajoute des villes à l'enfant
      en suivant les arêtes avec le moins de voisins restants.
    - Si un noeud n'a plus de voisins, on choisit un noeud non encore sélectionné.
    """

    n = Villes().n

    # construire la liste d'arêtes pour chaque ville (voisins dans les deux parents)
    edge_list = {k: set() for k in range(n)}
    for t in (tour1.sequence, tour2.sequence):
        for idx in range(n):
            edge_list[t[idx]].add(t[(idx - 1) % n])
            edge_list[t[idx]].add(t[(idx + 1) % n])

    enfant = [-1] * n

    # choisir un noeud de départ avec le moins de voisins
    start_candidates = [tour1.sequence[0], tour2.sequence[0]]
    start = min(start_candidates, key=lambda x: len(edge_list[x]))
    index = start

    for i in range(n):
        enfant[i] = index
        # supprimer le noeud courant des listes d'arêtes
        for edges in edge_list.values():
            edges.discard(index)

        # choisir le prochain noeud avec le moins de voisins restants
        if edge_list[index]:
            index = min(edge_list[index], key=lambda x: len(edge_list[x]))
        else:
            # si aucun voisin n'est disponible, choisir un noeud non encore sélectionné
            non_selected = [k for k in range(n) if k not in enfant]
            if non_selected:
                index = random.choice(non_selected)
            else:
                break  # tous les noeuds ont été sélectionnés

    return Tour(enfant)
