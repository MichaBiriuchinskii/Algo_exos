##############################################
#Tâche
##############################################
#Écrire une fonction qui prend en entrée (en paramètre) une liste de mots, et renvoie (par return) le nombre de mots qui sont plus longs que leur prédécesseur dans la liste.
#Seules fonctions prédéfinies utilisables : len(), range()

##############################################
#Solution
##############################################

def fonc(L):
  count = 0
  for i in range(len(L)-1):
    if len(L[i]) < len(L[i+1]):
      count += 1
  return count

L = ["mon", "beau", "navire"]
print(fonc(L))
