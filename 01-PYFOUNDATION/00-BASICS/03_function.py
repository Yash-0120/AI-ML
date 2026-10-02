def start():
    print("hello world")

# start()
def greet(n):
    return n,"hello_world"

# gr=greet(1)
# print(type(gr))

def square(n):
    return n*n


# sq=square(5)
# print(sq)


# -------------ARGUMENT--------------

def emp(name,br,salary=10000):
    print("Name : ",name)
    print("Salary : ",salary)

# emp("yash",122)    

def numbers(*n):
    total=0
    for no in n:
        total+=no
    print(total)

# numbers(1,3,32,76,3)    

def kwargs(**z):
    print(z)

# kwargs(
#     name=100,
#     age=21,
#     branch="IT"
# ) 

# -------------PRACTICE-------------

def model(cgpa,attendance,internship=True):
    if cgpa>=7.5 and attendance>=75 and internship:
        return "Good"
    else:
        return"Needs Improvement"

predict=model(7.7,79)
# print(predict)

def sqr():
    nums=[1,2,3,4,5,6,7]
    squares=[]
    for num in nums:
        squares.append(num*num)
    return squares

# print(sqr())


# -----------------LAMBDA FUNCTION-----------------

add=lambda a,b:a+b
# print(add(1,3))

cube=lambda c:c**3
# print(cube(2))
# even nums from list
nums=[4,6,65,7,42,54,75]
def is_even(nos):
    return nos%2==0
x=list(filter(is_even,nums))
# print(x)

#--------------lambda with map----------------

result=list(map(lambda nos:nos*nos,nums))
# print(result)

# ----------lambda with filter------------------

result=list(filter(lambda num:num%2==0,nums))
# print(result)


result=list(filter(lambda x:x>10,nums))
# print(result)
results=list(filter(lambda x:x>15,nums))
# print(results)
res=list(map(lambda x:x**2,nums))
# print(res)

def is_even(n):
    return n%2==0

res=list(filter(is_even,nums))

# print(res)

numb = [2, 7, 4, 9, 1, 6, 3, 10]

res=list(filter(lambda x:x>5,numb))
# print(res)

names = ["Yash", "Om", "Rahul", "Amit", "Rohan", "Raj"]

res=list(filter(lambda x:len(x)>3,names))
# print(res)

# -----------------function with dict/list------------------

students = [
    {"name": "Yash", "cgpa": 8.5},
    {"name": "Rahul", "cgpa": 7.2},
    {"name": "Amit", "cgpa": 9.1}
]

toped_stud=list(filter(lambda student:student["cgpa"]>=8,students))
print(toped_stud)