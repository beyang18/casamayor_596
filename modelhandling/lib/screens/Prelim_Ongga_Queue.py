#Kent Gabriel Ongga - CCS 1301 SC: 526
print("---QUEUE---")

class queue:
    def __init__(self):
        self.items = []

    def queue(self, items):
        self.items.append(items)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")

        else:
            return self.items.pop(0)
        
    def front(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items[0]
        
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return self.items
    

q = queue()
q.queue("A")
q.queue("B")
q.queue("C")

print("Enqueueing: ", q.items)
print("Queue elements:", q.items)
print("Dequeue element:", q.dequeue())
print("Front element:", q.front())
print("Queue after dequeue:", q.display())
    

        
    


