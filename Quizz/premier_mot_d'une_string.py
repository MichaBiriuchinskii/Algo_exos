##############################################
#Tâche
##############################################
# Écrire une fonction premierm() qui prend en paramètre une string s et renvoie (par return) la sous-chaîne comprenant tous les premiers caractères de s jusqu’au premier espace (non compris). Si la string ne contient aucun espace, elle est retournée telle quelle. Exemples : premierm("Le bateau ivre") renvoie ’Le’ premierm("Lebateau ivre") renvoie ’Lebateau’ premierm("Le_bateau_ivre") renvoie ’Le_bateau_ivre’ premierm(" Le bateau ivre") renvoie ”

##############################################
#Solution
##############################################

def avant(s):
  f = ""
  for i in s: 
    if i != " ":
      f += i
    else:
      break
  return f

print(avant("Lebateau ivre"))
