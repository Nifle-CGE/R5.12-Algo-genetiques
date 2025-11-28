import random

from villes import Villes


class Tour():
    def __init__(self, sequence: list[int]):
        self.sequence = sequence
        self.distance = self.calculer_distance()

    def calculer_distance(self) -> float:
        villes = Villes()
        total = 0.
        for i in range(villes.n - 1):
            total += villes.distance_matrix[self.sequence[i]][self.sequence[i + 1]]

        total += villes.distance_matrix[self.sequence[-1]][self.sequence[0]]

        return total


def tour_aleatoire(n: int) -> list[int]:
    tour = list(range(n))
    random.shuffle(tour)

    return tour
