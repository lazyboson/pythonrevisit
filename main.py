print('Hello World!')
x = 1
if x == 1:
    print('x is one')

print("Goodbye World!")

myint = 7
print(myint)

myfloat = 7.0
print(myfloat)

_float = float(10)
print(_float)

mystring = "india"
print(mystring)

a,b = 3,4
print(a, b)

one = 1
two = 2
hello = "hello"
#error - mixed operators are not supported 
#print(one + two + hello)

myString= "hello"
myFloat = float(10)
myInt = 20
if myString == "hello":
    print("String: %s" %mystring)
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" %myfloat)
if isinstance(myInt, int) and myInt == 20:
    print("Integer: %d" %myInt)

my_list = []
my_list.append(10)
my_list.append('hello')
my_list.append(1)
my_list.append('3')
my_list.append(30)
print(my_list)

for x in my_list:
    print(x)

#Airthmatic operations
number = 1 + 2*3 / 4.0
print(number)