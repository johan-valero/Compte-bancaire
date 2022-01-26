# Implémenter la classe Banque. 
# Les utilisateurs seront enregistré dans un attribut de type liste de la classe.
# Lors d'un emprunt, l'argent versé sur le compte de l'utilisateur viendra d'un attribut pecule de la classe banque.

from class_user import * 
from class_account import * 
from class_premium import *

class Banque:    
    
    def __init__(self):
        self.clients = []
        # self.pret = 0
        # self.pecule = pecule


    # def ajouter_client(self,client):
    #     self.ajouter_client()
    #     self.clients.append(client)
        
    def preter(self,client):
        client.compte.crediter(self.pecule)


        # self.  .Crediter(montant_pret)
        # self.  .pret += montant_pret



