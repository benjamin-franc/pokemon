import json
from pathlib import Path

class Pokedex:
    def __init__(self):
        self.pokedex = {}
        pokedex_path = Path.cwd() / 'pokedex.json'
        try:
            with open('Pokedex.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

                try:
                    self.pokedex = json.load(file)
                except json.JSONDecodeError:
                    print("Erreur lors de la lecture du fichier pokedex.json. Le fichier est peut-être vide ou corrompu.")
        except FileNotFoundError:
            with open(pokedex_path, 'w') as file:
                json.dump(self.pokedex, file)

    def charger_pokedex(self):
            pokedex_path = Path.cwd() / 'pokedex.json'
            try:
                with open(pokedex_path, "r") as f:
                    self.pokedex = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                    self.pokedex = {}

    def sauvegarder_pokedex(self):
        pokedex_path = Path.cwd() / 'pokedex.json'
        with open(pokedex_path, "w") as f:
            json.dump(self.pokedex, f, indent=4)

    def ajouter_pokemon(self, pokemon):
        if pokemon.get_nom() not in self.pokedex:
            self.pokedex[pokemon.get_nom()] = {
                "type": pokemon.type.nom,  # remplacer pokemon.type_ par pokemon.type.nom
                "defense": pokemon.defense,
                "attaque": pokemon.attaque,
                "vie": pokemon.get_vie(),
            }
            self.sauvegarder_pokedex()

    def afficher_pokedex(self):
        return "\n".join([f"{nom}: {infos}" for nom, infos in self.pokedex.items()])

    def get_nombre_pokemon(self):
        return len(self.pokedex)

    def get_pokemon(self, nom):
        if nom in self.pokedex:
            return self.pokedex[nom]
        return None

