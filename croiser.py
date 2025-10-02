import random


def croiser_ordre(villes, tour1, tour2): # Très similaire à deux découpes
    n = len(tour1)
    i, j = sorted(random.sample(range(n), 2))

    enfant = [-1] * n
    enfant[i:j] = tour1[i:j]

    pos = j
    for k in range(n):
        ville = tour2[(j + k) % n]
        if ville not in enfant:
            enfant[pos % n] = ville
            pos += 1

    return enfant


def croiser_ordre_modifie(villes, tour1, tour2): # Variante de croiser_ordre et c'est comme si on faisait une découpe
    n = len(tour1)
    i = random.randint(0, n - 1)

    enfant = [-1] * n
    enfant[:i] = tour1[:i]

    pos = i
    for ville in tour2:
        if ville not in enfant:
            enfant[pos] = ville
            pos += 1

    return enfant


def croiser_cycle(villes, tour1, tour2):
    n = len(tour1)
    enfant = [-1] * n

    start = random.randint(0, n - 1)
    index = start

    while True:
        enfant[index] = tour1[index]
        index = tour1.index(tour2[index])
        if index == start:
            break

    for i in range(n):
        if enfant[i] == -1:
            enfant[i] = tour2[i]

    return enfant


def croiser_grefenstette(villes, tour1, tour2):
    n = len(tour1)
    i, j = sorted(random.sample(range(n), 2))

    enfant = [-1] * n
    enfant[i:j] = tour1[i:j]

    edge_list = {k: set() for k in range(n)}
    for t in (tour1, tour2):
        for idx in range(n):
            edge_list[t[idx]].add(t[(idx - 1) % n])
            edge_list[t[idx]].add(t[(idx + 1) % n])
            

    return enfant
