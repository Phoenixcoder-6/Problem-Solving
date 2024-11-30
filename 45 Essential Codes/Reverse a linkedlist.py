class node:
    def __init__(self,data):
        self.data= data
        self.next= None
class Linkedlist:
    def __init__(self):
        self.head= None
    def insert_element(self,data):
        new_node= node(data)
        if not self.head:
            self.head=new_node
            return
        current= self.head
        while current.next:
            current= current.next
        current.next= new_node

    def reverse(self):
        current=self.head
        prev=None
        while current:
            next_node= current.next
            current.next= prev
            prev= current
            current= next_node
        self.head= prev

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")


l1=Linkedlist()
l1.insert_element(10)
l1.insert_element(20)
l1.insert_element(30)
print("Original list:")
l1.display()

l1.reverse()
print("After reverse:")
l1.display()


        
