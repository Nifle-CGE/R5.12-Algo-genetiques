import random

from tour import Tour


def muter_echange(tour: Tour) -> None:
    tour_sequence = tour.sequence
    i, j = random.sample(range(len(tour_sequence)), 2)
    tour_sequence[i], tour_sequence[j] = tour_sequence[j], tour_sequence[i]

    tour.sequence = tour_sequence
    tour.distance = tour.calculer_distance()
