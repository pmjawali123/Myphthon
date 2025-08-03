# class Person1():
#     def __init__(self):
#         print("Hello Python")
#
#
# p=Person1()
# q=Person1()

#
#
# class person():
#     def __init__(self,firstname,lastname):
#         print("Passing Parameter")
#         print("Hello " +firstname +"     "+lastname)
# p=person("Ram","Laxman")
#



class Base():
    def __init__(self):
        print("I am a base method")
#b=Base()

class Child(Base):
    def __init__(self):
        print("i am child class")
        print("I am learning automation Class")
c=Child()
c=Base()