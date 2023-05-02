import json

class Pokemon:
    def __init__(self, nom, type_, defense, attaque, vie):
        self.__nom = nom
        self.type_ = type_
        self.defense = defense
        self.attaque = attaque
        self.__vie = vie

    def get_nom(self):
        return self.__nom

    def get_vie(self):
        return self.__vie

    def set_vie(self, vie):
        self.__vie = vie

    def afficher_infos(self):
        return f"{self.__nom} (Type: {self.type_}, Vie: {self.__vie}, Attaque: {self.attaque}, Défense: {self.defense})"

    def enregistrer_pokemon(self):
        try:
            with open("pokedex.json", "r") as file:
                pokedex = json.load(file)
        except FileNotFoundError:
            pokedex = {"pokemons": []}

        for pokemon in pokedex["pokemons"]:
            if self.get_nom() == pokemon["nom"]:
                return

        pokedex["pokemons"].append({
            "nom": self.__nom,
            "type": self.type_,
            "defense": self.defense,
            "attaque": self.attaque,
            "vie": self.__vie
        })

        with open("pokedex.json", "w") as file:
            json.dump(pokedex, file, indent=4)
