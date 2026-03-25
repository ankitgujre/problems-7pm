'''
wap to check character is lowercase or uppercase
'''

a = input("Enter a character: ")
if a >= "A" and a <= "Z":
    print(a, "is an uppercase alphabet.")
elif a >= "a" and a <= "z":
    print(a, "is a lowercase alphabet.")
else:
    print(a, "is not an alphabet.")

ch = input("Enter a character: ")
if ch.isalpha():
    if ch.isupper():
        print(ch, "is an uppercase alphabet.")
    else:
        print(ch, "is a lowercase alphabet.")
else:
    print(ch, "is not an alphabet.")