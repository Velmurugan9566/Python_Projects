class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items += [item]  

    def pop(self):
        if not self.is_empty():
            popped_item = self.items[-1]
            new=[]
            for i in range(len(self.items)-1):
                new= new + [self.items[i]]
            self.items=new
            #self.items = self.items[:-1]  
            return popped_item
        else:
            print("Stack is empty. Cannot pop from an empty stack.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek into an empty stack.")
    def display(self):
        print(self.items)

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print("Top element:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)
stack.display()

