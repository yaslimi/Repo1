def per(n):
    """
    Cette fonction à pour objet de multiplier les chiffres d'un nombre entre eux 
    et d'afficher le rang à partir duquel le produit devient nul.
    
    Entrée:
        Le nombre 
         
    Sortie:
        Les differents produits des chiffres jusqu'à0
    
    """
    
    #### Si la longueur du chiffre vaut 1 alors 
    if len(str(n))==1:
        print(n) ### On affiche le chiffre
        return "Fin du jeu" #### C'est la fin du jeu
        
    #### On définie une liste qui retourne chacun des élements du nombre données et le stocke dans une liste  
    liste = [int(j) for j in str(n)] #### Ie par exemple 1,5,5,7,5...52 
    len(liste)
    
    resultat = 1
### Pour chaque élement de la liste, on multiplie les élements entre eux.
    for idx, a in enumerate(liste):
        resultat = resultat * a #### On multiplie l'élémeent de la liste par le précédent

    #### On affiche les résultats:
    print(resultat)
        
    ##### Par itération, on relance la même fonction
    per(resultat)
    
#     if len(resultat)==1:
#         break



per(9942)

per(277777788888899)