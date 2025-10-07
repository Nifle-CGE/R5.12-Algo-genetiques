from matplotlib.animation import FuncAnimation

from croiser import *
from genetique import *
from muter import *
from selectionner import *
from tour import *
from villes import *

SELECTIONNEURS = (selection_moitie, selection_tournoi, selection_roulette, selection_uniforme)
CROISEURS = (croiser_ordre, croiser_cycle, croiser_ordre_modifie)
MUTATEURS = (muter_echange,)


def comparatif_methodes(villes, taille_population, temps_dexecution, proba_mutation, montrer_evolution):
    results = []
    print("\nComparaison des méthodes génétiques :\n")

    for s in SELECTIONNEURS:
        for c in CROISEURS:
            for m in MUTATEURS:
                print(f"Test avec {s.__name__}, {c.__name__}, {m.__name__}", end="")
                tour, score, generations, evolution = algorithme_genetique(
                    villes,
                    taille_population=taille_population,
                    temps_dexecution=temps_dexecution,
                    proba_mutation=proba_mutation,
                    selectionner=lambda villes, population: s(villes, population, n=len(population) // 2),
                    croiser=c,
                    muter=m,
                    montrer_evolution=montrer_evolution
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


def afficher_tours(villes, evolution):
    x = [ville[0] for ville in villes]
    y = [ville[1] for ville in villes]

    fig = plt.figure(3, figsize=(8, 8))

    axis = plt.axes(xlim=(0, 1), ylim=(0, 1))

    tour_line, = axis.plot([], [], color='red')

    def init():
        tour_line.set_data([], [])
        return tour_line,

    def update(frame):
        tour, _ = evolution[frame]
        tour_x = [villes[i][0] for i in tour] + [villes[tour[0]][0]]
        tour_y = [villes[i][1] for i in tour] + [villes[tour[0]][1]]
        tour_line.set_data(tour_x, tour_y)
        plt.title(f"Génération {frame + 1} - Distance totale: {distance_totale(villes, tour):.2f}")
        return tour_line,

    ani = FuncAnimation(fig, update, frames=len(evolution), init_func=init, blit=True, repeat=False)

    print("Animation créée, sauvegarde en cours...")
    ani.save(f"./images/evolution_{int(time.time())}.mp4", writer='ffmpeg', fps=30)


def afficher_evolution(evolution):
    distances = [score for _, score in evolution]
    fitness = [1 / score for _, score in evolution]
    plt.figure(1, figsize=(10, 5))
    plt.plot(distances, color='blue')
    plt.title("Évolution de la distance totale au fil des générations")
    plt.xlabel("Génération")
    plt.ylabel("Distance totale")
    plt.grid()

    plt.figure(2, figsize=(10, 5))
    plt.plot(fitness, color='green')
    plt.title("Évolution du fitness au fil des générations")
    plt.xlabel("Génération")
    plt.ylabel("Fitness (1 / Distance totale)")
    plt.grid()
    plt.show()


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

    taille_population = demander_type("Taille de la population", int, default=200)
    temps_dexecution = demander_type("Temps d'exécution (secondes)", float, default=10.0)
    proba_mutation = demander_type("Probabilité de mutation (0.0 à 1.0)", float, default=0.01)

    print("Voulez-vous voir des stats d'évolution après l'exécution ?")
    montrer_evolution = demander(["Oui", "Non"], default=0) == "Oui"

    options_mode_genetique = ["Exécution unique", "Comparaison des méthodes"]
    mode_genetique = demander(options_mode_genetique, default=0)

    if mode_genetique == "Comparaison des méthodes":
        comparatif_methodes(villes, taille_population, temps_dexecution, proba_mutation, montrer_evolution)
    else:
        methode_selection = demander(list(map(lambda x: x.__name__, SELECTIONNEURS)), default=0)
        methode_croisement = demander(list(map(lambda x: x.__name__, CROISEURS)), default=0)
        methode_mutation = demander(list(map(lambda x: x.__name__, MUTATEURS)), default=0)

        tour, score, generations, evolution = algorithme_genetique(
            villes,
            taille_population=taille_population,
            temps_dexecution=temps_dexecution,
            proba_mutation=proba_mutation,
            selectionner=lambda villes, population: globals()[methode_selection](villes, population, n=len(population) // 2),
            croiser=globals()[methode_croisement],
            muter=globals()[methode_mutation],
            montrer_evolution=montrer_evolution
        )

        print(f"\nRésultat final après {generations} générations :")
        print(f"Meilleure distance totale = {score}\n")

        while True:
            analyse = demander(["Afficher l'évolution des tours", "Afficher le graphique de l'évolution", "Quitter"], default=2)
            if analyse == "Afficher l'évolution des tours":
                afficher_tours(villes, evolution)
            elif analyse == "Afficher le graphique de l'évolution":
                afficher_evolution(evolution)
            else:
                break


if __name__ == "__main__":
    main()
