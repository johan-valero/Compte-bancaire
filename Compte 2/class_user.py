from class_account import * 

class User:
    def __init__(self,nom, mdp):
        self.nom = nom
        self.mdp = mdp
        self.compte = None

    def afficher_info(self):
            print(f"Compte n°{self.compte}.\n"
                  f"Propriètaire du compte :{self.nom}.\n"
                  f"Mot de passe :{self.mdp}.\n"
                 )

    def creer_compte(self, montant):
        self.compte = Compte(self.nom)
        self.compte.Crediter(montant)
        