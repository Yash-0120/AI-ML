# -------------LIST------------------


a=[1,3,"yash"]

a[1]=5 #change the value at specific index
a.append(2)
a.insert(1,4)
a.remove(4)
# a.clear()

# iteration over the list


# for item in a:
    # print(item)

# -------------TUPLE--------------

li=[1,3,2,4,4,5]
# print(li)
# print(tuple(li))

# print(a[1:])
# print(li[::-1])
# print(li+a)
# b,*c,d=li
# print(b,c,d)

# -------------SET-----------------

s=set({1,23,4,4,6,1})
fs={1,3,4,64}
s.add(35)


# print(s)
# print(s.union(fs))
# print(s.intersection(fs))
# print("difference is :",s.difference(fs))


# ---------------DICTIONARY-------------
# name=input("Enter the name:")
# age=input("Enter the age:")
# branch=input("Enter the branch:")
# cgpa=input("Enter the CGPA:")
# student={
#     "name":name,
#     "age":age,
#     "branch":branch,
#     "cgpa":cgpa
# }
# print(student.keys())
# print(student.values())
# print(student["name"])
# for _ in student:
#     print(_," : ",student[_] )
