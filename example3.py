#Write a python program to input a & b and check whether a is greater than b, a is lesser than b or a is equal to b

a=(input("Enter a number:"))
b=(input("Enter a number:"))
if (a<b):
    print("a is either less than or equal to b")
elif (a>b):
    print("a is greater than or equal to b")
else:
    print("a is equal to b")