from class_user import * 
from class_account import * 
from class_bank import * 

class premium(User):
    def __init__(self, nom ,mdp):
        super().__init__(nom, mdp)
        self.emprunt = 0

    def emprunter(self, credit):
        self.compte.Crediter(credit)
        self.emprunt += credit