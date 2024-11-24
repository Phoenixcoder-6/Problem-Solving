class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class Linkedlist:
    def __init__(self):
        self.head= None
    def append(self,data):
        new_node= Node(data)
        if not self.head:
            self.head= new_node
        else:
            current=self.head
            while current.next:
                current= current.next
            current.next= new_node

    def insert_middle(self,data):
        if not self.head:
            new_node= Node(data)
            return
        slow= self.head
        fast= self.head

        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next

        new_node= Node(data)
        new_node.next= slow
        prev.next=new_node

    def display(self):
        current= self.head
        while current:
            print(current.data,end='->')
            current=current.next
        print("None")

l1= Linkedlist()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)

print("Original list:")
l1.display()

l1.insert_middle(25)
print("After inserting 25 in the middle:")
l1.display()




