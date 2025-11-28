import math
import random
import time

import matplotlib.pyplot as plt
import numpy as np

from utils import Singleton


class Villes(metaclass=Singleton):
    def __init__(self, villes: list[list[float]] | None = None):
        if villes is not None:
            self.villes = np.array(villes, dtype=float)
            self.n = np.size(villes, 0)
            self.distance_matrix = self._compute_distance_matrix()

    def _compute_distance_matrix(self) -> np.ndarray:
        distance_matrix = np.zeros((self.n, self.n), dtype=float)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                dist = distance(self.villes[i], self.villes[j])
                distance_matrix[i][j] = dist
                distance_matrix[j][i] = dist

        return distance_matrix


def villes_aleatoires(n: int, seed=None):
    if seed is not None:
        random.seed(seed)

    villes = []
    for _ in range(n):
        villes.append([random.random(), random.random()])

    Villes(villes)


def villes_en_cercle(n: int):
    villes = []
    radius = 0.5
    for i in range(n):
        angle = 2 * math.pi * i / n
        villes.append([0.5 + radius * math.cos(angle), 0.5 + radius * math.sin(angle)])

    Villes(villes)


def villes_defi_250():  # a battre 12.130 en 2mn avec 5 * nb_villes population
    villes = []
    with open("defi250.csv", "r") as f:
        data = f.readlines()

    for line in data[1:]:
        x, y = map(float, line.strip().split(";"))
        villes.append([x, y])

    Villes(villes)


def distance(ville1, ville2) -> float:
    return math.sqrt((ville1[0] - ville2[0]) ** 2 + (ville1[1] - ville2[1]) ** 2)
