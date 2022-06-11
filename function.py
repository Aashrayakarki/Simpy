# a="Hello"
# b="Python\n"
# def abc():
#     print(a)
#     print(b*6)
# abc()

# def abc():
#     x=10
#     y=20
#     c=x+y
#     print(c)
# abc()

# def login(username,password):
#     print(f"Your username is {username} and password is {password}")
# login("Sunil","123")

# def login(username,email,phonenumber,password):
#     print(f"Your username is {username}, email address is {email}, phone number is {phonenumber} and password is {password} ")
# login("Ram","Ram7@gmail.com","9808750214","Ram123")

# def abc():
#     x=50
#     y=20
#     a=x+y
#     b=x*y
#     c=x-y
#     d=x/y
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# abc()

# def abc(a,b,c):
#     if a>b and a>c:
#         print("a is the greatest number")
#     if b>c and b>a:
#         print("b is the greatest number")
#     else:
#         print("c is the greatest number")
# abc(1,2,3)

# def sum():
#     a=[1,2,3,4]
#     sum=1
#     for i in a:
#         sum=sum*i
#     print(sum)
# sum()

# def abc():
#     a="python"
#     b=[]
#     for i in reversed(a):
#         b.append(i)
#         print(b)
# abc()

# def show(name,age):
#     print(f"Name: {name} Age:{age}")
# show(name="Sunil",age=20)

# def show(*num):
#     z=num[0]+num[1]+num[2]
#     print(z)
# show(5,4,3)

# def show(**num):
#     z=num['a']+num['b']+num['c']
#     print(z)
# show(a=5,b=4,c=3)

# def add(y):
#     x=10
#     return x+y
# sum=add(20)
# print(sum)

# def add(x,y):
#     c=x+y
#     d=y-x
#     return c,d
# sum,sub=add(10,20)
# print(sum)
# print(sub)

# def abc():
#     x=10
#     y=20
#     c=x+y
#     print(c)
# abc()

# def sum(a,b):
#     sum=a+b
#     print(sum)
# sum(10,20)

# def abc():
#     x=100
#     y=10
#     d=y/x
#     print(d)
# abc()

# def greatest(a,b,c):
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     c=int(input("Enter a number: "))
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     elif b>a:
#         if b>c:
#             return b
#         else:
#             return c
# x=greatest("a","b","c")
# print(f"The greatest number is {x}")

# def disp():
#     def show():
#         return "show function"
#     result=show() + "disp function"
#     return result
# a=disp()
# print(a)

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         nonlocal z
#         z=z+1
#         print(x)
#         print("inside the function",y)
#     inner()
#     print("z:",z)
# outer()

# y=10
# def inner():
#         x=4
#         print(x)
#         print("inside the function",y)
# print("y:",y)
# inner()

# y=10
# def inner():
#         x=4
#         global y
#         y=y+1
#         print(x)
#         print("inside the function",y)
# print("y:",y)
# inner()

# x=10
# def outer():
#     x=8
#     def inner():
#         x=4
#     inner()
# print(x)
# outer()  

# def outer():
#     x="local"
#     def inner():
#         nonlocal x
#         x="nonlocal"
#         print("Inner:",x)
#     inner()
#     print("Outer:",x)
# outer()

# result=lambda n1,n2,n3: n1+n2+n3
# print("Sum of three values: ", result(10,20,30))

# result=lambda x,y: (x/y, x*y)
# a,b=result(5,2)
# print(a)
# print(b)

# lst= [5,7,22,97,54,62,77,23,73,61]
# square_list=list(map(lambda x:x**2, lst))
# print(square_list)

# a=[1,2,3]
# b=[3,4,5]
# abc=list(map(lambda x,y:x+y,a,b))
# print(abc)

# data=[1,2,3,4,5,6,6,7,9,10]
# abc=list(filter(lambda x:x%3==0,data))
# print(abc)

