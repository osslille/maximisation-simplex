import numpy as np

# Fonction de vérification de la fin de l'évaluation
def verif_fin(tab):
    for i in range(2,7):
        if tab[i] < 0:
            return True
    return False

x = [-1,-1]
y = [-1,-1]
valX = 0
valY = 0
iterations = 0

Z = [int(x) for x in input("Coefficients de l'équation à maximiser (coeff1/coeff2): ").split("/")]

contrainte1 = [int(x) for x in input("Première contrainte (coeff1/coeff2/valeur): ").split("/")]

contrainte2 = [int(x) for x in input("Deuxième contrainte (coeff1/coeff2/valeur): ").split("/")]

contrainte3 = [int(x) for x in input("Troisième contrainte (coeff1/coeff2/valeur): ").split("/")]

# Déclaration du tableau contenant les coefficients de l'équation de base et des contraintes
tableau = np.array([
[0,0,Z[0],Z[1],0,0,0],
[0,contrainte1[2],contrainte1[0],contrainte1[1],1,0,0],
[0,contrainte2[2],contrainte2[0],contrainte2[1],0,1,0],
[0,contrainte3[2],contrainte3[0],contrainte3[1],0,0,1],
[0,0,(-1*Z[0]),(-1*Z[1]),0,0,0]
], dtype = float)

tempTab = np.array([],dtype = float)

print(tableau)


# Boucle qui s'exécute tant qu'il y a encore des itérations possibles
while verif_fin(tableau[4]):
    iterations = iterations + 1
    valeurPivot = 0
    # Réinitialisation du tableau temporaire
    tempTab = np.empty(shape = (0,0))

    # Par défaut, on considère que la colonne pivot est la première
    colonnePivot = 2

    # Puis on parcourt toutes les colonnes dans Z pour trouver celle dont le coefficient est le plus petit
    for i in range(3,7):
        if tableau[4][i] < tableau[4][colonnePivot]:
            colonnePivot = i

    print("colonnePivot it1: " + str(colonnePivot))

    # Par défaut, on considère que la ligne pivot est la première
    lignePivot = 1

    # Puis on parcourt toutes les lignes pour trouver:
    # MIN {valeur de base de la ligne / coeff dans colonne pivot}
    for i in range(1,4):
        # Comme on ignore les valeurs négative ou nulles, on teste et on utilise le mot-clef continue de Python pour sauter les lignes concernées
        if (tableau[i][colonnePivot] < 0):
            lignePivot = i + 1
            continue
        if (tableau[i][1]/tableau[i][colonnePivot] < tableau[lignePivot][1]/tableau[lignePivot][colonnePivot]):
            lignePivot = i

    print("lignePivot it1: " + str(lignePivot))

    # Notre pivot est la valeur de l'intersection entre la colonne pivot et la ligne pivot
    valeurPivot = tableau[lignePivot][colonnePivot]

    tempTab = np.append(tempTab,tableau[0][colonnePivot])

    # À l'aide du tableau temporaire, on recalcule les valeurs de la ligne pivot comme suit:
    # nouvelle valeur = ancienne valeur / pivot
    for i in range(1,7):
        tempTab = np.append(tempTab, [[(tableau[lignePivot][i]/valeurPivot)]])

    # Dans notre tableau, on remplace l'ancienne ligne pivot par la nouvelle
    tableau[lignePivot]=tempTab

    # Pour les autres lignes on utilise à nouveau tempTab en le remplissant comme suit:
    # nouvelle valeur = ancienne valeur - (ancienne valeur dans la colonne pivot x nouvelle valeur dans la ligne pivot)
    for i in range(1,5):
        if i != lignePivot:
            tempTab = np.empty(shape = (0,0))
            tempTab = np.append(tempTab,[0])
            for j in range(1,7):
                tempTab = np.append(tempTab,(tableau[i][j]-(tableau[i][colonnePivot] * tableau[lignePivot][j])))

            tableau[i] = tempTab

    print(tableau)

    if colonnePivot == 2:
        x = [lignePivot,1]

    if colonnePivot == 3:
        y = [lignePivot,1]

    valX = tableau[x[0]][x[1]]
    valY = tableau[y[0]][y[1]]

print("x = ",valX," , y = ",valY, " & MAX(Z) = ",tableau[4][1], " (résolu en ",iterations," itération(s))")