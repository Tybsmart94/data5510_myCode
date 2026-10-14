#N squared
array = [-1, 0, 1, 2, 76, 2334, 55, 65, 3]

biggestDif = 0
difList = []


for num in array:
    for num2 in array:
        dif = num - num2
        difList.append(dif)
        if dif == max(difList):
            biggestDif = dif

print(difList)
print(biggestDif)

        
