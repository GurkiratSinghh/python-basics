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