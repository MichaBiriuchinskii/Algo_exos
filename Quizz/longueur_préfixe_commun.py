##############################################
#Tâche
##############################################

#Écrire un programme python qui détermine la longueur du préfixe commun de deux chaînes de caractères. Exemples : pour s1 = "maison" et s2 = "masure", le résultat doit être 2 ;

##############################################
#Solution
##############################################

def longueur_prefixe_commun(s1,s2):
  c = 0
  i = 0
  while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
    c += 1
    i += 1
  return c

print(longueur_prefixe_commun("maison",  "mais"))
