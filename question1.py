
'''
python program to find largest of thhree number
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    
    print("The largest number num1 ", num1)
elif (num2 >= num1) and (num2 >= num3):
    
    print("The largest number num2", num2)
else:
    print("The largest number num3", num3)