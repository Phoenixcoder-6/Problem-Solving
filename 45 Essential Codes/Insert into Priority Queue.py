class PriorityQueue:
    def __init__(self):
        self.heap=[]

    #Step-1 
    #Insert an element
    def push(self,val):
        self.heap.append(val) #Insert an element to the end
        self._heapify_up(len(self.heap)-1) #Restore heap property
    
    def pop(self):
        if not self.heap:
            return None
        root= self.heap[0]
        self.heap[0]= self.heap.pop()
        self._heapify_down(0)
        return root
        
        
    def _heapify_up(self,index):
        parent= (index-1)//2
        while index>0 and self.heap[index]< self.heap[parent]:
            self.heap[index],self.heap[parent]= self.heap[parent],self.heap[index]
            index=parent
            parent=(index-1)//2
    
    def _heapify_down(self,index):
        size= len(self.heap)
        smallest=index #Initially assume that the current node is the smallest.
        #Child node calculation
        left= 2*index +1
        right= 2*index+2
        #Check if left child node exists
        if left< size and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right<size and self.heap[right]<self.heap[smallest]:
            smallest=right
        if smallest != index:
            self.heap[index],self.heap[smallest]= self.heap[smallest],self.heap[index]
            self._heapify_down(smallest)

    def peek(self):
        return self.heap[0] if self.heap else None

l1=PriorityQueue()
l1.push(5)
l1.push(1)
l1.push(4)

print(l1.peek())
print(l1.pop())
print(l1.peek())

