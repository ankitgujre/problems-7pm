'''
print length of list
'''
lst = [1, 2, 3, 4, 5]
print("Length of the list is:", len(lst))


'''
reverse a list
'''
lst = [1, 2, 3, 4, 5]
lst.reverse()
print("Reversed list:", lst)

'''
driver method

'''
def main():
    lst = [1, 2, 3, 4, 5]
    print("Length of the list is:", len(lst))
    lst.reverse()
    print("Reversed list:", lst)
if __name__ == "__main__":
    main()
