from Pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self, nom, defense, attaque, vie):
        super().__init__(nom, "Normal", defense, attaque, vie)

class Feu(Pokemon):
    def __init__(self, nom, defense, attaque, vie):
        super().__init__(nom, "Feu", defense, attaque, vie)

class Eau(Pokemon):
    def __init__(self, nom, defense, attaque, vie):
        super().__init__(nom, "Eau", defense, attaque, vie)

class Terre(Pokemon):
    def __init__(self, nom, defense, attaque, vie):
        super().__init__(nom, "Terre", defense, attaque, vie)


