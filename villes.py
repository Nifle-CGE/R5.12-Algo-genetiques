import math
import random

import numpy as np

from utils import Singleton


class Villes(metaclass=Singleton):
    def __init__(self, villes: list[list[float]] | None = None):
        # Si une liste de villes est fournie, c'est que c'est la première
        # instanciation du singleton, donc on initialise les données.
        if villes is not None:
            self.villes = np.array(villes, dtype=float)
            # nombre de villes (nombre de lignes dans le tableau)
            self.n = np.size(villes, 0)
            # pré-calculer la matrice des distances pour accélérer les évaluations
            self.distance_matrix = self._compute_distance_matrix()

    def _compute_distance_matrix(self) -> np.ndarray:
        """Calcule la matrice symétrique des distances.

        La méthode remplit uniquement la moitié supérieure de la matrice et
        recopie la valeur symétrique pour éviter des calculs doublons.
        """
        distance_matrix = np.zeros((self.n, self.n), dtype=float)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # distance entre la i-ème et la j-ème ville
                dist = distance(self.villes[i], self.villes[j])
                distance_matrix[i][j] = dist
                distance_matrix[j][i] = dist

        return distance_matrix


def villes_aleatoires(n: int, seed=None):
    """Génère `n` villes aléatoires dans le carré [0,1] x [0,1].

    Si `seed` est fourni, il est utilisé pour initialiser le générateur
    pseudo-aléatoire afin d'obtenir des résultats reproductibles.
    """
    if seed is not None:
        random.seed(seed)

    villes = []
    for _ in range(n):
        # coordonnées x et y aléatoires dans [0, 1)
        villes.append([random.random(), random.random()])

    # Instancie le singleton Villes avec les nouvelles coordonnées
    Villes(villes)


def villes_en_cercle(n: int):
    """Place `n` villes régulièrement réparties sur un cercle centré en (0.5,0.5).

    Utile pour générer un cas géométrique simple (par ex. pour déboguer
    ou visualiser l'algorithme).
    """
    villes = []
    radius = 0.5
    for i in range(n):
        angle = 2 * math.pi * i / n
        villes.append([0.5 + radius * math.cos(angle), 0.5 + radius * math.sin(angle)])

    Villes(villes)


def villes_defi_250():
    """Charge les 250 villes du fichier `defi250.csv`.

    Le fichier est attendu avec un en-tête, et les coordonnées séparées par
    un point-virgule (`x;y`) sur chaque ligne suivante.
    """
    villes = []
    with open("defi250.csv", "r") as f:
        data = f.readlines()

    for line in data[1:]:
        x, y = map(float, line.strip().split(";"))
        villes.append([x, y])

    Villes(villes)


def distance(ville1, ville2) -> float:
    """Calcule la distance euclidienne entre deux villes.

    Les entrées `ville1` et `ville2` peuvent être des séquences indexables
    (ex : liste, tuple, np.array) contenant `[x, y]`.
    """
    return math.hypot((ville1[0] - ville2[0]), (ville1[1] - ville2[1]))
