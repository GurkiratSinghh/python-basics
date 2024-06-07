# input command
'''
a=input("Marks of english")

print(a)
'''
# print differences with sep  or end 
'''

print ("Gurkirat","Singh")
print ("Gurkirat","Singh",sep=",")
print ("Gurkirat","Singh",end="")
print ("Gurkirat","Singh",sep=",",end="")
'''

# Type function
'''
a=98
print(type(a))
b=65.5
print(type(b))
h=1+7j
print(type(h))
'''
# Loops and conditional statement
'''
n=int(input("no. of terms in fabonacci"))
a=0
b=1
print(a,b,end=" ")
while n>=0:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    n=n-1
'''

# factorial
'''
n=int(input("No. which u want factorial"))
mul=1
while n!=1:
    mul=mul*n 
    n=n-1
print(mul)
'''
# functions
'''

def area(r):
    return 3.14*r**2

print(area(4))
'''
# functions


import array
k=array.array("i",[6,9,4,5,2])
def array(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
print(array(k))

# lambda function
'''

area = lambda x: x**2

result = area(5)
print(result) 

volume=lambda x,y,h:x*y*h
print(volume(2,3,4))
'''
#Map
'''


k = [41, 23,93, 54, 65]
j=[5,6,7,8,9]
l=[]
add = map(lambda k,j:k + j,k,j)
print(list(add)) 
'''
# filter
'''

a = [34,45,23,36,78]
divisible_3 = filter(lambda x: x % 3 == 0,a)

print(list(divisible_3))  
'''
# reduce
'''
from functools import reduce  

s = [1,7,9,"2"]
product = reduce(lambda q, r:q * r,s)
print(product)  
'''