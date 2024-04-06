# a set is a collection ( kind of data structure ) which is unordered , unindexed . No duplicate values.
basket = {'apple','orange', 'pear','banana'}
print(basket)

#checking for the elements in set
'orange' in basket #true
'crabgrass' in basket #false

# a dictionary is a set of key : with value pairs ( given that the keys are unique )
dict_example={'python':5,'css':0}
print(dict_example)
print(dict_example['python']) #5
print(sorted(dict_example)) #sorted alphabetically

# functions in python
def person(name,age):
    print(name)
    print(age)

# arguments in python
def sum(a,*b):
    print(a)
    print(b)
    sum=a
    for i in b:
        sum=sum+i

    print(sum)
sum(34,78,90,78)

# *args -> allows you to pass non-key arguments
# **kwargs -> allows you to pass keyword args
def print_address(**kwargs):
    for key , value in kwargs.items():
        print(key)

# calling the function
print_address(street='123 false street',
              city='Noida',
              state='Uttar Pradesh',
              zip='201309')

# ILLUSTRATION
def shipping_func(*args,**kwargs):
    for arg in args:
     print(arg)
     print()
    for key , value in kwargs.items():
        print(f"{key} , {value}")
        print()

shipping_func("dr","spongebob0","squarepants","III",
              street='123 fake',
              city='noida',
              state='Uttar Pradesh')

#learning about the input / output
import math
print(f'The value of pi is approximately {math.pi}.')

#opening files and reading and stuff
#open(filename,mode,encoding=None)

#errors-and-exception - event which stops the flow of program is called exception
#difference between exception and error - error cannot be handled
num1=int(input("enter the number of your choice :"))
num2=int(input("enter the second number of your choice : "))
try:
   div=num1/num2
   print(div)
except :
    print("division by zero is not possible")

#understanding the concept of classes and object of object oriented programming
