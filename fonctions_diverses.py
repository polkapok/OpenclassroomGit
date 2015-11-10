# -*-coding:utf-8 -*

"""module affichant plusieurs fonctions"""

import os




def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
		
# test de la fonction table
if __name__ == "__main__":
    table(4)
    os.system("pause")
	

	
	

""""Cette fonction retourne la partie entière et le reste de entier / divise_par"""
def entier_reste(entier, divise_par):
	p_e = entier // divise_par
	reste = entier % divise_par
	#return p_e, reste
	print(p_e, reste)

# test de la fonction entier_reste
if __name__ == "__main__":
    entier_reste(25, 3)
    os.system("pause")

	
	
	

"""Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. 
La partie flottante doit avoir une longueur maximum de 3 caractères.
De plus, on va remplacer le point décimal par la virgule"""
def afficher_flottant(flottant):

    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])

