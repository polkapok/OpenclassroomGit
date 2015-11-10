# -*-coding:utf-8 -*

"""fichier testant la fonction importée afficher_flottant()
depuis le fichier fonctions_diverses"""

import os

from fonctions_diverses import afficher_flottant

# On attend que l'utilisateur saisisse le nombre flottant qu'il désire tester
flotteur = float(input("Saisissez un nombre flottant : ")) 

# test de la fonction afficher_flottant
test = afficher_flottant(flotteur)

# affichage du résultat
print(test)

# attente pour visualisation sur la console
os.system("pause")

