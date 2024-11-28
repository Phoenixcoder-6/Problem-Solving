class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head= None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current= self.head
        while current.next:
            current=current.next
        current.next=new_node

    def find_middle_element(self):
        slow= self.head
        fast= self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

# Example usage:
ll = Linkedlist()
for i in [15, 23, 425]:
    ll.append(i)

print("Middle element:", ll.find_middle_element()) 
