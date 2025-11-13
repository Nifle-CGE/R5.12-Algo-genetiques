import random

from point2d import Point2D

from villes import Villes, distance


class Tour():
    def __init__(self, sequence: list[int]):
        self.sequence = sequence
        self.distance = self.calculer_distance()

    def calculer_distance(self) -> float:
        villes = Villes().villes
        total = 0.
        for i in range(len(self.sequence)):
            ville1 = villes[self.sequence[i]]
            ville2 = villes[self.sequence[(i + 1) % len(self.sequence)]]
            total += distance(ville1, ville2)

        return total


def tour_aleatoire(n: int) -> list[int]:
    tour = list(range(n))
    random.shuffle(tour)

    return tour
