from classe_compte import *
from classe_user import *
from classe_premium import *

print("===========================")
print("Bienvenue sur la banque Leo")
print("===========================")

a = User("a","a")
b = premium("b", "b")
b.creer_compte(2000)
a.creer_compte(1000)
liste_user = [a, b]

while True:
    input()
    choix_user = input("Etes vous un nouvel utilisateur ou un client ? Nouveaux (n) - Client (c)\n")
    if choix_user == "n":
            types = input("Veuillez choisir votre type de compte : Classique (cla) - Premium (pre)\t\n") 
            if types == "cla":
                print("Création d'un compte classique")
                nom = input("Quel est votre nom ?\t\n")
                mdp = input("Veuillez saisir un mot de passse\t\n")
                montant = int(input("De combien souhaitez vous créditer votre compte?\t\n"))
                utilisateur = User(nom ,mdp )
                liste_user.append(utilisateur)
                utilisateur.creer_compte(montant)
                print("=========================")
                print("Creation de compte validé")
                print("=========================")
                utilisateur.afficher_info()   
                
            elif types == "pre":
                print("Création d'un compte premium")
                nom = input("Quel est votre nom ?\t\n")
                mdp = input("Veuillez saisir un mot de passse\t\n")
                montant = int(input("De combien souhaitez vous créditer votre compte?\t\n"))
                utilisateur = premium(nom ,mdp )
                liste_user.append(utilisateur)
                utilisateur.creer_compte(montant)
                print("=========================")
                print("Creation de compte validé")
                print("=========================")
                utilisateur.afficher_info()

            else:
                print("Veuillez répondre par (cla) pour un compte classique ou (pre) pour un compte premium")
    
    elif choix_user == "c":
        print("Connexion")
        continuer = True
        while continuer:   #------------gestion erreur sur le d'utilisateur------------
            login_user = input("Veuillez entrer votre nom d'utilisateur\n")   
            for i in liste_user:
                if login_user == i.nom:
                        login_mdp = input("Veuillez entrer votre mot de passe\n")
                        if login_mdp == i.mdp:    
                            print("Connecté")                                                        
                            if isinstance(i,premium) == True:
                                while True:  #------------gestion erreur sur les options du premium ------------          
                                    choix_premium = int(input("Que voulez vous faire ?\n\t"
                                                    "1: visualiser votre solde\n\t"
                                                    "2: créditer votre compte\n\t"
                                                    "3: débiter votre compte\n\t"
                                                    "4: Afficher  les crédits éffectués\n\t"
                                                    "5: Faire un emprunt\n\t"
                                                    "6: Quitter\n\t"))

                                    if choix_premium == 1:
                                        i.compte.Afficher()
                                    elif choix_premium == 2:
                                        montant = int(input("de combien souhaitez vous créditer ?\n"))
                                        i.compte.Crediter(montant)
                                    elif choix_premium == 3:
                                        mont= int(input("de combien souhaitez vous débiter ?\n"))
                                        i.compte.Debiter(mont)
                                    elif choix_premium == 4:
                                        i.compte.AfficherCredits()
                                    elif choix_premium == 5:
                                        emp = int(input("Quel montant suhaitez vous emprunter ?\n")) 
                                        i.emprunter(emp)
                                    else:
                                        print("Au revoir")
                                        continuer = False                                    
                                        break
                            elif isinstance(i,premium) == False:
                                while True:    #------------gestion erreur sur les options du classique ------------  
                                        choix_classique = int(input("Que voulez vous faire ?\n\t"
                                                        "1: visualiser votre solde\n\t"
                                                        "2: créditer votre compte\n\t"
                                                        "3: débiter votre compte\n\t"
                                                        "4: Afficher  les crédits éffectués\n\t"                           
                                                        "5: Quitter\n\t"))

                                        if choix_classique == 1:
                                            i.compte.Afficher()
                                        elif choix_classique == 2:
                                            montant = int(input("de combien souhaitez vous créditer ?\n"))
                                            i.compte.Crediter(montant)
                                        elif choix_classique == 3:
                                            mont= int(input("de combien souhaitez vous débiter ?\n"))
                                            i.compte.Debiter(mont)
                                        elif choix_classique == 4:
                                            i.compte.AfficherCredits()
                                        else:
                                            print("Au revoir")
                                            continuer = False
                                            break
                                        
                        else: #------------fin gestion sur mdp et utlisateur  ------------
                            print("Mot de passe ou utilisateur incorrect\n ")                           
    else:
        print("Veuillez répondre par c ou n \n") #------------fin gestion sur nouveau ou client  ------------
