# from classe_compte import *
# from classe_user import *
# from classe_premium import *

# # popo = User("Bro","bro")
# # popo_pre = premium("boro", "1")
# # popo_pre.creer_compte(2000)
# # popo.creer_compte(1000)
# # liste_user = [popo, popo_pre]

# def creation():
#     input()
#     a = User("a","a")
#     b = premium("b", "b")
#     b.creer_compte(2000)
#     a.creer_compte(1000)
#     liste_user = [a, b]
#     choix_user = input("Etes vous un Nouvel utilisateur ou client ? Nouveaux (n) - Client (c)\n")

#     if choix_user == "n":
#         types = input("Veuillez choisir votre type de compte : Classique (cla) - Premium (pre)\t\n") 
#         if types == "cla":
#             print("Création d'un compte classique")
#             nom = input("Quel est votre nom ?\t\n")
#             mdp = input("Veuillez saisir un mot de passse\t\n")
#             montant = int(input("De combien souhaitez vous créditer votre compte?\t\n"))
#             utilisateur = User(nom ,mdp )
#             liste_user.append(utilisateur)
#             utilisateur.creer_compte(montant)
#             utilisateur.afficher_info()
            
#         elif types == "pre":
#             print("Création d'un compte premium")
#             nom = input("Quel est votre nom ?\t\n")
#             mdp = input("Veuillez saisir un mot de passse\t\n")
#             montant = int(input("De combien souhaitez vous créditer votre compte?\t\n"))
#             utilisateur = premium(nom ,mdp )
#             liste_user.append(utilisateur)
#             utilisateur.creer_compte(montant)
#             utilisateur.afficher_info()

#         else:
#             print("Veuillez répondre par (cla) pour un compte classique ou (pre) pour un compte premium")

#         while True:
#                 nouveau = input("Créer un autres compte bancaire ? Oui : (o) - Non : (n)\n")
#                 if nouveau == "o":
#                     return creation()
#                 elif nouveau == "n":
#                     print("La banque vous remercie pour votre considération.")
#                     break 

# creation()