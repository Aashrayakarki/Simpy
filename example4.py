#Write a python program to input one number from the user. Print “Century” if the number is 100, "Half-century" if the number is 50, otherwise print "Enter a valid number"

a=int(input("Enter the number:"))
if a==100:
    print("Century")
elif a==50:
    print("Half-Century")
else:
    print("Enter a valid number")
