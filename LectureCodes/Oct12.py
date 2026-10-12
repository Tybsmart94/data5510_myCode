lst = [3,1,4,1,5,9]

#Didn't work :(
#This doesn't work because it quickly goes out of range which is why the correct example specifies to only iterate through len(lst)-1
# print("ME:", lst)

# for i in lst:
#     for j in lst:
#         try:
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#         except:
#             print("Out of range lol")

# print("ME:", lst)

print("TEACH:", lst)

for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

print("TEACH:", lst)