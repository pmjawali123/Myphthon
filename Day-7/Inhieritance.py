# class A:
#     def m1(self):
#         print("m1 method")
# class B(A):
#     def m2(selfs):
#         print("m2 method")
# class C(B):
#     def m3(self):
#         print("m3 method")
#
# p=A()
# p.m1()
# obj=C()
# obj.m2()
# obj.m1()
# obj.m3()


#
# class A:
#     def m1(self):
#         print("I am father")
# class B(A):
#     def m2(self):
#         print("I am Son")
# class C(A):
#     def m3(self):
#         print("I am Daughter")
#
# a=A()
# a.m1()
# b=B()
# b.m1()
# b.m2()
# c=C()
# c.m1()
# c.m3()

class Bank:
    def RateofIntereset(self):
        return 0

class ICICI(Bank):
    def RateofIntereset(self):
        return 10
class Axis(Bank):
    def RateofIntereset(self):
        return 20

objx=ICICI()
print(objx.RateofIntereset())

objA=Axis()
print(objA.RateofIntereset())





