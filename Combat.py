import random
from Types import Normal, Feu, Eau, Terre
from Pokedex import Pokedex
from Combat import Combat

class Combat:
    def __init__(self, joueur):
        self.joueur = joueur
        self.pokedex = Pokedex()
        self.adversaire = self._choix_adversaire(pokemon1.type_)
        self.tour = 1

    def _choix_adversaire(self, type_joueur):
        pokemons = [p for p in self.pokedex.pokedex.keys() if p != type_joueur]
        nom_pokemon = random.choice(pokemons)
        adversaire = getattr(__import__('Types', fromlist=[nom_pokemon]), nom_pokemon)()
    return adversaire


    def _tour_attaque(self, attaquant, defenseur):
        print(f"Tour {self.tour}")
        self.tour += 1

        if random.randint(0, 1) == 0:
            print(f"{attaquant.nom} rate son attaque.")
            return

        multipl = attaquant.type.multipl_defenseur(defenseur.type)

        print(f"{attaquant.nom} attaque {defenseur.nom}")
        print(f"{attaquant.nom} inflige {attaquant.attaque * multipl} dégâts")

        defenseur.enlever_vie(attaquant.attaque * multipl)

        if not defenseur.en_vie():
            print(f"{defenseur.nom} est KO")
            self._enregistrer_pokemon(self.adversaire.nom)
            return

        print(f"{defenseur.nom} a {defenseur.vie} points de vie restants")

    def _enregistrer_pokemon(self, nom_pokemon):
        if nom_pokemon not in self.pokedex.pokedex:
            pokemon = getattr(__import__('Types', fromlist=[nom_pokemon]), nom_pokemon)()
            self.pokedex.pokedex[nom_pokemon] = {
                "type": pokemon.type.nom,
                "defense": pokemon.defense,
                "attaque": pokemon.attaque,
                "vie": pokemon.vie
            }
            print(f"{nom_pokemon} a été ajouté à votre Pokédex !")
        else:
            print(f"{nom_pokemon} est déjà dans votre Pokédex.")

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

    combat = Combat(pokemon1, pokemon2)
    combat.combat()
    print(f"Le vainqueur est {combat.nom_du_vainqueur()}!")

