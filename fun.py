# def helloworld():
#     print("Hello")
#     print("Bye")
#
#
# def sum(num1,num2):
#     result=num1+num2
#     print("The result is:",result)
#
#
from sys import get_int_max_str_digits


# # helloworld()
# sum(100,200)

# def print_name(name1,name2,name3):
#     print(name1,name2,name3)
#
# print_name("java","c","C++")

def maxnumber(*args):
    print(max(args))

maxnumber(102,3000,900)