# EXERCICE 1

def indices_maxi(tab:list):
    # Le tableau est vide
    if len(tab) == 0:
        return "Le tableau est vide"    
    
    resultat = {"max": tab[0], "indices": []}

    for val in range(len(tab)):
        if type(tab[val]) != int and type(tab[val]) != float:
            return "Le tableau ne contient pas que des nombres"
        else:
            if tab[val] == resultat["max"]:
                resultat["indices"].append(val)
            elif tab[val] > resultat["max"]:
                resultat["max"], resultat["indices"] = tab[val], [val]
                
    return (resultat["max"], resultat["indices"])

print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))


# EXERCICE 2

def positif(pile): 
    pile_1 = list(pile) 
    pile_2 = [] 
    while pile_1 != []: 
        x = pile_1.pop() 
        if x >= 0: 
            pile_2.append(x) 
    while pile_2 != []: 
        x = pile_2.pop() 
        pile_1.append(x) 
    return pile_1

print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positif([-2]))