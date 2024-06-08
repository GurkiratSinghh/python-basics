'''
class car:
    def __init__(self,car_make,car_model,car_no):
        self.car_make=car_make
        self.car_model=car_model
        self.car_no=car_no
    def  show(self):
        print(self.car_make,self.car_model,self.car_no)
class rent(car):
    def __init__(self,car_make,car_model,car_no,time,price):
        car.__init__(self,car_make,car_model,car_no)
        self.time=time
        self.price=price
    def display_rent(self):
        print(self.car_make,self.car_model,self.car_no,self.time,self.price)
class owning(car):
    def __init__(self,car_make,car_model,car_no,ownership,price):
        car.__init__(self,car_make,car_model,car_no)
        self.ownership=ownership
        self.price=price
    def display_owning(self):
        print(self.car_make,self.car_model,self.car_no,self.ownership,self.price)

r=rent("mercedes","c220","PB02AQ0001","2 days",15000)
r.display_rent()
a=
o=owning("mercedes","g-class","PB02EQ0001","1st",15000000)
o.display_owning()
'''




'''
class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show(self):
        print(self.name,self.age,self.gender)
class student(person):
    def __init__(self,name,age,gender,rollno,stream):
        person.__init__(self,name,age,gender)
        self.rollno=rollno
        self.stream=stream
    def display_student(self):
        print(self.name,self.age,self.gender,self.rollno,self.stream)
class teacher(person):
    def __init__(self,name,age,gender,employee_id,department):
        person.__init__(self,name,age,gender)
        self.employee_id=employee_id
        self.department=department
    def display_teacher(self):
        print(self.name,self.age,self.gender,self.employee_id,self.department)
std=student("gurkirat singh",19,"male",30,"btech")
std.display_student()
tchr=teacher("rahul sir",42,"male",12315135,"computer science")
tchr.display_teacher()
'''
'''
# EXCEPTIONS
try:
    x=10
    y=0
    print(x/y)
except:
    print("a number cannot divisible by 0")




    
try:
    lst=[1,2,3]
    for i in range(0,5):
        print(lst[i])
        
except:
    print("some error")






try:
    x=int(input())
    y=int(input())
    z=x+y
    print(z)
except:
    print("empty string not allowed")
print("gurkirat")





try:
    a={"monday":"red color","tuesday":"orange color"}
    print(a.get("monday"))0
except:
    print("name is not defined")
finally:
    print("gurkirat")




#code
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        result = None
    finally:
        print("Division operation complete")
    
    return result

result1 = divide(10, 2)
print("Result 1:", result1)

result2 = divide(10, 0)
print("Result 2:", result2)

'''