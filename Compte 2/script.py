from class_Compte import *
from class_user import *
from class_Premium import *
from class_Banque import *
from functions import *

print("===========================")
print("Bienvenue à la BANK")
print("===========================")
print("Apuyer sur ENTREE pour commencer")

banque = Banque(50000)
moi = Premium("Jesus", "1234")
moi.creer_compte(100000000)
banque.ajouter_client(moi)

while True:
    input()
    choix_user = input("Etes vous un nouvel utilisateur ou un client ? Nouveaux (n) - Client (c)\n")
    if choix_user == "n":
        print("Création de compte")
        types_de_compte(banque)      
    elif choix_user == "c":
        print("==================")
        print("Espace utilisateur")
        print("==================")
        client = authentification(banque)                              
        if client:
            print("Connecté")
            Verification_premium(client,banque)
    else:
        print("Veuillez répondre par c ou n \n")
