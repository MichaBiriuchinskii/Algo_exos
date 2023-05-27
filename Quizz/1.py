##############################################
#Tâche
##############################################
# Ecrire un programme python qui, étant donnée une liste d’entiers stockée dans une variable (de nom L), affiche à l’écran la valeur minimale de cette liste.
# Fonctions prédéfinies utilisables : len() et range()
#Pour tester la réponse, on commence par générer une liste aléatoire d’entiers dans la cellule suivante, qu’on affiche à l’écran.

##############################################
#Solution
##############################################
# génération d'une liste d'entiers aléatoire
import random
Min = 1
Max = 99
N = 20
L = random.sample(range(Min, Max), N)
print(L)

# recherche du "champion"
best = L[0]
for i in range(len(L)):
if L[i] < best:
best = L[i]
print("L'entier le plus petit de la liste vaut %d." % best)
