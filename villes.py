import math
import random
import time

import matplotlib.pyplot as plt
from point2d import Point2D

from utils import Singleton


class Villes(metaclass=Singleton):
    def __init__(self, villes: list[Point2D] | None = None):
        if villes is not None:
            self.villes = villes


def villes_aleatoires(n: int, seed=None):
    if seed is not None:
        random.seed(seed)

    villes = []
    for _ in range(n):
        villes.append(Point2D(x=random.random(), y=random.random()))

    Villes(villes)


def villes_en_cercle(n: int):
    villes = []
    radius = 0.5
    for i in range(n):
        angle = 2 * math.pi * i / n
        villes.append(Point2D(x=0.5 + radius * math.cos(angle), y=0.5 + radius * math.sin(angle)))

    Villes(villes)


def villes_defi_250():  # a battre 12.130 en 2mn avec 5 * nb_villes population
    villes = []
    with open("defi250.csv", "r") as f:
        data = f.readlines()

    for line in data[1:]:
        x, y = map(float, line.strip().split(";"))
        villes.append(Point2D(x=x, y=y))

    Villes(villes)


def distance(ville1: Point2D, ville2: Point2D) -> float:
    vector = ville1 - ville2
    return vector.r
