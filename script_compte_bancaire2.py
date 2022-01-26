from classe_compte import *
from classe_user import *
from classe_premium import *

print("===========================")
print("Bienvenue sur la banque Leo")
print("===========================")

popo = User("Bro","bro")
popo_pre = premium("boro", "1")
popo_pre.creer_compte(2000)
popo.creer_compte(1000)
liste_user = [popo, popo_pre]

choix_user = input("Etes vous un Nouvel utilisateur ou client ? Nouveaux (n) - Client (c)\n")

if choix_user == "n":
    types = input("Veuillez choisir votre type de compte : Classique (cla) - Premium (Pre)\t\n") 
    if types == "cla":
        print("Création d'un compte classique")
        nom = input("Quel est votre nom ?\t\n")
        mdp = input("Veuillez saisir un mot de passse\t\n")
        montant = int(input("De combien souhaitez vous créditer votre compte?\t\n"))
        utilisateur = User(nom ,mdp )
        liste_user.append(utilisateur)
        utilisateur.creer_compte(montant)
        utilisateur.afficher_info()
        
    elif types == "pre":
        print("Création d'un compte premium")
        nom = input("Quel est votre nom ?\t\n")
        mdp = input("Veuillez saisir un mot de passse\t\n")
        montant = int(input("De combien souhaitez vous créditer votre compte?\t\n"))
        utilisateur = premium(nom ,mdp )
        liste_user.append(utilisateur)
        utilisateur.creer_compte(montant)
        utilisateur.afficher_info()

    else:
        print("Veuillez répondre par (cla) pour un compte classique ou (pre) pour un compte premium")

elif choix_user == "c":
        print("Connexion")
        # verif_login = False
        while True:
            login_user = input("Veuillez entrer votre nom d'utilisateur\n")    
            for i in liste_user:
                if login_user == i.nom:
                        login_mdp = input("Veuillez entrer votre mot de passe\n")
                        if login_mdp == i.mdp:    
                            print("Connecté")                        
                            # print("Ce compte est il premium ? : " + str(isinstance(i, premium)))                                    
                            if isinstance(i,premium) == True:              
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
                                    break                                    
                            elif isinstance(i,premium) == False:    
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
                                            break
            # verif_login = True 
            # if not verif_login:
            #     print("Utilisateur ou mot de passe incorrect")                   

            #         else:
            #             print("Mot de passe incorrect\n ")                    
            # else:
            #     print("Nom d'utilisateur inconnu ou incorrect\n")
    


# verif_login = False
# for i in User:
#     if i.nom == login_mdp:

#     verif_login = True

# if not in verif_login: 
#     print("Utilisateur ou mot de passe incorrect")        
            




    
  










