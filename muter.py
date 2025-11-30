from tour import Tour
from utils import get_distinct_random_indices
from villes import Villes


def muter_echange(tour: Tour) -> None:
    """Mutation par échange : permute deux positions dans la séquence.

    - Choisit deux indices aléatoires i et j (distincts) et échange les villes
      correspondantes dans la permutation.
    - Met ensuite à jour la distance du tour.
    """
    tour_sequence = tour.sequence
    n = Villes().n
    i, j = get_distinct_random_indices(n, 2)

    # échange des deux villes
    tour_sequence[i], tour_sequence[j] = tour_sequence[j], tour_sequence[i]

    # sauvegarder la nouvelle séquence et recalculer la distance
    tour.sequence = tour_sequence
    tour.distance = tour.calculer_distance()


def muter_operateur_2_opt(tour: Tour) -> None:
    """Mutation par 2-opt : échange deux arêtes pour réduire la distance.

    - Choisit deux indices aléatoires i et j (distincts).
    - Si l'échange des arêtes (i, i+1) et (j, j+1) réduit la distance,
      effectue l'échange en inversant la sous-séquence entre i+1 et j.
    - Met ensuite à jour la distance du tour.
    """

    villes = Villes()
    n = villes.n
    i, j = get_distinct_random_indices(n, 2)

    distance_actuelle = villes.distance_matrix[tour.sequence[i]][tour.sequence[(i + 1) % n]] + villes.distance_matrix[tour.sequence[j]][tour.sequence[(j + 1) % n]]
    distance_nouvelle = villes.distance_matrix[tour.sequence[i]][tour.sequence[j]] + villes.distance_matrix[tour.sequence[(j + 1) % n]][tour.sequence[(i + 1) % n]]
    if distance_nouvelle < distance_actuelle:
        # effectuer le 2-opt
        tour_sequence = tour.sequence
        tour_sequence[(i + 1) % n], tour_sequence[j], tour_sequence[(j + 1) % n] = tour_sequence[j], tour_sequence[(j + 1) % n], tour_sequence[(i + 1) % n]

        # sauvegarder la nouvelle séquence et recalculer la distance
        tour.sequence = tour_sequence
        tour.distance = tour.calculer_distance()


def muter_insertion(tour: Tour) -> None:
    """Mutation par insertion : extrait une ville et la réinsère ailleurs.

    - Choisit deux indices aléatoires i et j (distincts).
    - Extrait la ville à l'indice i et l'insère avant l'indice j,
      en décalant les autres villes.
    - Met ensuite à jour la distance du tour.
    """

    tour_sequence = tour.sequence
    n = Villes().n
    i, j = get_distinct_random_indices(n, 2)

    # extraire la ville à l'indice i
    ville = tour_sequence.pop(i)
    # insérer la ville avant l'indice j
    tour_sequence.insert(j, ville)

    # sauvegarder la nouvelle séquence et recalculer la distance
    tour.sequence = tour_sequence
    tour.distance = tour.calculer_distance()
