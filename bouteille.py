class Bouteille:
    def __init__(self, nom, quantite_max):
        self.nom = nom
        self.quantite_max = quantite_max
        self.quantite_courante = 0
        self.ouverte = True

    def fermer(self):
        if not self.ouverte:
            print(f'La bouteille {self.nom} est déjà fermée')
        else:
            self.ouverte = False
            print(f'La bouteille {self.nom} a été fermée')

    def ouvrir(self):
        if self.ouverte:
            print(f'La bouteille {self.nom} est déjà ouverte')
        else:
            self.ouverte = True
            print(f'La bouteille {self.nom} a été ouverte')

    def quantite(self):
        print(f'La bouteille {self.nom} possède {self.quantite_courante} sur {self.quantite_max}')

    def remplir(self, quantite: int):
        if not self.ouverte:
            print("La bouteille est fermée, t'es un booléen ou quoi ?")
        else:
            if self.quantite_courante + quantite > self.quantite_max:
                print(f"La bouteille {self.nom} va déborder ! Abandon du remplissage.")
            else:
                print(f"La bouteille {self.nom}, a été remplie avec {quantite} quantite")
                self.quantite_courante = self.quantite_courante + quantite


if __name__ == "__main__":
    bouteille_alice = Bouteille("Bouteille d'Alice", 20)
    bouteille_bob = Bouteille("Bouteille de Bob", 10)
    bouteille_bob.remplir(quantite=5)
    bouteille_bob.fermer()
    bouteille_bob.ouvrir()
    bouteille_bob.remplir(quantite=5)
    bouteille_bob.remplir(quantite=5)



class Bouteille:
    def __init__(self, nom, quantite_max):
        self.nom = nom
        self.quantite_max = quantite_max
        self.quantite_courante = 0
        self.ouverte = True

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

