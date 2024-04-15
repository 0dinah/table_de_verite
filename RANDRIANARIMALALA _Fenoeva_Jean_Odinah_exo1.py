def generer_table_verite(nombres_variables, fonction_logique, variables):
    table_verite = []
    for i in range(2 ** nombres_variables):
        combinaison = []
        for j in range(nombres_variables):
            combinaison.append((i >> j) & 1)
        resultat = eval(fonction_logique, dict(zip(variables, combinaison)))
        table_verite.append((combinaison, resultat))
    return table_verite

def afficher_formes_canoniques(table_verite, variables):
    mintermes = [combinaison for combinaison, resultat in table_verite if resultat]
    fonction_premiere_forme = []
    for minterme in mintermes:
        termes = []
        for i, valeur in enumerate(minterme):
            if valeur == 1:
                termes.append(variables[i])
            elif valeur == 0:
                termes.append(f"not {variables[i]}")
        fonction_premiere_forme.append("(" + " and ".join(termes) + ")")
    
    maxtermes = [combinaison for combinaison, resultat in table_verite if not resultat]
    fonction_deuxieme_forme = []
    for maxterme in maxtermes:
        termes = []
        for i, valeur in enumerate(maxterme):
            if valeur == 0:
                termes.append(variables[i])
            elif valeur == 1:
                termes.append(f"not {variables[i]}")
        fonction_deuxieme_forme.append("(" + " or ".join(termes) + ")")
    
    print("Première forme canonique de la fonction : ", " or ".join(fonction_premiere_forme))
    print("Deuxième forme canonique de la fonction : ", " and ".join(fonction_deuxieme_forme))

def principale():
    nombres_variables = int(input("Entrez le nombre de variables : "))
    variables = []
    for i in range(nombres_variables):
        nom_variable = input(f"Entrez le nom de la variable {i+1} : ")
        variables.append(nom_variable)
    fonction_logique = input("Entrez la fonction logique (en utilisant les noms des variables et les opérateurs logiques Python c'est à dire le ==>'and', ==>'not' et le ==>'or') : ")
    table_verite = generer_table_verite(nombres_variables, fonction_logique, variables)
    print("Table de vérité :")
    for combinaison, resultat in table_verite:
        print(combinaison, resultat)
    afficher_formes_canoniques(table_verite, variables)

principale()
