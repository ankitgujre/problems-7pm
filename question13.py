'''
wap to swap elements at given positions in a list
'''

lst =  [1, 2, 3, 4, 5]
pos1 = int(input("Enter the first position to swap: "))
pos2 = int(input("Enter the second position to swap: "))
temp = lst[pos1 - 1]
lst[pos1 - 1] = lst[pos2 - 1]
lst[pos2 - 1] = temp
print("List after swapping elements:", lst)
