'''
wap to find smallest number in a list
'''

n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("The smallest number in the list is:", smallest)
