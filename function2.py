# def add(a,b):
#     print(a+b)
# if __name__=="__main__":
#     add(2,3)

# import math
# a=dir(math)
# print(len(a))
# print(a)

# a=2.345333333333
# print(round(a,2))

# import math
# a=20
# print(math.sqrt(a))

# import math
# a=2.9
# print(math.floor(a))

# import random
# list=[1,2,3,4,5,6,7,8]
# print(random.choice(list))

# import random
# r1=random.randint(5,15)
# print("Random number between 5 and 15 is % s" % (r1))
# r2=random.randint(-10,-2)
# print("Random number between -10 and -2 is %d" % (r2))

# import random
# sample_list=[1,2,3,4,5]
# print("original list:")
# print(sample_list)
# random.shuffle(sample_list)
# print("\nAfter the first shuffle:")
# print(sample_list)

# import random
# for i in range(50):
#     r1=random.randint(20,50)
#     print("The random integer between 20 to 50 is %s" %r1)

# import random
# a=[]
# b=int(input("Enter a number:"))
# for i in range(b):
#     a.append(random.randint(1,20))
# print("Randomised list is: ",a)

# import datetime
# x=datetime.datetime.now()
# print(x.year)
# print(x.strftime("%b"))

# import datetime
# x=datetime.datetime(2021,5,17)
# print(x) 
    
# data=list(range(2,30,2))
# print(data)

# data=["Sunil","Roshan",29]
# print(data)
# data.append(9)
# data.append('Programming')
# print(data)

# data=["Sunil","Roshan",29]
# print(data)
# data.insert(3,'Battle')
# print(data)

#Q.Write the difference between append, extend and insert?

# mixed_list=[{1,2},[5,6,7],{"a":"r"}]
# number_tuple=(3,4)
# mixed_list.insert(1,number_tuple)
# print("Updated list:",mixed_list)

#Update:
# data=["Sunil","Roshan",29]
# print(data)
# data[0]="HHH"
# data[1]=9
# data[2]=80
# print(data)

# data=["HHH","Orton", 16]
# print(data)
# del data[1]
# print(data)

# data=["Sunil","Roshan",29]
# print(data)
# data.pop()
# print(data)

# data=["Sunil","Roshan",29]
# data2=["Orton","HHH","Batista","Flair"]
# data4=["GG"]
# print(data+data2+data4)

# data=["Orton","HHH","Batista","Flair"]
# data2=[]
# data2=data.copy()
# print(data)
# print(data2)

# data=["Orton","HHH","Batista","Flair"]
# data2=["a","b",12]
# data.extend(data2)
# print(data)

# data=["Orton","Riddle"]
# data.clear()
# print(data)

# a=(10, "WOOWOOWOO")
# print(type(a)) 

# data=("Sunil","HHH","JBL")
# print(data[1])

# data=tuple(range(0,10,1))
# print(data)

# data=("Sunil","Roshan",29,["HHH","JBL",39])
# print(data)
# print(len(data))
# data[3].pop()
# print(data)
# data[3].append("Master")
# print(data)
# data[3].remove("JBL")
# print(data)

# print("Maximum is;", max(1,3,2,7))
# print("Minimum is:", min(1,3,2,7))

# Tuple1=("Edge","Ripley","Priest")
# print("Original list",Tuple1)
# list1=list(Tuple1)
# print("original list",list1)
# list1.insert(3,"Ciampa")
# print("changed list",list1)
# Tuple2=tuple(list1)
# print("adding new name in tuple",Tuple2)

# data={1,2,3,4}
# data.add(5)
# print(data)

# data={1,2,3,4,5}
# data.remove(2)
# print(data)

# data={"HHH","Orton","JBl"}
# data.discard("HHH")
# print(data)

# data={1,2,3,4,5,6,7,"HHH"}
# if "KING" in data:
#     print("Present")
# else:
#     print("Not present")

# data={1,2,3,4,5,6}
# data.clear()
# print(data)

# data={1,2,3,4,5,6}
# print(data)
# data.copy
# print(data)

# x={"a","b","c"}
# y={"b","d","f"}
# x.update(y)
# print(x)

# data1={1,2,3,4}
# data2={3,4,5,6}
# union_set = data1|data2
# print(union_set)

# data1={1,2,3,4}
# data2={3,4,5,6}
# union_set = (data1).union(data2)
# print(union_set)

# data1={1,2,3,4}
# data2={3,4,5,6}
# intersection_set = data1 & data2
# print(intersection_set)

# data1={1,2,3,4}
# data2={5,6,7,8}
# x=data1.isdisjoint(data2)
# print(x)

# data1={1,2,3,4}
# data2={1,2,3,4}
# x=data1.issubset(data2)
# print(x)

# data={"Name":"Ak","Age":18}
# print(data)

# data1=dict(Name="Ak",age=18)
# print(data1)

# data={"Name":"Ak","Age":18}
# print(data)
# for i in data:
#     print(i)

# for i in data.values():
#     print(i)
# for i in data.items():
#     print(i)

# data={"Name":"AK","Age":18}
# if "Name" in data:
#     print("Present")
# else:
#     print("Not present")
# if "AK"



# data={"Name":"AK","Age":20}
# data2={"Fav Movie":"3 idiots","Sport":"Football"}
# data.update(data2)
# print(data)

# data={"Name":"AK","Age":20}
# del data["Age"]
# print(data)

# data={"Name":"Dele Alli","Age":17}
# print(data)
# remove_pop=data.pop("Age")
# print(remove_pop)

# data={"Name":"AK","Age":20}
# print(data)
# data.clear()
# print(data)

# a_dict={"a":1,"B":2,"C":3}
# new_key="A"
# old_key="a"
# a_dict[new_key]=a_dict.pop(old_key)
# print(a_dict)

# thisdict= {   
#     "brand":"Marphak",
#     "model":"mustang",
#     "year":1964
# }
# print(thisdict)
# thisdict["year"]

