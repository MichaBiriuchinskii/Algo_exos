
##############################################
#Task
##############################################
# Given a text as input, find and output the longest word.

##############################################
#Solution
##############################################

txt = input()

#your code goes here
texte = txt.replace(',', ' ').split()
premier = texte[0]

for i in texte:
    if len(i) > len(premier):
        premier = i


print(premier)
