import random

from tour import Tour
from villes import Villes


def croiser_ordre(tour1: Tour, tour2: Tour) -> Tour:  # Très similaire à deux découpes
    n = Villes().n
    i, j = sorted(random.sample(range(n), 2))

    enfant = [-1] * n
    enfant[i:j] = tour1.sequence[i:j]

    pos = j
    for k in range(n):
        ville = tour2.sequence[(j + k) % n]
        if ville not in enfant:
            enfant[pos % n] = ville
            pos += 1

    return Tour(enfant)


def croiser_ordre_modifie(tour1: Tour, tour2: Tour) -> Tour:  # Variante de croiser_ordre et c'est comme si on faisait une découpe
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
    n = Villes().n
    enfant = [-1] * n

    start = random.randint(0, n - 1)
    index = start

    while True:
        enfant[index] = tour1.sequence[index]
        index = tour1.sequence.index(tour2.sequence[index])
        if index == start:
            break

    for i in range(n):
        if enfant[i] == -1:
            enfant[i] = tour2.sequence[i]

    return Tour(enfant)


def croiser_grefenstette(tour1: Tour, tour2: Tour) -> Tour:
    n = Villes().n
    i, j = sorted(random.sample(range(n), 2))

    enfant = [-1] * n
    enfant[i:j] = tour1.sequence[i:j]

    edge_list = {k: set() for k in range(n)}
    for t in (tour1.sequence, tour2.sequence):
        for idx in range(n):
            edge_list[t[idx]].add(t[(idx - 1) % n])
            edge_list[t[idx]].add(t[(idx + 1) % n])

    return Tour(enfant)
