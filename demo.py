class Stack():
    def __init_(self):
        self.stack = []
        
    def empty(self):
        return len(self.stack) == 0
        
    def is_push(self,item):
        self.stack.append(item)
        
    def is_pop(self):
        if self.stack is not empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is Empty")
            
    def peek(self):
        if self.stack is not empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is Empty")
            
    def size(self):
        return len(self.stack)
        
        
stack = Stack()
stack.is_push(10)
stack.is_push(5)
stack.is_push(30)
    
print(len(stack))