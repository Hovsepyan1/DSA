class Stack:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def push(self, item):
        self.arr.append(item)
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        item = self.arr.pop()
        self.size -= 1
        return item
    
    def top(self):
        if not self.is_empty():
            return self.arr[-1]  
        else:
            return None  
    
    def is_empty(self):
        return self.size == 0
    
    def size(self):
        return self.size
    
    def __str__(self):
        return f"{self.arr}"
    
    
# st = Stack()
# st.push(1)
# st.push(2)
# st.push(3)
# print(st)
# st.pop()
# print(st)
# print(st.top())


