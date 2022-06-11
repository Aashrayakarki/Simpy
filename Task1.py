#Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3"
a=input("Enter a number: ")
b=input("Enter a number: ")

if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")


#Print "Hello" if a is equal to b, and c is equal to d
a=input("Enter a: ")
b=input("Enter b: ")
c=input("Enter c: ")
d=input("Enter d: ")

if a==b and c==d:
    print("Hello")
else:
    print("Invalid")


#Print "Hello" if a is equal to b, or if c is equal to d
a=input("Enter a: ")
b=input("Enter b: ")
c=input("Enter c: ")
d=input("Enter d: ")

if a==b or c==d:
    print("Hello")


#For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0
x=float(input("Enter a number: "))

if x>0:
    print("True")
elif x<0:
    print("False")
else:
    print("Zero")


#Check whether the user input number is even or odd and display it to user
x=float(input("Enter a number: "))

if x%2==0:
    print("It is even")
else:
    print("It is odd")


#WAP which accepts marks of four subjects and display total marks, percentage and grade

sub1=int(input("enter your marks:"))
sub2=int(input("enter your marks:"))
sub3=int(input("enter your marks:"))
sub4=int(input("enter your marks:"))
total_marks=sub1+sub2+sub3+sub4
percentage=total_marks/4
print(total_marks)
print(percentage)
if percentage>=70:
    print("distinction")
elif percentage>=60:
    print("first division")
elif percentage>=40:
    print("pass")
else:
 print("fail")



#What is the output of ‘APPLE’ > ‘apple’?
print('APPLE'>'apple')


#Write a Python program to display your details like name, age, address in three different lines
name=input("What is your name?")
age=input("What is your age?")
address=input("Where is your home?")

print(name)
print(age)
print(address)


#Write a python program which accepts the radius of circle from user and compute the area
r = float(input("Enter the radius of the circle: "))
area = 3.1416 * r
print("Radius:", r)
print("Area = ", area)

#A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a<b and a<c:
    print(a,"is smallest number")
elif b<a and b<c:
    print(b,"is smallest number")
else:
    print(c,"is smallest number")

a=int(input('enter a number:'))
b=int(input('enter a number:'))
c=int(input('enter a number:'))
sum=a+b+c
print(sum)

b=int(input('enter length of base of right angled triangle:'))
h=int(input('enter height of right angled triangle: '))
area=(b*h)/2
print(area)






