'''
calculate sum of even number from 1 to n
'''

n = int(input("Enter a number: "))
sum_even = 0
if n < 1:
    print("Please enter a positive integer.")
for i in range(1, n + 1):
    
    if i % 2 == 0:
        sum_even += i
        print(i)
    
print("The sum of even numbers is:", sum_even)
