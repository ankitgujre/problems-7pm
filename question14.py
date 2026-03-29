'''
turn every item in a list into its square
'''

# lst = [1, 2, 3, 4, 5]
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input("Enter a number: "))
    lst.append(num) 
    squared_lst = [num ** 2 for num in lst]
print("List of squared numbers:", squared_lst)

# squared_lst = [num ** 2 for num in lst]
# print("List of squared numbers:", squared_lst)
