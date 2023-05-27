##############################################
#Task
##############################################
# Given a sentence as input, calculate and output the average word length of that sentence.

##############################################
#Solution
##############################################

text = input()
list = text.split()
count = 0 
for i in list: 
	for p in i: 
		count += 1 
		
	
print(count/len(list))
