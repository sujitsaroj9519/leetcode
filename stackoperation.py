class Stack():
    def __init__(self):
        self.stack =[]

    def empty(self):
        return len(self.stack) == 0
    
    def is_push(self, item):
        self.stack.append(item)

    def is_pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is Empty")
        
    def is_peek(self):
        if not self.empty():
            return self.stack[-1]
        else:
            raise IndentationError("Stack is empty")
    
    def size(self):
        return len(self.stack)
    

stack = Stack()

stack.is_push(10)
stack.is_push(20)
stack.is_push(30)

print(stack.empty())
# print(stack.stack)
print(stack.is_peek())
print(stack.stack)
print(stack.size())

print(stack.is_pop())
print(stack.is_pop())
print(stack.stack)
print(stack.size())
print(stack.empty())
print(stack.is_peek())
        
    


    