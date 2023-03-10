# EXERCICE 1

def verifie(tableau:list):
    # Le tableau est vide
    if len(tableau) == 0:
        return "Le tableau est vide"
    # Le tableau n'a qu'un élément
    if len(tableau) == 1:
        return True
    else:
        for val in range(1, len(tableau)):
            if type(tableau[val]) != int and type(tableau[val]) != float:
                return "Le tableau ne contient pas que des nombres"
            if tableau[val] < tableau[val -1]:
                return False
        return True
                
print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))


# EXERCICE 2

def depouille(urne): 
    resultat = {}
    for bulletin in urne: 
        if bulletin in resultat.keys(): 
            resultat[bulletin] = resultat[bulletin] + 1 
        else: 
            resultat[bulletin] = 1
    return resultat 
 
 
def vainqueur(election): 
    vainqueur = '' 
    nmax = 0 
    for candidat in election: 
        if election[candidat] > nmax : 
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax] 
    return liste_finale

urne = ['A', 'A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
depouillage = depouille(urne)
print(vainqueur(depouillage))