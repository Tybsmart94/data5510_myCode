#Order N
array = [3, 1, 4, 1, 5, 9, 2, 6]

largest = 0
secondLargest = 0
counter = 0

for num in array:
    if num > largest:
        largest = num

for i in range(len(array)):
    if array[i] > secondLargest and array[i] < largest:
        secondLargest = array[i]

print(largest)
print(secondLargest)