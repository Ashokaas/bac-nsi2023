# EXERCICE 1

def moyenne(liste:list):
    if len(liste) == 0:
        return "La liste est vide"
    notes = 0
    coef = 0
    for note in liste:
        notes += note[0] * note[1]
        coef += note[1]
        
    if coef == 0:
        return None
    else:
        return notes / coef
    
print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))


# EXERCICE 2

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],  
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],  
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],  
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],  
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] 
 
def affiche(dessin): 
    ''' affichage d'une grille : les 1 sont représentés par  
        des " *" , les 0 par deux espaces "  ". 
        La valeur "" donnée au paramètre end permet de ne pas avoir    
        de saut de ligne.''' 
    for ligne in dessin: 
        for col in ligne: 
            if col == 1: 
                print(" *", end= "") 
            else: 
                print("  ", end= "") 
        print() 
          
def zoomListe(liste_depart, k): 
    '''renvoie une liste contenant k fois chaque  
       élément de liste_depart''' 
    liste_zoom = [] 
    for elt in liste_depart : 
        for i in range(k): 
            liste_zoom.append(elt)
    return liste_zoom 
 
def zoomDessin(grille, k): 
    '''renvoie une grille où les lignes sont zoomées k fois  
       ET répétées k fois''' 
    grille_zoom = [] 
    for elt in grille: 
        liste_zoom = zoomListe(elt, k) 
        for i in range(k): 
            grille_zoom.append(liste_zoom) 
    return grille_zoom
 
affiche(zoomDessin(coeur, 3))
 
