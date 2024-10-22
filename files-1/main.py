class Stack:
    def __init__(self):
        self._data = [] # nonpublic list instance   
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e) # new item stored at end of list
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1] # the last item in the list
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop() # remove last item from list


#Driver Code
stack = Stack()
stack.push(5)
stack.push(3)
print(stack.top()) #Prints 3
stack.pop()
print(stack.top()) #Prints 5
