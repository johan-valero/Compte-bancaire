from classe_user import * 
from classe_compte import * 

class premium(User):
    def __init__(self, nom ,mdp):
        super().__init__(nom, mdp)
        self.emprunt = 0

    def emprunter(self, credit):
        self.compte.Crediter(credit)
        self.emprunt += credit
        
# moi = premium("Leo", "broa")
# moi.emprunter(100)
# moi.afficher_info()


    