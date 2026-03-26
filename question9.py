'''
fibonacci
'''
n = int(input("Enter any number: "))

a = 0
b = 1
if n < 1:
    print("Please enter positive number: ")
else:
    print("Fibonacci series: ", end="")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c