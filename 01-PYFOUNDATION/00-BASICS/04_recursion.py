def fact(n):
    result=1
    if(n==1):
        return 
    return n*fact(n-1)
# print(fact(5))

def countDown(n):
    if(n==0):
        return "stop"
    print(n)
    return countDown(n-1)
# print(countDown(10))
lists=[1,34,5,74,-54,234,344,255,2]
largest=0
for num in lists:
    if(num>largest):
        largest=num
# print(largest) 

def longSum(n):
    if(n==0):
        return 0

    return n+longSum(n-1)
# print(longSum(3))