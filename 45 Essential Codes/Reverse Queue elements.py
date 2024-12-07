from queue import Queue
def add_elements(elements):
    q= Queue()
    for elem in elements:
        q.put(elem)
    return q

def reverse_queue(q):
    stack=[]
    while not q.empty():
        stack.append(q.get())

    while stack:
        q.put(stack.pop())

    return q


elements=[10,20,30,40]
q= add_elements(elements)

print(list(q.queue))
res= reverse_queue(q)
print(list(res.queue))


