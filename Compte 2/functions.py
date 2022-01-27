from class_Compte import *
from class_user import *
from class_Premium import *
from class_Banque import *
from script import *

# def authentification():
#     banque = Banque
#     login_user = input("Veuillez entrer votre nom d'utilisateur\n")
#     client = banque.trouver_client(login_user) 
#     if client:
#         login_mdp = input("Veuillez entrer votre mot de passe\n")
#         client2 = banque.trouver_mdp(login_mdp)     

def authentification(banque):
    nom = input("Veuillez entrer votre nom d'utilisateur\n")
    mdp = input("Veuillez entrer votre mot de passe\n")
    client = banque.trouver_client(nom)

    if not client:
      print("Indentifiant ou mot de passe incorrect")
      return None
    
    if mdp != client.mdp:
      print("Indentifiant ou mot de passe incorrect")
      return None
    
    # si on arrive ici c'est que tout est ok
    return client

