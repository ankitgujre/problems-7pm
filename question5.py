'''
wap to check character is alphabet digit or special character
'''

a = input("Enter a character: ")
if a >= "A" and a <= "Z" or a >= "a" and a <= "z":
    print(a, "is an alphabet.")
elif a >= "0" and a <= "9":
    print(a, "is a digit.")
else:
    print(a, "is a special character.")