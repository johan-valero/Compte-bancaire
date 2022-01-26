import datetime

class Compte:
    banque = "BANK"

    def __init__(self, proprio):
        self.date_creation = str(datetime.date.today())
        self.proprietaire = proprio
        self.solde = 0
        self.debit = []
        self.credit = []

    def Crediter(self, montant):
        self.solde += montant
        self.credit.append(montant)
        print("{} : +{}€".format(self.date_creation,montant))
        self.Afficher()

    def Debiter(self, montant):
        if self.solde > montant:
            self.solde -= montant
            print("{} : -{}€".format(self.date_creation,montant))
            self.Afficher()
        else:
            print("Fond insuffisant")

    def Afficher(self):
        print("Solde : {}€".format(self.solde))

    def Resume(self):
        print("Le proprietaire du compte est {}. "
              "Le compte a été créé le {}. "
              "Il dispose de {}€. "
              "Il est hébergé à la banque {} ".format(self.proprietaire,
                                                      self.date_creation,
                                                      self.solde,
                                                      self.banque))

    def AfficherCredits(self):
        for i in self.credit:
            print(self.date_creation,":", i)