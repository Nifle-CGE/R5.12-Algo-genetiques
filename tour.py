import random

from villes import Villes


class Tour():
    """Objet représentant un parcours (tour) sur l'ensemble des villes.

    - `sequence` : liste d'entiers représentant l'ordre des villes
    - `distance` : distance totale parcourue par ce tour
    """

    def __init__(self, sequence: list[int]):
        self.sequence = sequence
        # calcul initial de la distance
        self.distance = self.calculer_distance()

    def calculer_distance(self) -> float:
        """Calcule la distance totale du tour en utilisant la matrice pré-calculée."""
        villes = Villes()
        total = 0.0
        # somme des distances entre positions consécutives
        for i in range(villes.n - 1):
            total += villes.distance_matrix[self.sequence[i]][self.sequence[i + 1]]

        # ajouter la distance du dernier au premier (boucle fermée)
        total += villes.distance_matrix[self.sequence[-1]][self.sequence[0]]

        return total


def tour_aleatoire(n: int) -> list[int]:
    """Génère une permutation aléatoire des indices 0..n-1 (tour aléatoire)."""
    tour = list(range(n))
    random.shuffle(tour)

    return tour
