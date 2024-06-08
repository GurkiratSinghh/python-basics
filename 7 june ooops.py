#oops practice
'''
class multiplication:
    a=7
    def mul(self):
        multiplication.a*=2

o=multiplication()
o.mul()
print(multiplication.a)
o.mul()
o.mul()
print(multiplication.a)
'''
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def append(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=Node(data)
    def display(self):
        if self.head==None:
            print("LL is empty")
        else:
            current=self.head
            while current!=None:
                print(current.data,end="->")
                current=current.next

    def search(self, target):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                if current.data == target:
                    print("Target found")
                    break
                current = current.next
            else:
                print("Target not found")

a=LL()
a.append(9)
a.append(14)
a.append(67)
a.append(29)
a.append(93)
a.display()
a.search(67)
a.search(2)
"""
# class creation

# class ClassName:
    #statement
    
# object creation

#obj=ClassName()
# print(obj.attribute)                      Attributes are the variables that belong to a class.
#                                    Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute
# example

#class Dog:
 #   sound="Bark"
    
'''An object consists of:

State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects
'''
'''
# a class
class Dog:

    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

'''
'''
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print("Hello my name is " + self.name+" and I" +
              " work in "+self.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()
'''
'''
class GFG:
    def __init__(somename, name, company):
        somename.name = name
        somename.company = company

    def show(somename):
        print("Hello my name is " + somename.name +
              " and I work in "+somename.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()
'''
'''

class message:
    pass
    def hi(self``):
        print("hi how are you")

a=message()
a.hi()
'''
'''
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()
'''
'''
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def __str__(self):
        return f"My name is {self.name} and I work in {self.company}."


my_obj = GFG("John", "GeeksForGeeks")
print(my_obj)

'''
'''
class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):

        # Instance Variable
        self.breed = breed
        self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)

'''
'''
class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):

        # Instance Variable
        self.breed = breed
        self.color = color

    def detailb_buzzo(self):
        print("Details of Buzzo:\nBuzzo is a",self.animal,"\nBuzzo's breed is",self.breed,"and color is",self.color)
    
    def detailb_rodger(self):
        print("Details of rodger:\nrodger is a",self.animal,"\nrodger's breed is",self.breed,"and color is",self.color)    
a1=Dog("pug","Black")
a2=Dog("Sitzu","White")
a1.detailb_buzzo()
a2.detailb_rodger()
'''

class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed):

        # Instance Variable
        self.breed = breed
    def __str__(self):
        return f"detail of the {self.animal}"
    
    

    # Adds an instance variable
    def setColorbreed(self, color):
        self.color = color

    # Retrieves instance variable
    def getColorbreed(self):
        print(self.breed,self.color)


# Driver Code
Rodger = Dog("pug")
Rodger.setColorbreed("brown")
print(Rodger)
Rodger.getColorbreed()

