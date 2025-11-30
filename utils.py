import numpy as np


class Singleton(type):
    """Métaclasse qui force une seule instance par classe.

    L'appel de la classe retourne la même instance à chaque fois.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def get_distinct_random_indices(n: int, k: int) -> list[int]:
    """Retourne `k` indices distincts choisis aléatoirement dans 0..n-1."""

    if k > n:
        raise ValueError("k doit être inférieur ou égal à n pour des indices distincts.")

    indices = set()
    while len(indices) < k:
        indices.add(np.random.randint(0, n))

    return list(indices)
