class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")
    
    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return "Queue:" + "->".join(map(str,self.queue))

q= queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q)