# d=float(input("How far did you travel today (in miles)?"))
# t=float(input("How long did it take you (in hours)?"))

# s=d/t

# print("Your speed was " + str(s) + " miles per hour ")


import pdb
bike1 = "yamaha"
bike1_price = 250000

bike2 = "Honda"
bike2_price = 500000

pdb.set_trace()
name = input("Enter your name:")
choose=int(input("press 1 for yamaha and 2 for honda:"))
print(f"Hello {name}")

if choose==1:
    print(f"{bike1} will cost you {bike1_price}")
if choose==2:
    print(f"{bike2} will cost you {bike2_price}")
else:
    print("Enter 1 or 2 only")