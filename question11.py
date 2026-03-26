'''
wap to find sum of even and odd numbers in a list
'''
n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print("Sum of even numbers in the list is:", even_sum)
print("Sum of odd numbers in the list is:", odd_sum)
