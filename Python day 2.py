name="Lisa"
education='BE.CSE'
college='PSG COLLEGE'
percentage=89
print('My name is',name,'and I completed' ,education,'at' ,college)
print("My name is %s and I completed %s at %s"%(name,education,college))
print("My name is {} and I completed {} at {} and scored {}".format(name,education,college,percentage))
print("My name is {1} and I completed {2} at {0} and scored {3}".format(college,name,education,percentage))
print(f'My name is {name} and I completed {education} at {college} and scored {percentage}')
print(f'My name is {"Lisa"} and I completed {"BE.CSE"} at {"PSG College"} and scored {"89"}')
a=10
b=5
print(f"a+b")
print(f"{a+b}")
x=5.15
print(int(x))
print(float(x))
print(bool(x))
y=-5.15
print(bool(y))
print(bool(x+y))
list=[2,4,6,8,10,6]
print(len(list))
print(list.index(4))
print(list.count(6))
z=(20,15,5)
print(type(z))
print(sum(z))
information={'name':'Lisa','place':'Chennai','age':18}
print(information)
print(information['age'])
print(information.keys())
print(information.values())
print(information.items())
for key,value in information.items():
    print(key,value)
print(id(list))
list2=[1,2,3,4,5,6]
print(id(list2))
num={10,20,30,40,50}
print(type(num))
