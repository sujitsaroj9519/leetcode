class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is Empty")
        
    def size(self):
        return len(self.queue)
    

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.queue)
print(queue.size())
print(queue.peek())

print(queue.is_empty())
print(queue.dequeue())
print(queue.queue)
print(queue.enqueue(100))
print(queue.queue)