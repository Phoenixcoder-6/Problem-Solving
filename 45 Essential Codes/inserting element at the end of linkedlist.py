class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head= new_node
        else:
            current= self.head
            while current.next:
                current= current.next
            current.next= new_node
    
    def display(self):
        current= self.head
        while current is not None:
            print(current.data,end="->")
            current=current.next
        
        print("None")


l1= linkedlist()
l1.insert_at_end(10)
l1.insert_at_end(20)
l1.insert_at_end(30)
l1.insert_at_end(40)

l1.display()

    