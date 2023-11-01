class Stack:
    def __init__(self):
        self.stack =[]

    def empty():
        return len(self.stack) == 0
    
    def is_push(self,item):
        self.stack.append(item)

    def is_pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")
    def is_peek(self):
        if not self.empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return len(self.stack)
    
obj = Stack()
print(obj.is_push(10))
print(obj.is_push(30))
obj.is_push(90)

print(obj.stack)

print(obj.size())
print(obj.is_pop())
        