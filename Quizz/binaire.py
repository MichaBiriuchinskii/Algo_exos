##############################################
#Tâche
##############################################
# Ecrire une fonction qui prend en paramètre une string (ne contenant que des 0 et des 1) et qui retourne la valeur de cette string interprétée comme un nombre écrit en base 2.

##############################################
#Solution
##############################################

 def valeur(s):
  val = 0
  for i in range(len(s)):
      val += 2**i if s[len(s) - (i+1)] == '1' else 0
  return val

print(valeur("1001"))
