'''
factorial
'''

n = int(input("Enter any number: "))
fact = 1
if n < 1:
    print("Please enter positive number")
else:
    for i in range(1, n+1):
        fact = fact * i

print("factorial = ", fact)