# def sum():
#     a=[8,2,3,-1,7]
#     sum=1
#     for i in a:
#         sum=sum*i
#     print(sum)
# sum()


# def sum():
#     a=[8,2,3,0,7]
#     sum=0
#     for i in a:
#         sum=sum+i
#     print(sum)
# sum()


# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter Third number: "))

# def abc():
#     if(a<=b) and (a<=c):
#         s=a
#     elif(b<=a) and (b<=c):
#          s=b
#     else:
#          s=c
#     print("Smallest number among  the three is",s)
# abc()


# def fizz_buzz(x):
#     if x%3==0 & x%5==0:
#         return "FizzBuzz"
#     elif x%3==0:
#         return"Fizz"
#     elif x%5==0:
#         return"Buzz"
#     else:  
#         return x
# print(fizz_buzz(30))


# def abc(name,age):
#     print("name=", name)
#     print("age=", age)
# abc("AK", 18)


# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter Third number: "))

# def abc():
#     if(a>=b) and (a>=c):
#         l=a
#     elif(b>=a) and (b>=c):
#          l=b
#     else:
#          l=c
#     print("Largest number among  the three is",l)
# abc()


# def abc(a):
#     b=[]
#     for i in a:
#         if i%2==0:
#             b.append(i)
#     return b
# print(abc([1,2,3,4,5,6]))


# def abc(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n%x==0):
#                 return False
#         return True
# print(abc(43))


# def func(a):
#     return a[::-1]
# text=func("Hello there")
# print(text)


# def abc(name,age):
#     print(name,age)
# abc("AK", 18)


# def func1(*num):
#     print(*num)
# func1("Hey","Hello","Hi","78")


# def calculation(a,b):
#     sum = a+b
#     sub = a-b
#     return sum, sub
# z=calculation(22,28)
# print(z)


# def show_employee(name, salary=9000):
#     print("Name:",name,  "Salary:",salary)
# show_employee("AK", 12500)
# show_employee("Jimmy")


# x=[4,6,8,24,12,2]
# print(max(x))


# x=[4,6,8,24,12,2]
# print(min(x))


# def abc(roll):
#     x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#     if roll in x:
#         print(f"Roll number {roll} is present")
#     else:
#         print(f"Roll number {roll} is absent")
# roll=int(input("Enter roll number: "))
# abc(roll)


# def abc(num):
#     if num%2==0:
#         print("The number is even")
#     else:
#         print("The number is odd")
# num=int(input("Enter a number: "))
# abc(num)


# word=input("Enter a word: ")
# vowels=0
# consonants=0

# for i in word:
#     if 'a'==i or 'e'==i or 'i'==i or 'o'==i or 'u'==i or 'A'==i or 'E'==i or 'I'==i or 'O'==i or 'U'==i:
#         vowels=vowels+1
#     else:
#         consonants=consonants+1
# print("The number of vowels: ",vowels)
# print("n/The number of consonants: ",consonants)




# def area():
#     r=float(input(f"Input the radius of circle: "))
#     a=3.142*r**2
#     return f"The area of the circle is {a}"
# print(area())


# 