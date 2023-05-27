##############################################
#Task
##############################################
# Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

##############################################
#Solution
##############################################


a = input()
b = input()

c = a.count(b)
d = len(a)

print(int((c/d) * 100))
