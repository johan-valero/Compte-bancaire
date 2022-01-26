# Implémenter la classe Banque. 
# Les utilisateurs seront enregistré dans un attribut de type liste de la classe.
# Lors d'un emprunt, l'argent versé sur le compte de l'utilisateur viendra d'un attribut pecule de la classe banque.

from class_user import * 
from class_Compte import * 
from class_Premium import *

class Banque:    
    
    def __init__(self, pecule):
        self.clients = []
        self.pecule = pecule


    def ajouter_client(self,client):
        self.clients.append(client)
        
    def preter(self,client):
        client.compte.Crediter(self.pecule)

    def trouver_client(self,nom):
        for client in self.clients:
            if client.nom == nom:
                return client
        
        return None

    

        # self.  .Crediter(montant_pret)
        # self.  .pret += montant_pret



