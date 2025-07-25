import random

def jouer_niveau(niveau, essais_max):
    print("\n" + "*" * 20)
    print(f"*** NIVEAU {niveau} ***")
    print("*" * 20)

    # Le nombre secret devient plus difficile à chaque niveau
    limite_max = 100  
    nombre_secret = random.randint(0, limite_max)
    essais = 0

    while essais < essais_max:
        try:
            nombre_entre = int(input(f"Devinez le nombre secret (entre 0 et {limite_max}) : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        essais += 1

        if nombre_entre == nombre_secret:
            print(" Bravo, vous avez trouvé le nombre secret !")
            return True  # Niveau réussi
        elif nombre_entre < nombre_secret:
            print("Trop petit !")
        else:
            print("Trop grand !")

        print(f"Il vous reste {essais_max - essais} essais.")

    # Si tous les essais sont épuisés
    print(f"❌ Vos essais sont épuisés. Le nombre secret était : {nombre_secret}")
    return False

def jeu():
    print("DEVINEZ LE NOMBRE MAGIQUE")
    print("=" * 30)

    niveau = 1
    essais_max = 10  # Premier niveau avec 10 essais

    while True:
        reussi = jouer_niveau(niveau, essais_max)

        if reussi:
            niveau += 1
            essais_max = max(3, essais_max - 1)  # Chaque niveau diminue les essais
            print(f"\n🚀 Vous passez au niveau {niveau} avec {essais_max} essais !")
        else:
            print("\n💀 Fin du jeu. Essayez encore !")
            break

# Lancer le jeu
jeu()