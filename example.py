#Write a python program to input a number and check whether it is positive, negative or zero

number=int(input("Enter the number:"))
if number<0:
    print("It is negative")
elif number>0:
    print("It is positive")
else:
    print("It is zero")
