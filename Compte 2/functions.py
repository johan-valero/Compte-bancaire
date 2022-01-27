from http import client
from class_Compte import *
from class_user import *
from class_Premium import *
from class_Banque import *
# from script import *
 
def types_de_compte(banque):
    types = input("Veuillez choisir un type de compte : Classique (cla) - Premium (pre)\t\n")
    if types == "cla":
        print("Création d'un compte classique")
        nom = input("Quel est votre nom ?\t\n")
        mdp = input("Veuillez saisir un mot de passse\t\n")
        montant = int(input("De combien souhaitez vous créditer votre compte pour l'ouverture ?\t\n"))
        utilisateur = User(nom, mdp)

        print("=========================")
        print("Creation de compte validé")
        print("=========================")
        banque.ajouter_client(utilisateur)
        utilisateur.creer_compte(montant)
        utilisateur.afficher_info()
        print("Appuyer sur ENTREE pour revenir au menu principal")

    elif types == "pre":
        print("Création d'un compte premium")
        nom = input("Quel est votre nom ?\t\n")
        mdp = input("Veuillez saisir un mot de passse\t\n")
        montant = int(input("De combien souhaitez vous créditer votre compte?\t\n"))
        utilisateur = Premium(nom, mdp)

        print("=========================")
        print("Creation de compte validé")
        print("=========================")
        banque.ajouter_client(utilisateur)
        utilisateur.creer_compte(montant)
        utilisateur.afficher_info()
        print("Appuyer sur ENTREE pour revenir au menu principal")
    else:
        print("Veuillez répondre par (cla) pour un compte classique ou (pre) pour un compte premium")

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
    return client

def Verification_premium(client,banque):
            if isinstance(client, Premium) == True:
                while True:  # ------------WHILE 2  ------------
                    choix_premium = int(input(
                        "Que voulez vous faire ?\n\t"
                        "1: visualiser votre solde\n\t"
                        "2: créditer votre compte\n\t"
                        "3: débiter votre compte\n\t"
                        "4: Afficher  les crédits éffectués\n\t"
                        "5: Faire un emprunt\n\t"
                        "6: Quitter\n\t"
                    ))

                    if choix_premium == 1:
                        client.compte.Afficher()
                    elif choix_premium == 2:
                        montant = int(
                            input("De combien souhaitez vous créditer ?\n"))
                        client.compte.Crediter(montant)
                    elif choix_premium == 3:
                        mont = int(
                            input("De combien souhaitez vous débiter ?\n"))
                        client.compte.Debiter(mont)
                    elif choix_premium == 4:
                        client.compte.AfficherCredits()
                    elif choix_premium == 5:
                        emp = int(input("Combien souhaitez vous emprunter ?\n"))
                        banque.preter(client,emp)
                    else:
                        print("Au revoir")
                        break
            elif isinstance(client, Premium) == False:
                while True:  # ------------gestion erreur sur les options du classique ------------
                    choix_classique = int(input("Que voulez vous faire ?\n\t"
                                                "1: visualiser votre solde\n\t"
                                                "2: créditer votre compte\n\t"
                                                "3: débiter votre compte\n\t"
                                                "4: Afficher  les crédits éffectués\n\t"
                                                "5: Quitter\n\t"))

                    if choix_classique == 1:
                        client.compte.Afficher()
                    elif choix_classique == 2:
                        montant = int(input("De combien souhaitez vous créditer ?\n"))
                        client.compte.Crediter(montant)
                    elif choix_classique == 3:
                        mont = int(input("De combien souhaitez vous débiter ?\n"))
                        client.compte.Debiter(mont)
                    elif choix_classique == 4:
                        client.compte.AfficherCredits()
                    else:
                        print("Au revoir")
                        continuer = False
                        break
