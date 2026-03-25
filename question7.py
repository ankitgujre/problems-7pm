'''
remove duplicate elements from list
'''

lst = [1, 2, 3, 4, 5, 2, 3, 6]
remove_duplicate = list(set(lst))
print("Original list:", lst)
print("List after removing duplicates:", remove_duplicate)

