import json
import random
from Types import Normal, Feu, Eau, Terre
from Pokedex import Pokedex
import ijson

class Pokedex:
    def __init__(self):
        self.pokedex_data = []

        with open('Pokédex.json', 'r') as f:
            pokedex_json = ijson.items(f, 'item')
            for pokemon in pokedex_json:
                self.pokedex_data.append(pokemon)

    def search_pokemon(self, name):
        # implementation of search method


pokedex = Pokedex()

def ajouter_pokemon(pokedex):
    print("Ajoutez un Pokémon:")
    nom = input("Nom: ")
    type_ = input("Type (Normal, Feu, Eau, Terre): ")
    defense = int(input("Défense: "))
    attaque = int(input("Attaque: "))
    vie = int(input("Vie: "))

    if type_ == "Normal":
        pokemon = Normal(nom, defense, attaque, vie)
    elif type_ == "Feu":
        pokemon = Feu(nom, defense, attaque, vie)
    elif type_ == "Eau":
        pokemon = Eau(nom, defense, attaque, vie)
    elif type_ == "Terre":
        pokemon = Terre(nom, defense, attaque, vie)
    else:
        print("Type de Pokémon non valide.")
        return

    pokedex.ajouter_pokemon(pokemon)
    print(f"{pokemon.get_nom()} a été ajouté à votre Pokédex!")

def lancer_combat(pokedex):
    print("Choisissez votre Pokémon:")
    for nom, infos in pokedex.pokedex.items():
        print(nom)

    choix = input("Entrez le nom du Pokémon que vous voulez utiliser: ")
    infos_pokemon1 = pokedex.get_pokemon(choix)
    if not infos_pokemon1:
        print("Ce Pokémon n'est pas dans votre Pokédex.")
        return

    if infos_pokemon1["type"] == "Normal":
        pokemon1 = Normal(choix, infos_pokemon1["defense"], infos_pokemon1["attaque"], infos_pokemon1["vie"])
    elif infos_pokemon1["type"] == "Feu":
        pokemon1 = Feu(choix, infos_pokemon1["defense"], infos_pokemon1["attaque"], infos_pokemon1["vie"])
    elif infos_pokemon1["type"] == "Eau":
        pokemon1 = Eau(choix, infos_pokemon1["defense"], infos_pokemon1["attaque"], infos_pokemon1["vie"])
    elif infos_pokemon1["type"] == "Terre":
        pokemon1 = Terre(choix, infos_pokemon1["defense"], infos_pokemon1["attaque"], infos_pokemon1["vie"])
    else:
        print("Type de Pokémon non valide.")
        return

    print("Choisir un adversaire aléatoire:")
    adversaire = random.choice(list(pokedex.pokedex.keys()))
    print(adversaire)
    infos_pokemon2 = pokedex.get_pokemon(adversaire)

    if infos_pokemon2["type"] == "Normal":
        pokemon2 = Normal(adversaire, infos_pokemon2["defense"], infos_pokemon2["attaque"], infos_pokemon2["vie"])
    elif infos_pokemon2["type"] == "Feu":
        pokemon2 = Feu(adversaire, infos_pokemon2["defense"], infos_pokemon2["attaque"], infos_pokemon2["vie"])
    elif infos_pokemon2["type"] == "Eau":
        pokemon2 = Eau(adversaire, infos_pokemon2["defense"], infos_pokemon2["attaque"], infos_pokemon2["vie"])
    elif infos_pokemon2["type"] == "Terre":
        pokemon2 = Terre(adversaire, infos_pokemon2["defense"], infos_pokemon2["attaque"], infos_pokemon2["vie"])
    else:
        print("Type de Pokémon non valide.")
        return


    #print("Choisir un adversaire aléatoire:")
    #adversaire = random.choice(list(pokedex.pokedex.keys()))
    #print(adversaire)
    #pokemon2 = pokedex.get_pokemon(adversaire)

    combat = Combat(pokemon1, pokemon2)
    combat.combat()
    print(f"Le vainqueur est {combat.nom_du_vainqueur()}!")


def main():
    pokedex = Pokedex()
    while True:
        print("\nMenu:")
        print("1. Ajouter un Pokémon")
        print("2. Accéder à votre Pokédex")
        print("3. Lancer une partie")
        print("4. Quitter")
        choix = int(input("Choisissez une option: "))

        if choix == 1:
            ajouter_pokemon(pokedex)
        elif choix == 2:
            print(pokedex.afficher_pokedex())
        elif choix == 3:
            lancer_combat(pokedex)
        elif choix == 4:
            break
        else:
            print("Option non valide.")

if __name__ == "__main__":
    main()
