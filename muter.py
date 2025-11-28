import random

import numpy as np

from tour import Tour
from villes import Villes


def muter_echange(tour: Tour) -> None:
    tour_sequence = tour.sequence
    n = Villes().n
    i = np.random.randint(0, n - 1)
    j = np.random.randint(0, n - 1)
    while j == i:
        j = random.randint(0, n - 1)
    tour_sequence[i], tour_sequence[j] = tour_sequence[j], tour_sequence[i]

    tour.sequence = tour_sequence
    tour.distance = tour.calculer_distance()
