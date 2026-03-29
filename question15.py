'''
concatenate two lists
'''

lst1  = ["Hello", "World"]
lst2 = ["Python", "Programming"]
# lst3 = lst1 + lst2
print(lst1+lst2)
# print("Concatenated list:", lst3)

'''
concatenate two lists index wise'''

lst1 = ["Hello ", "World "]
lst2 = ["Python", "Programming"]
lst3 = []
for i in range(len(lst1)):
    lst3.append(lst1[i] + lst2[i])
print("Concatenated list index wise:", lst3)