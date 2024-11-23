class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node= Node(data)
        new_node.next= self.head
        self.head= new_node

    def display(self):
        current= self.head
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print("None")


l1= linkedlist()
l1.insert_at_beginning(11)
l1.insert_at_beginning(22)
l1.insert_at_beginning(33)

l1.display()





