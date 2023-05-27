##############################################
#Tâche
##############################################
# Ecrire un algorithme en Python permettant de trier une liste selon l'algorithme du tri à bulles (Bubble Sort).

##############################################
#Solution
##############################################

def tri_a_bulles(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                print(L[j])
                L[j], L[j+1] = L[j+1], L[j]

# Exemple d'utilisation
liste = [9, 2, 5, 1, 7, 34, 54,23,1,6,8,3,5,65,7,23,654,8776,97,2,5,8]

print(liste)
