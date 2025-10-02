from unittest import result
from croiser import *
from genetique import *
from muter import *
from selectionner import *
from tour import *
from villes import *

SELECTIONNEURS = (selection_moitie, selection_tournoi, selection_roulette, selection_uniforme)
CROISEURS = (croiser_ordre, croiser_cycle, croiser_ordre_modifie)
MUTATEURS = (muter_echange,)


def comparatif_methodes(villes, taille_population, temps_dexecution, proba_mutation):
    results = []
    print("\nComparaison des méthodes génétiques :\n")
    
    for s in SELECTIONNEURS:
        for c in CROISEURS:
            for m in MUTATEURS:
                print(f"Test avec {s.__name__}, {c.__name__}, {m.__name__}", end="")
                tour, score, generations = algorithme_genetique(
                    villes,
                    taille_population=taille_population,
                    temps_dexecution=temps_dexecution,
                    proba_mutation=proba_mutation,
                    selectionner=lambda villes, population: s(villes, population, n=len(population) // 2),
                    croiser=c,
                    muter=m,
                    montrer_evolution=False
                )

                print(f" | Meilleure distance totale = {score} après {generations} générations")


def demander(options, default=None):
    print("Choisissez :")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    while True:
        try:
            if default is not None:
                choix = int(input(f"Entrez le numéro de votre choix (par défaut {default + 1}) : ") or default + 1) - 1
            else:
                choix = int(input("Entrez le numéro de votre choix : ")) - 1

            return options[choix]
        except (ValueError, IndexError):
            print("Choix invalide. Veuillez entrer un numéro valide.")


def demander_type(prompt, type_cast, default=None):
    while True:
        try:
            if default is not None:
                valeur = type_cast(input(f"{prompt} (par défaut {default}) : ") or default)
            else:
                valeur = type_cast(input(prompt))
            return valeur
        except ValueError:
            print(f"Entrée invalide. Veuillez entrer une valeur de type {type_cast.__name__}.")


def main():
    options_mode_villes = ["Villes aléatoires", "Villes en cercle", "Défi 250 villes"]
    mode_villes = demander(options_mode_villes, default=0)
    if mode_villes == "Villes aléatoires":
        n_villes = demander_type("Nombre de villes", int, default=30)
        villes = villes_aleatoires(n_villes)
    elif mode_villes == "Villes en cercle":
        n_villes = demander_type("Nombre de villes", int, default=30)
        villes = villes_en_cercle(n_villes)
    else:
        villes = villes_defi_250()

    options_mode_genetique = ["Exécution unique", "Comparaison des méthodes"]
    mode_genetique = demander(options_mode_genetique, default=0)

    taille_population = demander_type("Taille de la population", int, default=200)
    temps_dexecution = demander_type("Temps d'exécution (secondes)", float, default=10.0)
    proba_mutation = demander_type("Probabilité de mutation (0.0 à 1.0)", float, default=0.01)
    
    if mode_genetique == "Comparaison des méthodes":
        comparatif_methodes(villes, taille_population, temps_dexecution, proba_mutation)
    else:
        methode_selection = demander(list(map(lambda x: x.__name__, SELECTIONNEURS)), default=0)
        methode_croisement = demander(list(map(lambda x: x.__name__, CROISEURS)), default=0)
        methode_mutation = demander(list(map(lambda x: x.__name__, MUTATEURS)), default=0)

        tour, score, generations = algorithme_genetique(
            villes,
            taille_population=taille_population,
            temps_dexecution=temps_dexecution,
            proba_mutation=proba_mutation,
            selectionner=lambda villes, population: globals()[methode_selection](villes, population, n=len(population) // 2),
            croiser=globals()[methode_croisement],
            muter=globals()[methode_mutation],
            montrer_evolution=True
        )

        print(f"\nRésultat final après {generations} générations :")
        print(f"Meilleure distance totale = {score}")

        visualiser_villes(villes, tour)


if __name__ == "__main__":
    main()
