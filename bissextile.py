# -*-coding:utf-8 -*

### Programme testant si une année, saisie par l'utilisateur, est bissextile ou non ###


# On importe le module os qui dispose de variables 
# et de fonctions utiles pour dialoguer avec votre 
# système d'exploitation
import os


# On attend que l'utilisateur fournisse l'année qu'il désire tester
annee = input("Saisissez une année : ") 


# On essaye de convertir l'année en entier
# Risque d'erreur si l'utilisateur n'a pas saisi un nombre
try: 
        annee = int(annee) 
except:
        print("Erreur lors de la conversion de l'année.")


# Condition réelle qui détermine bien si oui ou non l'année est bissextile
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")


# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
