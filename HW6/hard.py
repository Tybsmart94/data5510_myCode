#Imports
import random

#Inputs to initialize the list
lowest = int(input("Enter a low number: "))
highest = int(input("Enter a MUCH higher number than the previous entry: "))

lst = []

for i in range(10):
    lst.append(random.randint(lowest, highest))

#with max function (n^2)
biggestDif = 0
difList = []

for num in lst:
    for num2 in lst:
        dif = num - num2
        difList.append(dif)
        if dif == max(difList):
            biggestDif = dif

print(lst)
# print(difList)
print(biggestDif)

#without max function (O(n^2) according to chat)
biggestDif2 = 0
difList2 = []

for num in lst:
    for num2 in lst:
        dif = num - num2
        difList2.append(dif)

for num in difList2:
    if num > biggestDif2:
        biggestDif2 = num

# print(difList2)
print(biggestDif2)

#Prompts sent to chat
# what would the big O notation of this code be:

# for num in lst:
#     for num2 in lst:
#         dif = num - num2
#         difList.append(dif)

# for num in range(len(difList)):
#     if num > biggestDif2:
#         biggestDif2 = num
