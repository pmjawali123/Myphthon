#Different of types of Collection
#List,Tuple,Set,Dictionary

#print(list(range(10)))
###################### #xample2################
#list  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list = ["apple","Banana","Chery"]
# print(list2)
# mylist=list()
# print(mylist)
###################### #xample2################
# print(list[0])
# print(list[2])
# print(list[-2])
# print(list[-1])
######################Example#################
# list = ["apple","Banana","Chery","apple"]
# # print(list[-4:-1])
# # print(list[1:3])
#
# ######################Example 6#################
# list[0]="Orange"
# print(list)
# ###################### Example 7#################

# for i in list:
#     print(i)
#
# if "apple" in list:
#     print("yes")
# else:
#     print("no")
# ###################### Example 7   how to count #################
# mylist = ["apple","Banana","Chery","apple"]
# print(len(mylist ))

###################### Example 8   how to add into the listt #################
mylist = ["apple","Banana","Chery","apple"]
# mylist.append("Orange")
# print(mylist)
# mylist.insert(1,"manago")

#pop
# #mylist.pop(0)
# del mylist[3]
# print(mylist)
#
# mylist.clear()
# print(mylist)
###################### Example 8    #################

# mylist1 = ["apple","Banana","Chery","apple","sdfskdfks"]
# mylist2 = mylist1.copy()

mylist1 = [1,2,3]
mylist2 = ["a","b","c"]
for i in mylist2:
    mylist1.append(i)
print(mylist1)
