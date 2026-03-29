'''
iterate both list simaltaneously

'''


lst1 = ["Hello", "World", "Python"]
lst2 = ["Programming", "is", "fun"]
for i in range(min(len(lst1), len(lst2))):
    print(lst1[i], lst2[i])
    