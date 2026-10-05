import random

#List comprehension
lst = [random.randint(1,100) for x in range(100)] #To understand it, start with the for loop, then read the first part (which is what is being put into the list)
print("lst: \n", lst)

lst2 = [2 ** x for x in range(11)]
print("lst2: \n", lst2)

