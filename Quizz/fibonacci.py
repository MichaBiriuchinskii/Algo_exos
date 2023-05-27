#############################################
#Tâche
##############################################
# Écrire une fonction fibo() qui prend comme paramètre un entier n et crée une liste d’entiers de longueur n + 1 comprenant dans l’ordre les nombres de la suite de Fibonacci jusqu’au rang n. La suite de Fibonacci est une suite d’entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent. Le terme de rang n, noté fn est défini par f0 = 0, f1 = 1 et fn = fn1 + fn2 pour n > 2. Par exemple, l’appel fibo(5) créera une liste comprenant les nombres : 0, 1, 1, 2, 3, 5

##############################################
#Solution
##############################################


def fibo(n):
  fb = [0, 1]
  for i in range(2,n+1):
    fb.append(fb[i-1]+fb[i-2])
  return fb[0:n+1]

print(fibo(43))
