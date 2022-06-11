txt1="My name is {name} & I'm {age}".format(name="Ak",age=18)
txt2="My name is {0} & I'm {1}".format("Ak",18)
txt3="My name is {} & I'm {}".format("Ak",18)
print(txt1)
print(txt2)
print(txt3)

name= 'Raj'
age= 30
print( "my name is " + name + "and my age is" + str(age))
print("my name is {} and my age is {}".format(name,age))

print("Hello {}, your balance is {},".format("adam",230))
print("Hello {0}, your balance is {1},".format("adam",230))
print("Hello {name}, your balance is {blc},".format(name="adam",blc=230))
print("Hello {0}, your balance is {blc},".format("adam",blc=230))

quantity=3
items=300
price=49.65
myorder= "I want to pay {2} dollars for {0} pieces of item {1},"
print(myorder.format(quantity,items,price))

a=2
b=4
c=8
print(f"The product of {a} and {b} is {c} ")

name=input()
n=input("What is your name")
mobile=input("enter your mobile number")
print(name)
print(n)
print(mobile)

