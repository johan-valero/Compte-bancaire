from class_account import * 

class User:
    def __init__(self,nom, mdp):
        self.nom = nom
        self.mdp = mdp
        self.compte = None

    def afficher_info(self):
        print(f"Le propriètaire du compte est {self.nom}.\n"
              f"Le mot de passe de votre compte est {self.mdp}.\n"
              f"Votre compte est {self.compte}.\n"
             )

    def creer_compte(self, montant):
        self.compte = Compte(self.nom)
        self.compte.Crediter(montant)
        